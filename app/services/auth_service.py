from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.models.users import User
from app.core.security import verify_password, create_access_token

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
            "hp": user.hp,
            "menu_klp": user.menu_klp,
        },
        "_user": user
    }