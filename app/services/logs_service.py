from datetime import datetime
from zoneinfo import ZoneInfo

import uuid

from sqlalchemy.orm import Session

from app.models.logs import Log


def save_log(
    db: Session,
    action,
    module,
    description,
    request=None,
    user=None,
    username=None,
    status="SUCCESS",
    old_data=None,
    new_data=None,
):
    try:
        log = Log(
            id=str(uuid.uuid4())[:20],

            user_id=getattr(user, "id", None),
            username=getattr(user, "username", username),
            nama=getattr(user, "nama", None),

            action=action,
            module=module,
            description=description,

            method=request.method if request else None,
            endpoint=str(request.url.path) if request else None,

            old_data=old_data,
            new_data=new_data,

            ip_address=request.client.host if request else None,
            user_agent=request.headers.get("user-agent") if request else None,

            status=status,
        )
        
        db.add(log)
        db.commit()
        
    except Exception as e:
        db.rollback()
        print(f"❌ Gagal menyimpan log : {e}")