# models/__init__.py
from .base import Base, engine
from .user import User
from .message import Message

# Create all tables
Base.metadata.create_all(engine)