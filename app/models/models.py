from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base

class Berita(Base):
    __tablename__ = "berita"

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String(255))
    isi = Column(Text)
    gambar = Column(String(255))
    created_at = Column(DateTime)