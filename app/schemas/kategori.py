from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class KategoriResponse(BaseModel):
    id: str
    uraian: str
    createdAt: datetime

    class Config:
        from_attributes = True

class KategoriRequest(BaseModel):
    data_ke: int = 1
    cari_value: Optional[str] = ""

class KategoriCreate(BaseModel):
    uraian: str

class KategoriUpdate(BaseModel):
    uraian: str