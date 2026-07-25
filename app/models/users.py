from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Text)
    username = Column(String(20), primary_key=True, index=True)
    nama = Column(String(255), nullable=True)
    password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    hp = Column(String(15), nullable=True)
    menu_klp = Column(String(25), nullable=True)
    createdAt = Column(DateTime, nullable=True)
    editedAt = Column(DateTime, nullable=True)
    editedBy = Column(String(25), nullable=True)

    # relasi