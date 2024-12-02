from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import UserCreate
from crud.user import register_user as crud_register_user
from crud.user import login_user as crud_login_user
from auth.utils import validate_token, generate_token

router = APIRouter()

# Register user
@router.post(
            "/register",
            description="Create a new user",
            status_code=status.HTTP_201_CREATED
)
async def create_user(user: UserCreate):
    try:
        if crud_register_user(user.username, user.password):
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
        if crud_login_user(user.username, user.password):
            generated_token = generate_token(user.username)
            return {"message": "Login successful", "token": generated_token}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Private endpoint
@router.get(
            "/private",
            description="Private endpoint",
            status_code=status.HTTP_200_OK
)
async def private_endpoint(validated_token: bool = Depends(validate_token)):
    if not validated_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "This is a private endpoint"}