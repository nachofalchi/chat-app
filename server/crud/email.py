from models.email import Email as db
from schemas.email import EmailSchema, EmailList

def send_email(email : EmailSchema):
    if not db.add_email(email):
        return False
    return True

def get_emails(username):

    email_list = db.get_emails(username)
    if not email_list:
        return []
    else:
        return EmailList.from_db(email_list)
        
