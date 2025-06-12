from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Temporary placeholder logic
    return {
        "username": form_data.username,
        "message": "Login endpoint hit successfully"
    }

@app.get("/")
def root():
    return {"message": "Auth service is up"}