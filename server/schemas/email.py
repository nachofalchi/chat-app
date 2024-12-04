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
class EmailList(BaseModel):
    emails: List[EmailSchema]

    @classmethod
    def from_db(cls, email_list):
        email_schemas = [
            EmailSchema(
                sender=email.sender,
                recipient=email.recipient,
                subject=email.subject,
                body=email.body,
                timestamp=email.timestamp,
                is_read=email.is_read,
                folder=email.folder
            ) 
            for email in email_list
        ]
        return cls(emails=email_schemas)