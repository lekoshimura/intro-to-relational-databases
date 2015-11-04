# https://www.udacity.com/course/viewer#!/c-ud088/l-4325204629/m-4294324434

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    address = Column(String(250))
    city = Column(String(250))
    state = Column(String(250))
    zipCode = Column(String(5))
    website = Column(String(250))
    email = Column(String(250))

class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    dateOfBirth = Column(Date)
    breed = Column(String(250))
    gender = Column(String(8))
    picture = Column(String(250))
    weight = Column(Float(precision='2'))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)

class Profile(Base):
    id Column(Integer, primary_key = True)
    picture = Column(String(250))

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)

# Na linha de comando, digite:
# $ python ex01_db_setup
