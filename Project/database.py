from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for models
Base = declarative_base()

# Import models here to avoid circular import issues
from models.dimension import Dimension
from models.element import ElementId
from models.concrete_type import ConcreteType
from models.element_type import ElementType
from models.steel_type import SteelType
from models.load_capacity import LoadCapacity
from models.attachment import FileAttachment

# Set up the engine
engine = create_engine('sqlite:///con_element_db.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

def setup_database():
    # Create tables for all models
    Base.metadata.create_all(engine)
