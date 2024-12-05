from pydantic import BaseModel, EmailStr, Field, constr
from datetime import datetime
from typing import List

class EmailSchema(BaseModel):
    sender: EmailStr
    recipient: EmailStr
    subject: str = Field(max_length=100)
    body: str = Field(max_length=10000)
    timestamp: datetime = Field(default=datetime.utcnow())
    is_read: bool = Field(default=False)
    folder: str = Field(
        default="inbox",
        pattern="^(inbox|sent|drafts|trash)$"
    )
    
class EmailOut(BaseModel):
    id: int
    sender: EmailStr
    recipient: EmailStr
    subject: str = Field(max_length=100)
    body: str = Field(max_length=10000)
    timestamp: datetime = Field(default=datetime.utcnow())
    is_read: bool = Field(default=False)
    folder: str = Field(
        default="inbox",
        pattern="^(inbox|sent|drafts|trash)$"
    )
    @classmethod
    def from_db(cls, email_dict):
        return cls(**{
        "id": email_dict["id"],
        "sender": email_dict["sender"],
        "recipient": email_dict["recipient"],
        "subject": email_dict["subject"],
        "body": email_dict["body"],
        "timestamp": email_dict["timestamp"],
        "is_read": email_dict["is_read"],
        "folder": email_dict["folder"]
    })


class EmailInbox(BaseModel):
    id : int
    sender: EmailStr
    subject: str = Field(max_length=100)
    timestamp: datetime = Field(default=datetime.utcnow())
    is_read: bool = Field(default=False)
    folder: str = Field(
        default="inbox",
        pattern="^(inbox|sent|drafts|trash)$"
    )

class EmailList(BaseModel):
    emails: List[EmailInbox]

    @classmethod
    def from_db(cls, email_list):
        email_schemas = [
            EmailInbox(
                id = email.id,
                sender=email.sender,
                subject=email.subject,
                timestamp=email.timestamp,
                is_read=email.is_read,
                folder=email.folder
            ) 
            for email in email_list
        ]
        return cls(emails=email_schemas)