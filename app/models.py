from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base


# create table library
class Library(Base):
    __tablename__ = 'library'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    in_stock = Column(Boolean)
