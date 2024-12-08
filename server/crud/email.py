from models.email import Email as db
from schemas.email import EmailSchema, EmailList, EmailOut

# CRUD ops for inbox

def send_email(email : EmailSchema, username):
    if not db.add_email(email, username):
        return False
    return True

def get_emails(username):
    email_list = db.get_emails(username)
    if not email_list:
        return []
    else:
        return EmailList.from_db(email_list)
    
def get_email(username,id):
    email = db.get_email(username,id)
    if not email:
        return False
    else:
        return EmailOut.from_db(email)

def delete_email(username,id):
    if not db.delete_email(username,id):
        return False
    return True

def get_trash_emails(username):
    email_list = db.get_trash_emails(username)
    if not email_list:
        return []
    else:
        return EmailList.from_db(email_list)
    
def get_sent_emails(username):
    email_list = db.get_sent_emails(username)
    if not email_list:
        return []
    else:
        return EmailList.from_db(email_list)
    
def get_draft_emails(username):
    email_list = db.get_draft_emails(username)
    if not email_list:
        return []
    else:
        return EmailList.from_db(email_list)

def save_draft(email, username):
    if not db.save_draft(email, username):
        return False
    return True
