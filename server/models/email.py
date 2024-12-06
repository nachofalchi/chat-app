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
    def add_email(cls, email: EmailSchema, username):
        session = Session()
        try:
            new_email = Email(
                sender=username,
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
            emails = session.query(Email).filter_by(recipient=recipient, folder='inbox').all()
            return emails
        finally:
            session.close()

    @classmethod
    def get_email(cls, recipient, id):
        session = Session()
        try:
            email = session.query(Email).filter_by(recipient=recipient, id = id).first()
            email.is_read = True
            session.commit()
            if not email:
                return False
            email_dict = {
                "id": email.id,
                "sender": email.sender,
                "recipient": email.recipient,
                "subject": email.subject,
                "body": email.body,
                "timestamp": email.timestamp,
                "is_read": email.is_read,
                "folder": email.folder
            }
            return email_dict
        finally:
            session.close()

    @classmethod
    def delete_email(cls, recipient, id):
        session = Session()
        try:
            email = session.query(Email).filter_by(recipient=recipient, id = id).first()
            if not email:
                return False
            email.folder = 'trash'
            session.commit()
            return True
        finally:
            session.close()
    
    # Trash
    @classmethod
    def get_trash_emails(cls, recipient):
        session = Session()
        try:
            emails = session.query(Email).filter_by(recipient=recipient, folder='trash').all()
            return emails
        finally:
            session.close()