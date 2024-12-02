# models/user.py
from sqlalchemy import Column, String
from .base import Base, Session
import bcrypt
from sqlalchemy.exc import IntegrityError

class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True, unique=True)
    password_hash = Column(String)

    @classmethod
    def login_user(cls, username, password):
        session = Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if not user:
                return False
            return bcrypt.checkpw(password.encode(), user.password_hash)
        finally:
            session.close()
    
    @classmethod
    def register_user(cls, username, password):
        session = Session()
        try:
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User(username=username, password_hash=password_hash)
            session.add(user)
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def validate_user(cls, username):
        session = Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                return True
            return False
        finally:
            session.close()