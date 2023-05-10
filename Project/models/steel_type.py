from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SteelType(Base):
    __tablename__ = 'SteelType'
    id = Column(Integer, primary_key=True)
    steeltype = Column(Integer)
