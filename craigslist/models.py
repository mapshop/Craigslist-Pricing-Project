# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 18:55:53 2015

@author: Jay
"""

#models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()
# <--snip-->
class Apts(DeclarativeBase):
    __tablename__ = "lexington"
    
    craigId = Column('craigId', BigInteger, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    price = Column('price', Integer, nullable=True)
    #area = Column('area', String, nullable=True)
    beds = Column('beds', Integer, nullable=True)
    size = Column('size', Integer, nullable=True)
    date = Column('date', String, nullable=True)
    numPic = Column('numPic', Integer, nullable=True)
    postDate = Column('postDate', String, nullable=True)
    updateDate = Column('updateDate', String, nullable=True)
    reposts = Column('reposts', Integer, nullable=True)
    contentLen = Column('contentLen', Integer, nullable=True)
    baths = Column('baths', Float, nullable=True)
    latitude = Column('latitude', Float(Precision=8), nullable=True)
    longitude = Column('longitude', Float(Precision=8), nullable=True)
    zipcode = Column('zipcode', String, nullable=True)

def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)

def db_connect():
    return create_engine(URL(**settings.DATABASE))