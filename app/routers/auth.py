import json

from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.user import UserLogin
from app.schemas.auth import TokenResponse

from app.services.auth_service import login_user
from app.services.logs_service import save_log

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
def login(
    credentials: UserLogin,
    request: Request,
    db: Session = Depends(get_db)
):

    print("=" * 50)
    print("📥 LOGIN REQUEST")
    print(f"👤 Username : {credentials.username}")
    print("=" * 50)

    try:

        result = login_user(db, credentials)

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

        del result["_user"]

        return result

    except HTTPException as e:

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

        raise