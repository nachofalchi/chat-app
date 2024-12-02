from models.user import User as db

def register_user(username, password):
    if not db.register_user(username, password):
        return False
    return True

def login_user(username, password):
    if not db.login_user(username, password):
        return False
    return True
    
def validate_user(username):
    return db.validate_user(username)