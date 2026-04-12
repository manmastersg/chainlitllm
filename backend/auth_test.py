import chainlit as cl
from openai import AsyncOpenAI

# LLM Configuration (from test_llm_connection.py)
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
    
    await cl.Message(
        content=f"Welcome {user.display_name}! Your authenticated role is: **{role}**. You can now chat with the LLM."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Create a streaming message
    msg = cl.Message(content="")
    
    # Call OpenAI (Qwen)
    stream = await client.chat.completions.create(
        model="qwen3-coder-plus",
        messages=[{"role": "user", "content": message.content}],
        stream=True,
    )

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    await msg.send()
