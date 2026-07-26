from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    nama: Optional[str] = None
    email: str
    hp: Optional[str] = None
    menu_klp: Optional[str] = None

    class Config:
        from_attributes = True