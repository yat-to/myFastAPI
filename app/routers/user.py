import json

from pprint import pprint

from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserResponse, UserLogin, TokenResponse
from app.services import user_service
from app.services.logs_service import save_log

router = APIRouter(tags=["users"])

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

# ── Auth ───────────────────────────────────────────
@router.post("/auth/login", response_model=TokenResponse)
def login(
    credentials: UserLogin,
    request: Request,
    db: Session = Depends(get_db)
):
    print("=" * 40)
    print(f"📥 LOGIN REQUEST MASUK")
    print(f"👤 Username : {credentials.username}")
    print(f"🔑 Password : {credentials.password}")
    print("=" * 40)

    try:

        result = user_service.login_user(db, credentials)

        # Simpan log login berhasil
        save_log(
            db=db,
            user=result["_user"],
            action="LOGIN",
            module="Authentication",
            description="Login berhasil",
            request=request,
            status="SUCCESS"
        )

        print("✅ LOGIN BERHASIL")
        print(json.dumps(result["user"], indent=4, ensure_ascii=False))
        print("=" * 50)

        del result["_user"]

        return result

    # result =  user_service.login_user(db, credentials)

    # print(f"✅ LOGIN BERHASIL :")
    # pprint(result, sort_dicts=False)
    # print("=" * 40)

    # return result

    except HTTPException as e:

        # Simpan log login gagal
        save_log(
            db=db,
            username=credentials.username,
            action="LOGIN",
            module="Authentication",
            description=e.detail,
            request=request,
            status="FAILED"
        )

        print("❌ LOGIN GAGAL")
        print(e.detail)
        print("=" * 50)

        raise