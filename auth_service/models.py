from pydantic import BaseModel
import bcrypt

class User(BaseModel):
    username: str
    role: str

#temp user db with "hashed" passwords
fake_users_db = {
    "admin_user": {
        "username": "admin_user",
        "role": "admin",
        "hashed_password": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
    },
    "observer_user": {
        "username": "observer_user",
        "role": "observer",
        "hashed_password": bcrypt.hashpw("observer123".encode(), bcrypt.gensalt()).decode()
    }
}