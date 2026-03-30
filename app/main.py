from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.database import SessionLocal
from models.models import Berita

from db.database import engine

print(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Da jalan ini barang pis !!!"}

@app.get("/berita")
def get_berita(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM berita LIMIT 5"))
    data = [dict(row._mapping) for row in result]
    return data