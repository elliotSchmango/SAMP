import jwt
import bcrypt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models import User
import os
from dotenv import load_dotenv
from database import SessionLocal
from sqlalchemy.orm import Session

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(username: str, password: str, db: Session = next(get_db())):
    user = db.query(User).filter(User.username == username).first()
    if not user or not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        return None
    return user

#create JWT token
def create_access_token(username: str, role: str):
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": username, "role": role, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

#get current user
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return User(username=username, role=role)  # lightweight model
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")