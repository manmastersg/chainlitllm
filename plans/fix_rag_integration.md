# Plan: Fix RAG Integration in auth_test.py

The objective is to enable Retrieval-Augmented Generation (RAG) in the `auth_test.py` Chainlit app so that the LLM can refer to documents indexed via the `PageIndexService`.

## Key Files
- `myproject/chainlitsrc/backend/auth_test.py`: The main application script.
- `myproject/chainlitsrc/backend/pageindex_service.py`: The service providing document indexing and retrieval.

## Implementation Steps

1. **Modify `myproject/chainlitsrc/backend/auth_test.py`**:
    - Import `get_pageindex_service` from `pageindex_service`.
    - Update the `@cl.on_message` handler (`main` function):
        - Before calling the LLM, retrieve the `PageIndexService` instance.
        - Show a status message "Searching knowledge base..." while retrieving context.
        - Call `svc.build_rag_context(message.content)` to get relevant document information.
        - Prepend the retrieved context to the user's message *only for the current LLM call* (avoiding bloating the persisted conversation history).
        - Update the LLM call to use this augmented message.

2. **Verification**:
    - Start the application using `./start_chainlitsrc.sh`.
    - Upload a badminton court booking invoice (if not already present).
    - Ask "How much is the court".
    - Verify that the assistant provides the correct price based on the PDF content (RM 59.36).

## Details of Changes in `auth_test.py`

```python
# Import at the top
from pageindex_service import get_pageindex_service

# ...

@cl.on_message
async def main(message: cl.Message):
    try:
        # 1. Get history from session
        history = cl.user_session.get("history")
        history.append({"role": "user", "content": message.content})
        
        # SLIDING WINDOW: Keep only the last 10 messages (plus system prompt)
        if len(history) > 11:
            history = [history[0]] + history[-10:]
            cl.user_session.set("history", history)

        # 2. Search knowledge base
        status_msg = cl.Message(content="*Searching knowledge base...*", author="System")
        await status_msg.send()
        
        svc = get_pageindex_service()
        # Use asyncio.to_thread to avoid blocking the event loop while querying
        context = await asyncio.to_thread(svc.build_rag_context, message.content)
        
        await status_msg.update(content="*Thinking...*")

        # 3. Prepare messages for LLM (include context if found)
        llm_messages = history.copy()
        if context:
            # Prepend context to the last user message for the LLM prompt
            last_msg = llm_messages[-1].copy()
            last_msg["content"] = context + last_msg["content"]
            llm_messages[-1] = last_msg

        # 4. Call LLM
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=llm_messages, # Use augmented messages
            stream=False,
            extra_body={
                "enable_thinking": llm_config.get("enable_thinking", False)
            }
        )
        
        # ... rest of the existing logic ...
```

## Migration & Rollback
- Since this is a simple script modification, rollback is just reverting the changes in `auth_test.py`.
