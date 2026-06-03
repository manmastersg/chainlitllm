import json
import os
import re
import time
import traceback

from httpx import AsyncClient, Limits, Timeout
from openai import AsyncOpenAI

import chainlit as cl

# ---- Shared OpenAI client (reused across messages to keep httpx pool warm) ----
_shared_openai_client = None
_shared_client_config_hash = None  # tracks which config this client was built for


def _get_openai_client():
    """Return a shared AsyncOpenAI client, recreating only if the config changed."""
    global _shared_openai_client, _shared_client_config_hash

    config_path = os.path.join(os.path.dirname(__file__), "llm_settings.json")
    with open(config_path) as f:
        config = json.load(f)
    active = next(
        (p for p in config["providers"] if p.get("is_active")), config["providers"][0]
    )
    # Stable hash so we can detect config changes
    cfg_hash = (active["base_url"], active["model"], active["api_key"])

    if _shared_openai_client is not None and _shared_client_config_hash == cfg_hash:
        return _shared_openai_client

    # Build a shared httpx client so the connection pool persists across calls
    http_client = AsyncClient(
        http2=True,
        timeout=Timeout(30.0, connect=10.0),
        limits=Limits(max_connections=10, max_keepalive_connections=5),
    )

    _shared_openai_client = AsyncOpenAI(
        base_url=active["base_url"],
        api_key=active["api_key"],
        http_client=http_client,
    )
    _shared_client_config_hash = cfg_hash
    return _shared_openai_client


async def _warm_openai_client():
    """Send a lightweight request to warm the httpx connection pool at startup."""
    try:
        client = _get_openai_client()
        # Fetch models list — cheap, fast, warms the TLS + HTTP connection
        print("[warmup] Warming httpx connection pool...")
        await client.models.list()
        print("[warmup] httpx connection pool warmed (via models.list)")
    except Exception as e:
        print(f"[warmup] models.list() failed: {e}")
        try:
            # Fallback: make a tiny chat completion to warm the pool
            print("[warmup] Retrying with trivial chat completion...")
            model = "deepseek-v4-flash-free"
            if _shared_client_config_hash:
                model = _shared_client_config_hash[1]
            await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "ok"}],
                stream=False,
                max_tokens=1,
            )
            print("[warmup] httpx connection pool warmed (via chat completion)")
        except Exception as e2:
            print(f"[warmup] all warmup attempts failed: {e2}")


# ---- Wiki paths ----
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.join(SCRIPT_DIR, "..", "wiki")
WIKI_INDEX_PATH = os.path.join(WIKI_DIR, "index.md")


# ---- File-based system prompt ----
DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful assistant. Provide direct textual answers. "
    "Do NOT attempt to use functions or tool calls."
)


def resolve_system_prompt_path():
    """Return the path to the system prompt Markdown file.

    Resolution order:
      1. SYSTEM_PROMPT_FILE env var (explicit override)
      2. prestart.md next to this script (convention-based auto-detect)

    Returns None if none exist — caller falls back to DEFAULT_SYSTEM_PROMPT.
    """
    env_path = os.environ.get("SYSTEM_PROMPT_FILE")
    if env_path:
        abs_env = os.path.abspath(os.path.expanduser(env_path))
        if os.path.isfile(abs_env):
            return abs_env

    # Convention: prestart.md alongside auth_test.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prestart = os.path.join(script_dir, "prestart.md")
    if os.path.isfile(prestart):
        return prestart

    return None


def load_system_prompt():
    """Read the system prompt from a Markdown file, or return the default string."""
    path = resolve_system_prompt_path()
    if path is None:
        return DEFAULT_SYSTEM_PROMPT
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read().strip()
        print(f"[system prompt] Loaded from {path} ({len(content)} chars)")
        return content
    except OSError as e:
        print(f"[system prompt] Failed to read {path}: {e}")
        return DEFAULT_SYSTEM_PROMPT


def load_llm_config():
    """Load LLM configuration from llm_settings.json adjacent to this script."""
    config_path = os.path.join(os.path.dirname(__file__), "llm_settings.json")
    with open(config_path) as f:
        config = json.load(f)

    # Get the first active provider
    active_provider = next(
        (p for p in config["providers"] if p.get("is_active")), config["providers"][0]
    )
    return active_provider


