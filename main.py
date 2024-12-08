from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Crear las tablas de la base de datos automáticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas de la API

# Crear una nueva obra de arte
@app.post("/artworks/", response_model=schemas.ArtworkOut)
def create_artwork(artwork: schemas.ArtworkCreate, db: Session = Depends(get_db)):
    return crud.create_artwork(db=db, artwork=artwork)

# Obtener todas las obras de arte
@app.get("/artworks/", response_model=List[schemas.ArtworkOut])
def get_artworks(db: Session = Depends(get_db)):
    return crud.get_artworks(db=db)

# Obtener una obra de arte por ID
@app.get("/artworks/{artwork_id}", response_model=schemas.ArtworkOut)
def get_artwork(artwork_id: int, db: Session = Depends(get_db)):
    return crud.get_artwork(db=db, artwork_id=artwork_id)

# Actualizar una obra de arte
@app.put("/artworks/{artwork_id}", response_model=schemas.ArtworkOut)
def update_artwork(artwork_id: int, artwork: schemas.ArtworkCreate, db: Session = Depends(get_db)):
    return crud.update_artwork(db=db, artwork_id=artwork_id, artwork=artwork)

# Eliminar una obra de arte
@app.delete("/artworks/{artwork_id}", response_model=schemas.ArtworkOut)
def delete_artwork(artwork_id: int, db: Session = Depends(get_db)):
    return crud.delete_artwork(db=db, artwork_id=artwork_id)
