from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
from models import User
from roles import require_role
from database import Base, engine
import models
from seed import seed_admin_user

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

#to protect the admin area
@app.get("/admin-area")
def admin_area(user: User = Depends(require_role("admin"))):
    return {"message": f"Welcome Admin {user.username}"}

@app.get("/observer-area")
def observer_area(user: User = Depends(require_role("observer"))):
    return {"message": f"Hello Observer {user.username}"}

#create db tables on startup
Base.metadata.create_all(bind=engine)

#call seed admin user
seed_admin_user()