# ---- Wiki retrieval helpers ----


def read_wiki_index():
    """Read wiki/index.md and return its content, or '' if missing."""
    if not os.path.isfile(WIKI_INDEX_PATH):
        print("[wiki] index.md not found")
        return ""
    with open(WIKI_INDEX_PATH, encoding="utf-8") as f:
        return f.read()


def read_wiki_pages(filenames):
    """Read specific wiki .md files and return concatenated content.

    Handles both 'filename.md' and 'filename' (appends .md automatically).
    Skips missing files gracefully.
    """
    chunks = []
    for fname in filenames:
        if not fname.endswith(".md"):
            fname += ".md"
        path = os.path.join(WIKI_DIR, fname)
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                content = f.read().strip()
            chunks.append(f"### From {fname}\n{content}")
            print(f"[wiki] Loaded {fname} ({len(content)} chars)")
        else:
            print(f"[wiki] Skipped (not found): {fname}")
    return "\n\n".join(chunks)


async def select_relevant_pages(client, model_name, question, index_content):
    """Ask the LLM which wiki pages are relevant to the question.

    Returns a list of filenames (e.g. ['mps-series.md', 'prism-options.md']).
    This is a cheap, focused call — just index navigation.
    """
    prompt = (
        "You are a precise wiki navigator. A user is asking about the PRISM product family.\n\n"
        f"Wiki table of contents:\n{index_content}\n\n"
        f"User question: {question}\n\n"
        "Which wiki pages contain information relevant to this question?\n"
        'Return ONLY a JSON array of filenames. Example: ["mps-series.md", "prism-options.md"]\n'
        "If nothing is relevant, return []. Do not include index.md."
    )
    try:
        resp = await client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            stream=False,
        )
        content = resp.choices[0].message.content or ""
        print(f"[wiki navigator] Raw: {content[:300]}")
        # Extract JSON array via regex (handles markdown code fences)
        match = re.search(r"\[.*?\]", content, re.DOTALL)
        if match:
            pages = json.loads(match.group())
            if isinstance(pages, list):
                return pages
    except Exception as e:
        print(f"[wiki navigator] Error: {e}")
    return []


def is_trivial_message(text):
    """Check if the message is a greeting or trivial — skip wiki retrieval."""
    text = text.strip().lower()
    greetings = {
        "hi",
        "hello",
        "hey",
        "hi!",
        "hello!",
        "hey!",
        "good morning",
        "good afternoon",
        "good evening",
        "sup",
        "yo",
        "howdy",
    }
    return text in greetings or (
        len(text) < 5
        and not any(
            kw in text
            for kw in [
                "prism",
                "mps",
                "mpd",
                "mpp",
                "telestream",
                "option",
                "format",
                "spec",
                "what",
                "how",
                "which",
                "tell",
                "explain",
            ]
        )
    )


def is_list_query(text):
    """Check if the user is asking to list/show all wiki files — bypass navigator.

    Only matches questions about wiki *structure* itself (what pages exist),
    NOT general 'show me all X' content questions (e.g. 'show all options').
    """
    t = text.strip().lower()
    list_phrases = [
        "what files",
        "how many pages",
        "how many files",
        "list files",
        "all pages",
        "all files",
        "show files",
        "list of pages",
        "list of files",
        "what md",
        "what .md",
        "file listing",
        "page listing",
        "wiki structure",
    ]
    return any(phrase in t for phrase in list_phrases)


# ---- Auth ----

# Temporary user store
users = {
    "admin": {"password": "admin", "role": "admin", "name": "Administrator"},
    "user": {"password": "user", "role": "user", "name": "Standard User"},
}


@cl.password_auth_callback
async def auth_callback(username: str, password: str):
    if username in users and users[username]["password"] == password:
        user_data = users[username]
        return cl.User(
            identifier=username,
            display_name=user_data["name"],
            metadata={"role": user_data["role"]},
        )
    return None


# ---- Chat handlers ----


