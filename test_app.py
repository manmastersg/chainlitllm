# Simple Chainlit app to test the LLM Settings feature
import chainlit as cl

@cl.on_chat_start
async def start():
    await cl.Message(
        content="# Welcome to Chainlit! 🚀\n\nYour forked version with LLM Settings is running.\n\nNavigate to `/admin/settings/llm` to access the LLM configuration panel (requires admin login)."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content=f"You said: `{message.content}`. This is a placeholder response from your custom Chainlit instance."
    ).send()