from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate
from crud.user import create_user as crud_create_user
from crud.user import verify_user as crud_verify_user

router = APIRouter()

# Register user
@router.post(
            "/register",
            description="Create a new user",
            status_code=status.HTTP_201_CREATED
)
async def create_user(user: UserCreate):
    try:
        if crud_create_user(user.username, user.password):
            return {"message": "User created successfully"}
        else:
            raise HTTPException(status_code=400, detail="Could not create user")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Login user
@router.post(
            "/login",
            description="Login user",
            status_code=status.HTTP_200_OK
)
async def login_user(user: UserCreate):
    try:
        if crud_verify_user(user.username, user.password):
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))