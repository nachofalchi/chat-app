from fastapi import APIRouter, HTTPException, status, Depends
from schemas.email import EmailSchema
from auth.utils import validate_token
from crud.email import send_email as crud_send_email
from crud.email import get_emails as crud_get_emails
from crud.email import get_email as crud_get_email
from crud.email import delete_email as crud_delete_email
from crud.email import get_trash_emails as crud_get_trash_emails
from crud.email import get_sent_emails as crud_get_sent_emails
from crud.email import get_draft_emails as crud_get_draft_emails
from crud.email import save_draft as crud_save_draft


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
async def send_email(email: EmailSchema, username = Depends(validate_token)):
    try:
        success = crud_send_email(email, username)
        if not success:
            raise HTTPException(status_code=400, detail="Could not send email")
        else:
            return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error sending email: {str(e)}"
        )

# Inbox

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
    
@router.get(
            "/inbox/get_email",
            description="Get a specific email",
            status_code=status.HTTP_200_OK,
            responses={
                200: {
                    "description": "Email retrieved successfully"
                },
                400: {
                    "description": "Could not retrieve email"
                },
                401: {
                    "description": "Could not validate credential"
                }
            }
)
async def get_email(id: int,username = Depends(validate_token)):
    try:
        email = crud_get_email(username,id)
        if email is None:
            return {"message": "Email not found"}
        else:
            return email
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving email: {str(e)}"
        )
    
@router.delete(
            "/inbox/delete_email",
            description="Delete a specific email",
            status_code=status.HTTP_200_OK,
            responses={
                200: {
                    "description": "Emails retrieved successfully"
                },
                400: {
                    "description": "Could not retrieve email"
                },
                401: {
                    "description": "Could not validate credential"
                }
            }
)
async def delete_email(id: int,username = Depends(validate_token)):
    try:
        success = crud_delete_email(username,id)
        if success:
            return {"message": "Email deleted successfully"}
        else:
            return {"message": "Email not deleted"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting email: {str(e)}"
        )
    
# Trash
@router.get(
            "/trash",
            description="Get all emails in trash",
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
async def get_trash(username = Depends(validate_token)):
    try:
        emails = crud_get_trash_emails(username)
        if emails is None:
            return {"message": "No emails found"}
        else:
            return emails
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}"
        )
    
# Sent
@router.get(
            "/sent",
            description="Get all sent emails",
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
async def get_sent(username = Depends(validate_token)):
    try:
        emails = crud_get_sent_emails(username)
        if emails is None:
            return {"message": "No emails found"}
        else:
            return emails
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}"
        )

# Drafts
@router.get(
            "/drafts",
            description="Get all draft emails",
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
async def get_drafts(username = Depends(validate_token)):
    try:
        emails = crud_get_draft_emails(username)
        if emails is None:
            return {"message": "No emails found"}
        else:
            return emails
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}"
        )

# Save Draft
@router.post(
            "/save-draft",
            description="Save an email as a draft",
            status_code=status.HTTP_201_CREATED,
            responses={
                201: {
                    "description": "Email saved as draft"
                },
                400: {
                    "description": "Could not save email"
                },
                401: {
                    "description": "Could not validate credentials"
                }
            }
)
async def save_drafts(email: EmailSchema,username = Depends(validate_token)):
    try:
        success = crud_save_draft(email, username)
        if not success:
            raise HTTPException(status_code=400, detail="Could not save email")
        else:
            return {"message": "Email saved as draft"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}"
        )

