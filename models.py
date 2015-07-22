import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    username = Column(String(32), nullable=False)
    password = Column(String(256), nullable=False)
