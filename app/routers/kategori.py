from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.kategori import KategoriResponse, KategoriRequest, KategoriCreate, KategoriUpdate
from app.services import kategori_service

router = APIRouter(tags=["kategori"])

@router.post("/kategori/view")
def read_kategori(params: KategoriRequest, db: Session = Depends(get_db)):
    return kategori_service.getKategori(
        db,
        page = params.data_ke,
        search = params.cari_value
    )

@router.post("/kategori/addData", response_model=KategoriResponse)
def addData(kategori: KategoriCreate, db: Session = Depends(get_db)):
    return kategori_service.addData(db, kategori)

@router.put("/kategori/{id}", response_model=KategoriResponse)
def editData(id: str, kategori: KategoriUpdate, db: Session = Depends(get_db)):
    db_kategori = kategori_service.editData(db, id, kategori)
    if db_kategori is None:
        raise HTTPException(status_code=404, detail="Kategori tidak ditemukan")
    return db_kategori

@router.delete("/kategori/{id}")
def removeData(id: str, db: Session = Depends(get_db)):
    success = kategori_service.removeData(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Kategori tidak ditemukan")
    return {"message": "Kategori berhasil dihapus"}