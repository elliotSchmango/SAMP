from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
from models import User

app = FastAPI()


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(user.username, user.role)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/profile")
def profile(user: User = Depends(get_current_user)):
    return {"username": user.username, "role": user.role}


@app.get("/")
def root():
    return {"message": "Auth service is up"}
