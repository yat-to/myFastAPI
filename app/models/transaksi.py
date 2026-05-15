from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime
import uuid

def generate_id():
    return str(uuid.uuid4())

class Transaksi(Base):
    __tablename__ = "transaksi"

    id = Column(String(36), primary_key=True, default=generate_id)
    kode_transaksi = Column(String(50), nullable=False)

    total = Column(Integer, nullable=False)
    bayar = Column(Integer, nullable=False)
    kembalian = Column(Integer, nullable=False)

    metode_bayar = Column(String(20))
    jenis_order = Column(String(20))

    user_id = Column(String(20), ForeignKey("users.username"))
    createdAt = Column(DateTime, default=datetime.utcnow)

    # relasi
    user = relationship("User", back_populates="transaksi")
    detail = relationship(
        "TransaksiDetail",
        back_populates="transaksi",
        cascade="all, delete"
    )