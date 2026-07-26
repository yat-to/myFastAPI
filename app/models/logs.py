from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, String, Text, DateTime, JSON

from app.db.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(String(20), primary_key=True)

    user_id = Column(String(20), nullable=True)
    username = Column(String(100), nullable=True)
    nama = Column(String(150), nullable=True)

    action = Column(String(30), nullable=False)
    module = Column(String(100), nullable=False)

    description = Column(Text, nullable=True)

    method = Column(String(10), nullable=True)
    endpoint = Column(String(255), nullable=True)

    old_data = Column(JSON, nullable=True)
    new_data = Column(JSON, nullable=True)

    ip_address = Column(String(50), nullable=True)
    user_agent = Column(Text, nullable=True)

    status = Column(String(20), default="SUCCESS")

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(ZoneInfo("Asia/Makassar"))
    )