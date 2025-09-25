from sqlalchemy.orm import Session # type: ignore
from models import Message
from schemas import MessageCreate

def create_message(db: Session, msg: MessageCreate):
    db_msg = Message(role=msg.role, content=msg.content)
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg

def get_last_messages(db: Session, limit: int = 10):
    return db.query(Message).order_by(Message.timestamp.desc()).limit(limit).all()[::-1]
