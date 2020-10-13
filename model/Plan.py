from sqlalchemy import Column, String, Float, Integer
from model.Base import Base


class Plan(Base):
    __tablename__ = 'plan'
    id = Column(Integer, primary_key=True)
    lp = Column(String, unique=True)
    easting = Column(Float)
    northing = Column(Float)
