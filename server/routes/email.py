from fastapi import APIRouter, HTTPException, status, Depends
from schemas.email import EmailSchema
from auth.utils import validate_token
from crud.email import send_email as crud_send_email
from crud.email import get_emails as crud_get_emails

router = APIRouter()

@router.post(
            "/send_email",
            description="Send an email",
            status_code=status.HTTP_201_CREATED,
            responses={
                201: {
                    "description": "Email sent successfully",
                },
                400: {
                    "description": "Could not send email"
                },
                401: {
                    "description": "Authentication failed"
                },
                500: {
                    "description": "Internal server error"
                }
            }

)
async def send_email(email: EmailSchema, _: bool = Depends(validate_token)):
    try:
        success = crud_send_email(email)
        if not success:
            raise HTTPException(status_code=400, detail="Could not send email")
        else:
            return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error sending email: {str(e)}"
        )

@router.get(
            "/inbox",
            description="Get all emails in inbox",
            status_code=status.HTTP_200_OK,
            responses={
                200: {
                    "description": "Emails retrieved successfully"
                },
                400: {
                    "description": "Could not retrieve emails"
                },
                401: {
                    "description": "Could not validate credentials"
                }
            }
)
async def get_inbox(username = Depends(validate_token)):
    try:
        emails = crud_get_emails(username)
        if emails is None:
            return {"message": "No emails found"}
        else:
            return emails
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}"
        )