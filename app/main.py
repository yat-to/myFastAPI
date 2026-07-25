from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user
from app.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTER
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Gaspol! Backend sudah jalan."}