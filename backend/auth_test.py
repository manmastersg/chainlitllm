import chainlit as cl
from openai import AsyncOpenAI
import traceback
import time

# LLM Configuration
client = AsyncOpenAI(
    base_url="http://127.0.0.1:3000/openai-qwen-oauth/v1",
    api_key="admin123"
)

# Temporary user store
users = {
    "admin": {"password": "admin", "role": "admin", "name": "Administrator"},
    "user": {"password": "user", "role": "user", "name": "Standard User"}
}

@cl.password_auth_callback
async def auth_callback(username: str, password: str):
    if username in users and users[username]["password"] == password:
        user_data = users[username]
        return cl.User(
            identifier=username,
            display_name=user_data["name"],
            metadata={"role": user_data["role"]}
        )
    return None

@cl.on_chat_start
async def start():
    user = cl.user_session.get("user")
    role = user.metadata.get("role", "unknown")
    
    # Initialize message history
    cl.user_session.set("history", [{"role": "system", "content": "You are a helpful assistant."}])
    
    await cl.Message(
        content=f"Welcome {user.display_name}! Your authenticated role is: **{role}**. You can now chat with the LLM."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    try:
        # Get history from session
        history = cl.user_session.get("history")
        history.append({"role": "user", "content": message.content})
        
        # SLIDING WINDOW: Keep only the last 10 messages (plus system prompt)
        # This keeps the history from growing indefinitely and speeds up processing
        if len(history) > 11:
            history = [history[0]] + history[-10:]
            cl.user_session.set("history", history)

        # Create a message to stream results
        msg = cl.Message(content="")
        
        # Start timer
        start_time = time.perf_counter()
        ttft = None
        token_count = 0
        
        # Show a "Thinking" status
        await cl.Message(content="*Thinking...*", author="System").send()

        # Call OpenAI (Qwen) with streaming
        stream = await client.chat.completions.create(
            model="qwen3.6-plus",
            messages=history,
            stream=True,
        )
        
        async for part in stream:
            if not part.choices:
                continue
                
            token = part.choices[0].delta.content or ""
            if token:
                if ttft is None:
                    ttft = time.perf_counter() - start_time
                
                token_count += 1
                await msg.stream_token(token)

        # End timer
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        # Finalize
        content = msg.content
        if content:
            history.append({"role": "assistant", "content": content})
            cl.user_session.set("history", history)
            
            tokens_per_sec = token_count / duration if duration > 0 else 0
            metrics_text = (
                f"⏱️ Total: {duration:.2f}s | "
                f"⚡ TTFT: {ttft:.2f}s | "
                f"🚀 {tokens_per_sec:.1f} tok/s | "
                f"📝 {token_count} chunks"
            )
            
            msg.elements = [cl.Text(name="Metrics", content=metrics_text, display="inline")]
            await msg.send()
        else:
            await cl.Message(content="Error: Received empty response from LLM.").send()

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}\n\n```\n{traceback.format_exc()}\n```"
        await cl.Message(content=error_msg).send()
