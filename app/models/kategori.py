from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime
import uuid

def generate_id():
    return str(uuid.uuid4())

class Kategori(Base):
    __tablename__ = "kategori"

    id = Column(String(36), primary_key=True, default=generate_id)
    uraian = Column(String(100), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)

    # relasi
    menu = relationship("Menu", back_populates="kategori")