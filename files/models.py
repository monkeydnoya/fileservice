from database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship


class FileSave(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True,unique=True,autoincrement=True)
    eventid = Column(Integer, unique=True)
    filename = Column(String, unique=True)
    link = Column(String, unique=True)