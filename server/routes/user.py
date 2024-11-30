from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate
from crud.user import create_user as crud_create_user

router = APIRouter()

# Register user
@router.post(
            "/",
            status_code=status.HTTP_201_CREATED,
            description="Create a new user"
)
async def create_user(user: UserCreate):
    try:
        if crud_create_user(user.username, user.password):
            return {"message": "User created successfully"}
        else:
            raise HTTPException(status_code=400, detail="Could not create user")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))