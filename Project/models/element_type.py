from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ElementType (Base):
    __tablename__ = 'ElementType'
    id = Column(Integer, primary_key=True)
    type = Column(String)
