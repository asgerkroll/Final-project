from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConcreteType(Base):
    __tablename__ = 'ConcreteType'
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    label = Column(String)
