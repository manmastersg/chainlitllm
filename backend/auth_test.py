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
        
        # Start timer
        start_time = time.perf_counter()
        
        # Call OpenAI (Qwen)
        response = await client.chat.completions.create(
            model="qwen3.6-plus",
            messages=history,
            stream=False,
        )
        
        # End timer
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        content = response.choices[0].message.content
        if content:
            # Add to history
            history.append({"role": "assistant", "content": content})
            cl.user_session.set("history", history)
            
            # Calculate metrics
            usage = response.usage
            total_tokens = usage.total_tokens if usage else 0
            completion_tokens = usage.completion_tokens if usage else 0
            tokens_per_sec = completion_tokens / duration if duration > 0 else 0
            
            # Create metrics text
            metrics_text = (
                f"⏱️ {duration:.2f}s | "
                f"🚀 {tokens_per_sec:.1f} tok/s | "
                f"📝 {completion_tokens} tokens"
            )
            
            # Send message with metrics as an element
            await cl.Message(
                content=content,
                elements=[
                    cl.Text(name="Metrics", content=metrics_text, display="inline")
                ]
            ).send()
        else:
            await cl.Message(content="Error: Received empty response from LLM.").send()

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}\n\n```\n{traceback.format_exc()}\n```"
        await cl.Message(content=error_msg).send()
