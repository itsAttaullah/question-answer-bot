from fastapi import FastAPI, Depends # type: ignore
from fastapi.responses import StreamingResponse # type: ignore
from sqlalchemy.orm import Session # type: ignore
from db import SessionLocal, engine, Base
from crud import create_message, get_last_messages
from schemas import MessageCreate
from utils import stream_groq_response
import json

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Chat endpoint with streaming
@app.post("/chat")
async def chat(user_msg: MessageCreate, db: Session = Depends(get_db)):
    # 1. Save user message
    create_message(db, user_msg)

    # 2. Retrieve last 10 messages from DB
    messages_db = get_last_messages(db, limit=10)
    messages = [{"role": m.role, "content": m.content} for m in messages_db]

    # 3. Call Groq API (stream response)
    async def event_generator():
        assistant_reply = ""
        async for chunk in stream_groq_response(messages):
            try:
                data = json.loads(chunk)
                delta = data["choices"][0]["delta"].get("content", "")
                if delta:
                    assistant_reply += delta
                    yield delta
            except:
                continue
        # Save assistant reply after streaming ends
        create_message(db, MessageCreate(role="assistant", content=assistant_reply))

    return StreamingResponse(event_generator(), media_type="text/plain")


# New endpoint to fetch last N messages
@app.get("/history")
def get_history(limit: int = 10, db: Session = Depends(get_db)):
    messages_db = get_last_messages(db, limit=limit)
    return [{"role": m.role, "content": m.content} for m in messages_db]
