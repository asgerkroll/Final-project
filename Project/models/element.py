import string
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from dimension import Dimension
from random import choices

Base = declarative_base()

class ElementId(Base):
    __tablename__ = 'ElementId'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    dimension_id = Column(Integer, ForeignKey('Dimensions.id'))

    dimension = relationship(Dimension)

    def size(self):
        return self.dimension.size

    def SKU(self):
        code = ''.join(choices(string.ascii_letters + string.digits, k=4))
        return f"{self.type}-{self.size:.2f}-{code}"
