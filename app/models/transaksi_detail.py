from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid

def generate_id():
    return str(uuid.uuid4())

class TransaksiDetail(Base):
    __tablename__ = "transaksi_detail"

    id = Column(String(36), primary_key=True, default=generate_id)

    transaksi_id = Column(String(36), ForeignKey("transaksi.id"))
    menu_id = Column(String(36), ForeignKey("menu.id"))

    nama_menu_snapshot = Column(String(150), nullable=False)
    harga = Column(Integer, nullable=False)
    qty = Column(Integer, nullable=False)
    subtotal = Column(Integer, nullable=False)

    # relasi
    transaksi = relationship("Transaksi", back_populates="detail")
    menu = relationship("Menu", back_populates="transaksi_detail")