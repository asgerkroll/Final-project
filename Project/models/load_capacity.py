from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LoadCapacity (Base):
    __tablename__ = 'LoadCapacity'
    id = Column(Integer, primary_key=True)
    load_capacity = Column(Float)
