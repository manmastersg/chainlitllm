# Simple Chainlit app with authentication for LLM Settings access
import chainlit as cl

# Simple user store
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
        content=f"# Welcome, {user.display_name}! 👋\n\nYour role: **{role}**\n\nGo to `/admin/settings/llm` to configure LLM settings (admin only)."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content=f"You said: `{message.content}`. This is a test response from your Chainlit instance."
    ).send()