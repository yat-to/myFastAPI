from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings 

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Taruh get_db di sini agar bisa dipakai di mana saja (Reusable)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()