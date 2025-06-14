from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
import bcrypt


def seed_admin_user():
    db: Session = SessionLocal()

    #checking if admin_user exists
    user = db.query(User).filter(User.username == "admin_user").first()
    #if not
    if not user:
        print("Creating default admin_user...")
        hashed = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
        new_user = User(username="admin_user", hashed_password=hashed, role="admin")
        db.add(new_user)
        db.commit()
        print("admin_user created")
    else:
        print("admin_user already exists")

    db.close()