@cl.on_chat_start
async def start():
    if cl.user_session.get("history") is None:
        user = cl.user_session.get("user")
        role = user.metadata.get("role", "unknown")

        system_content = load_system_prompt()

        cl.user_session.set(
            "history",
            [{"role": "system", "content": system_content}],
        )

        # Warm the httpx connection pool BEFORE showing the welcome message,
        # so the pool is guaranteed ready when the user types their first message.
        await _warm_openai_client()

        await cl.Message(
            content=f"Welcome {user.display_name}! Your authenticated role is: **{role}**."
        ).send()


@cl.on_message
async def main(message: cl.Message):
    try:
        # --- Update conversation history ---
        history = cl.user_session.get("history")
        history.append({"role": "user", "content": message.content})

        # SLIDING WINDOW: Keep only the last 10 messages (plus system prompt)
        if len(history) > 11:
            history = [history[0]] + history[-10:]
            cl.user_session.set("history", history)

        start_time = time.perf_counter()
        t_log = [("start", start_time)]

        # --- Get reusable OpenAI client (connection pool stays warm) ---
        client = _get_openai_client()
        t_log.append(("get_client", time.perf_counter()))

        active_provider = next(
            (
                p
                for p in json.load(
                    open(os.path.join(os.path.dirname(__file__), "llm_settings.json"))
                )["providers"]
                if p.get("is_active")
            ),
            None,
        )
        if active_provider is None:
            config_path = os.path.join(os.path.dirname(__file__), "llm_settings.json")
            with open(config_path) as f:
                active_provider = json.load(f)["providers"][0]
        model_name = active_provider["model"]
        stream_enabled = active_provider.get("enable_streaming", False)
        t_log.append(("read_config", time.perf_counter()))

        # === PROGRESS STATUS (updates in-place) ===
        status_msg = cl.Message(content="", author="System")
        await status_msg.send()
        t_log.append(("status_sent", time.perf_counter()))

        async def update_status(text):
            status_msg.content = text
            await status_msg.update()

        # === DECIDE: wiki retrieval or quick reply? ===
        needs_wiki = not is_trivial_message(message.content)

        if needs_wiki:
            await update_status("📖 Reading wiki index...")

            # Step 1: Read the index
            index_content = read_wiki_index()

            if is_list_query(message.content):
                # Meta-question about wiki structure — list ALL files directly
                await update_status("📂 Listing all wiki pages...")
                all_files = sorted(
                    f
                    for f in os.listdir(WIKI_DIR)
                    if f.endswith(".md") and f != "index.md"
                )
                file_listing = "\n".join(f"- {f}" for f in all_files)
                wiki_context = (
                    f"## Complete Wiki File Listing\n\n"
                    f"There are {len(all_files)} wiki pages available:\n\n{file_listing}"
                )
                relevant_pages = all_files  # All pages are "relevant" for listing
                print(f"[wiki] List query — all {len(all_files)} files")

            else:
                # Step 2: Quick navigation call — which pages are relevant?
                relevant_pages = []
                if index_content:
                    await update_status("🔍 Searching relevant pages...")
                    relevant_pages = await select_relevant_pages(
                        client, model_name, message.content, index_content
                    )
                    print(f"[wiki] Pages selected: {relevant_pages}")

                # Step 3: Read only those pages from disk
                wiki_context = read_wiki_pages(relevant_pages) if relevant_pages else ""

            # Step 4: Build augmented messages
            system_msg = history[0]
            augmented_messages = [system_msg]

            if wiki_context:
                augmented_messages.append(
                    {
                        "role": "system",
                        "content": f"## Retrieved from PRISM Wiki\n\n{wiki_context}",
                    }
                )

            augmented_messages.extend(history[1:])
        else:
            # Trivial message — skip wiki entirely, respond directly
            print(f"[wiki] Skipped retrieval for trivial message: {message.content!r}")
            augmented_messages = list(history)

        t_log.append(("before_api_call", time.perf_counter()))

        await update_status("🤖 Generating answer...")

        # === STREAMING ANSWER ===
        if stream_enabled:
            t_log.append(("stream_create_start", time.perf_counter()))
            # Stream tokens into the SAME status message — no gap, no flash
            stream = await client.chat.completions.create(
                model=model_name,
                messages=augmented_messages,
                stream=True,
                extra_body={
                    "enable_thinking": active_provider.get("enable_thinking", False)
                },
            )
            t_log.append(("stream_created", time.perf_counter()))

            full_content = ""
            thinking_content = ""  # thinking trace if present
            first_token = True
            first_output_token = True
            async for chunk in stream:
                # Check for thinking/reasoning content (separate field)
                delta = chunk.choices[0].delta if chunk.choices else None
                if delta:
                    # DeepSeek/openai-compatible thinking field
                    chunk_thinking = getattr(delta, "reasoning_content", None) or (
                        delta.model_extra.get("reasoning_content")
                        if hasattr(delta, "model_extra") and delta.model_extra
                        else None
                    )
                    if chunk_thinking:
                        thinking_content += chunk_thinking
                        continue  # Don't show thinking in the message
                    if delta.content:
                        if first_token:
                            t_log.append(("first_token", time.perf_counter()))
                            first_token = False
                        if first_output_token and thinking_content:
                            # First actual output token — log thinking length
                            print(
                                f"[thinking] {len(thinking_content)} chars of reasoning stripped"
                            )
                            first_output_token = False
                            # Clear the "Generating answer..." status now that real output starts
                            status_msg.content = ""
                            await status_msg.update()
                        full_content += delta.content
                        await status_msg.stream_token(delta.content)

            t_log.append(("stream_done", time.perf_counter()))

            end_time = time.perf_counter()
            duration = end_time - start_time

            # Print breakdown
            # Only show API-related timing tags (skip the 0ms preliminaries)
            api_labels = {
                "stream_create_start",
                "stream_created",
                "first_token",
                "stream_done",
            }
            break_parts = []
            for i in range(1, len(t_log)):
                label, ts = t_log[i]
                _prev_label, prev_ts = t_log[i - 1]
                delta_ms = (ts - prev_ts) * 1000
                print(
                    f"[timing] {label}: +{delta_ms:.0f}ms  (cumulative: {(ts - start_time) * 1000:.0f}ms)"
                )
                if label in api_labels:
                    break_parts.append(f"{label}={delta_ms:.0f}ms")

            # Try to extract token usage from last chunk (provider-dependent)
            usage = getattr(chunk, "usage", None)
            completion_tokens = (
                usage.completion_tokens if usage else len(full_content.split())
            )

            metrics_text = (
                f"⏱️ {duration:.2f}s | "
                f"{completion_tokens} tok | "
                f"{' | '.join(break_parts[:4])}"
            )

            status_msg.elements = [
                cl.Text(name="Metrics", content=metrics_text, display="inline")
            ]
            await status_msg.update()

        else:
            # Non-streaming fallback
            response = await client.chat.completions.create(
                model=model_name,
                messages=augmented_messages,
                stream=False,
                extra_body={
                    "enable_thinking": active_provider.get("enable_thinking", False)
                },
            )

            end_time = time.perf_counter()
            duration = end_time - start_time

            full_content = response.choices[0].message.content or ""

            await status_msg.remove()

            usage = response.usage
            completion_tokens = usage.completion_tokens if usage else 0

            metrics_text = (
                f"⏱️ Total: {duration:.2f}s | "
                f"🚀 {completion_tokens / duration:.1f} tok/s | "
                f"📝 {completion_tokens} tokens"
            )

            await cl.Message(
                content=full_content,
                elements=[
                    cl.Text(name="Metrics", content=metrics_text, display="inline")
                ],
            ).send()

        # --- Update history ---
        if full_content:
            history.append({"role": "assistant", "content": full_content})
            cl.user_session.set("history", history)
        else:
            debug_info = "\n\nRaw response not available."
            await cl.Message(
                content=f"Error: Received empty response from LLM.{debug_info}"
            ).send()

    except Exception as e:
        error_msg = f"An error occurred: {e!s}\n\n```\n{traceback.format_exc()}\n```"
        await cl.Message(content=error_msg).send()
