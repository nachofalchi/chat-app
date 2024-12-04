# models/__init__.py
from .base import Base, engine
from .user import User
from .email import Email

# Create all tables
Base.metadata.create_all(engine)