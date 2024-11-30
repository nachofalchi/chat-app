# models/message.py
from sqlalchemy import Column, String, DateTime, ForeignKey
from .base import Base
from datetime import datetime

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(String, primary_key=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String, ForeignKey('users.username'))