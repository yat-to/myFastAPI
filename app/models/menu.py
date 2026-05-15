from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime
import uuid

def generate_id():
    return str(uuid.uuid4())

class Menu(Base):
    __tablename__ = "menu"

    id = Column(String(36), primary_key=True, default=generate_id)
    nama_menu = Column(String(150), nullable=False)
    harga = Column(Integer, nullable=False)
    kategori_id = Column(String(36), ForeignKey("kategori.id"))
    status = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.utcnow)

    # relasi
    kategori = relationship("Kategori", back_populates="menu")
    transaksi_detail = relationship("TransaksiDetail", back_populates="menu")