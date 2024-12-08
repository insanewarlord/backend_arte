from sqlalchemy.orm import Session
from . import models, schemas

# Crear una nueva obra de arte
def create_artwork(db: Session, artwork: schemas.ArtworkCreate):
    db_artwork = models.Artwork(
        title=artwork.title,
        artist=artwork.artist,
        description=artwork.description,
        price=artwork.price,
        image_url=artwork.image_url
    )
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork

# Obtener todas las obras de arte
def get_artworks(db: Session):
    return db.query(models.Artwork).all()

# Obtener una obra de arte por ID
def get_artwork(db: Session, artwork_id: int):
    return db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()

# Actualizar una obra de arte
def update_artwork(db: Session, artwork_id: int, artwork: schemas.ArtworkCreate):
    db_artwork = db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()
    if db_artwork:
        db_artwork.title = artwork.title
        db_artwork.artist = artwork.artist
        db_artwork.description = artwork.description
        db_artwork.price = artwork.price
        db_artwork.image_url = artwork.image_url
        db.commit()
        db.refresh(db_artwork)
        return db_artwork
    return None

# Eliminar una obra de arte
def delete_artwork(db: Session, artwork_id: int):
    db_artwork = db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()
    if db_artwork:
        db.delete(db_artwork)
        db.commit()
        return db_artwork
    return None
