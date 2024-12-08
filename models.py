from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    description = Column(String)
    price = Column(Float)
    image_url = Column(String)
