# models.py
from sqlalchemy import create_engine, Column, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

Base = declarative_base()
engine = create_engine('sqlite:///chat.db')
Session = sessionmaker(bind=engine)

class UserDatabase(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True, unique=True)
    password_hash = Column(String)

    @classmethod
    def verify_password(cls, username, password):
        session = Session()
        try:
            user = session.query(UserDatabase).filter_by(username=username).first()
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
            user = UserDatabase(username=username, password_hash=password_hash)
            session.add(user)
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False
        finally:
            session.close()

Base.metadata.create_all(engine)