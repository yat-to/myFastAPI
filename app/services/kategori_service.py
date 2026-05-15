import math
import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.kategori import Kategori
from app.schemas.kategori import KategoriCreate, KategoriUpdate

def getKategori(db: Session, page: int, search: str):
    data_batas = 10
    data_start = (page - 1) * data_batas
    
    # 1. query dasar dengan filter pencarian
    query = db.query(Kategori)
    if search:
        query = query.filter(Kategori.uraian.ilike(f"%{search}%"))

    # 2. menghitung total data
    total_data = query.count()

    # 3. menghitung jumlah halaman
    total_halaman = math.ceil(total_data / data_batas)
    if total_halaman < 1:
        total_halaman = 1

    #  4. ambil data dengan limit & offset
    results= query.order_by(Kategori.uraian.asc()) \
                  .offset(data_start) \
                  .limit(data_batas) \
                  .all()
    
    return{
        "data": results,
        "jml_data": total_halaman
    }

def addData(db: Session, kategori: KategoriCreate):
    print(f"DEBUG LOG: Data diterima -> {kategori.model_dump()}")

    db_kategori = Kategori(uraian=kategori.uraian)
    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)
    return db_kategori

def get_kategori_by_id(db: Session, kategori_id: str):
    return db.query(Kategori).filter(Kategori.id == kategori_id).first()

def editData(db: Session, kategori_id: str, kategori: KategoriUpdate):
    db_kategori = db.query(Kategori).filter(Kategori.id == kategori_id).first()
    if db_kategori:
        db_kategori.uraian = kategori.uraian
        db.commit()
        db.refresh(db_kategori)
    return db_kategori

def removeData(db: Session, kategori_id: str):
    db_kategori = db.query(Kategori).filter(Kategori.id == kategori_id).first()
    if db_kategori:
        db.delete(db_kategori)
        db.commit()
        return True
    return False