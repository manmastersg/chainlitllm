import json
import os
import time
import traceback

from openai import AsyncOpenAI

import chainlit as cl


# Load LLM Configuration from llm_settings.json
# Note: This is called fresh each time to pick up any settings changes
def load_llm_config():
    config_path = os.path.join(os.path.dirname(__file__), "llm_settings.json")
    with open(config_path) as f:
        config = json.load(f)

    # Get the first active provider
    active_provider = next(
        (p for p in config["providers"] if p.get("is_active")), config["providers"][0]
    )
    return active_provider


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


@cl.on_chat_start
async def start():
    # Only greet and initialize if this is a fresh session
    if cl.user_session.get("history") is None:
        user = cl.user_session.get("user")
        role = user.metadata.get("role", "unknown")

        # Initialize message history
        cl.user_session.set(
            "history",
            [
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Provide direct textual answers. Do NOT attempt to use functions or tool calls.",
                }
            ],
        )

        await cl.Message(
            content=f"Welcome {user.display_name}! Your authenticated role is: **{role}**."
        ).send()


@cl.on_message
async def main(message: cl.Message):
    try:
        # Get history from session
        history = cl.user_session.get("history")
        history.append({"role": "user", "content": message.content})

        # SLIDING WINDOW: Keep only the last 10 messages (plus system prompt)
        if len(history) > 11:
            history = [history[0]] + history[-10:]
            cl.user_session.set("history", history)

        # Start timer
        start_time = time.perf_counter()

        # Show a "Thinking" status
        status_msg = cl.Message(content="*Thinking...*", author="System")
        await status_msg.send()

        # ---- RELOAD LLM CONFIG DYNAMICALLY ON EACH MESSAGE ----
        llm_config = load_llm_config()

        # Recreate the OpenAI client with current settings
        client = AsyncOpenAI(
            base_url=llm_config["base_url"], api_key=llm_config["api_key"]
        )
        model_name = llm_config["model"]
        # ------------------------------------------------------

        # Call LLM with current config settings
        response = await client.chat.completions.create(
            model=model_name,
            messages=history,
            stream=False,
            extra_body={"enable_thinking": llm_config.get("enable_thinking", False)},
        )

        # DEBUG: Log the raw response structure
        print(f"DEBUG LLM Response: {response.model_dump_json()}")

        # End timer
        end_time = time.perf_counter()
        duration = end_time - start_time

        content = response.choices[0].message.content

        # Remove the status message
        await status_msg.remove()

        if content:
            # Add assistant response to history
            history.append({"role": "assistant", "content": content})
            cl.user_session.set("history", history)

            # Calculate metrics
            usage = response.usage
            completion_tokens = usage.completion_tokens if usage else 0
            tokens_per_sec = completion_tokens / duration if duration > 0 else 0

            # Create metrics text
            metrics_text = (
                f"⏱️ Total: {duration:.2f}s | "
                f"🚀 {tokens_per_sec:.1f} tok/s | "
                f"📝 {completion_tokens} tokens"
            )

            # Send message with metrics
            await cl.Message(
                content=content,
                elements=[
                    cl.Text(name="Metrics", content=metrics_text, display="inline")
                ],
            ).send()
        else:
            # Handle empty content (log raw response for debugging)
            debug_info = (
                f"\n\nRaw Response: ```json\n{response.model_dump_json(indent=2)}\n```"
            )
            await cl.Message(
                content=f"Error: Received empty response from LLM.{debug_info}"
            ).send()

    except Exception as e:
        error_msg = f"An error occurred: {e!s}\n\n```\n{traceback.format_exc()}\n```"
        await cl.Message(content=error_msg).send()
