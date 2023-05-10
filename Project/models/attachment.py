from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FileAttachment(Base):
    __tablename__ = 'FileAttachments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(LargeBinary)
