from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from jwt import decode, ExpiredSignatureError
import os
from dotenv import load_dotenv
from crud.user import validate_user

load_dotenv('config.env')

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_token(username):
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), "sub": username}    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validate_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode(token, SECRET_KEY, algorithms=ALGORITHM, options={"verify_exp": False})
        username = payload.get("sub")
        if not validate_user(username):
            return False
        return True
    except ExpiredSignatureError:
        return False