from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes import user

app = FastAPI()

# Main route
@app.get("/")
def get():
    return HTMLResponse("""
    <html>
        <body>
            <h1>Welcome to the chat server!</h1>
        </body>
    </html>
    """)

app.include_router(user.router, prefix="/users", tags=["Users"])


