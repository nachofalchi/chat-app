from models.user import User as db

def create_user(username, password):
    if not db.register_user(username, password):
        return False
    return True

def verify_user(username, password):
    return db.verify_password(username, password)