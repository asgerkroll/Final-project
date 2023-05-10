from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dimension(Base):
    __tablename__ = 'Dimensions'
    id = Column(Integer, primary_key=True)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)
