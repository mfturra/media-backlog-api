# coding: utf-8
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Videogame(Base):
    __tablename__ = 'videogames'

    videogame_id = Column(Integer, primary_key=True)
    videogame_title = Column(String(30), nullable=False)
    videogame_platform = Column(String(30), nullable=False)
    videogame_releasedate = Column(Date)
    videogame_publisher = Column(String(30))
