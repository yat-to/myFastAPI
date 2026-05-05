from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.models import User
from app.schemas.user import UserLogin
from app.core.security import verify_password, create_access_token

def get_all_users(db: Session):
    return db.query(User).all()

def login_user(db: Session, credentials: UserLogin):
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Username Salah !!!")
    
    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Password Salah !!!")

    token = create_access_token({"sub": user.username, "name": user.nama})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "nama": user.nama,
            "email": user.email,
        }
    }