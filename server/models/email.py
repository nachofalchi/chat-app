# models/email.py
from sqlalchemy import Column, String, DateTime, Boolean, Integer
from datetime import datetime
from .base import Base, Session
from sqlalchemy.exc import IntegrityError
from schemas.email import EmailSchema

class Email(Base):
    __tablename__ = 'emails'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    sender = Column(String, nullable=False)
    recipient = Column(String, nullable=False)
    subject = Column(String)
    body = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
    folder = Column(String, default='inbox')


    @classmethod
    def add_email(cls, email: EmailSchema):
        session = Session()
        try:
            new_email = Email(
                sender=email.sender,
                recipient=email.recipient,
                subject=email.subject,
                body=email.body
            )
            session.add(new_email)
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def get_emails(cls, recipient):
        session = Session()
        try:
            emails = session.query(Email).filter_by(recipient=recipient).all()
            return emails
        finally:
            session.close()