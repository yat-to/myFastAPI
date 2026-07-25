from pprint import pprint

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserResponse, UserLogin, TokenResponse
from app.services import user_service

router = APIRouter(tags=["users"])

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

# ── Auth ───────────────────────────────────────────
@router.post("/auth/login", response_model=TokenResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    print("=" * 40)
    print(f"📥 LOGIN REQUEST MASUK")
    print(f"👤 Username : {credentials.username}")
    print(f"🔑 Password : {credentials.password}")
    print("=" * 40)

    result =  user_service.login_user(db, credentials)

    print(f"✅ LOGIN BERHASIL :")
    pprint(result, sort_dicts=False)
    print("=" * 40)

    return result