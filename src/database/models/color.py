from sqlalchemy import Column, Integer, String, DateTime, func
from src.db.database import db

class Color(db.Model):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, index=True)
    color_name = Column(String(50), nullable=False)
    red = Column(Integer, nullable=False)
    green = Column(Integer, nullable=False)
    blue = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
