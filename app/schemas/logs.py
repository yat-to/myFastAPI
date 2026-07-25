from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LogBase(BaseModel):
    user_id: Optional[str] = None
    username: Optional[str] = None
    nama: Optional[str] = None

    action: str
    module: str

    description: Optional[str] = None

    method: Optional[str] = None
    endpoint: Optional[str] = None

    old_data: Optional[Any] = None
    new_data: Optional[Any] = None

    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

    status: Optional[str] = "SUCCESS"


class LogCreate(LogBase):
    pass


class LogResponse(LogBase):
    id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)