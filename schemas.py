from pydantic import BaseModel

class ArtworkCreate(BaseModel):
    title: str
    artist: str
    description: str
    price: float
    image_url: str

class ArtworkOut(ArtworkCreate):
    id: int

    class Config:
        orm_mode = True
