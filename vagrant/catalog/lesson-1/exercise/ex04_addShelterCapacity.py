#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from random import randint
import datetime
import random
from sqlalchemy.sql import func

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
    maximumCapacity = Column(Integer)
    currentOccupancy = Column(Integer)

class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    dateOfBirth = Column(Date)
    breed = Column(String(250))
    gender = Column(String(8))
    weight = Column(Float(precision='2'))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    profile = relationship("PuppyProfile", uselist=False, backref="Puppy")

class PuppyProfile(Base):
    __tablename__ = 'puppy_profile'
    id = Column(Integer, primary_key = True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship(Puppy)
    picture_url = Column(String(250))
    description = Column(String(250))
    special_needs = Column(String(250))

class Adopter(Base):
    __tablename__ = 'adopter'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))

class PuppyAdopter(Base):
    __tablename__ = 'puppy_adopter'
    adopter_id = Column(Integer, ForeignKey('adopter.id'), primary_key = True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'), primary_key = True)
    adopter = relationship(Adopter)
    puppy = relationship(Puppy)

engine = create_engine('sqlite:///puppyshelter_ex04_shelterCapacity.db')
Base.metadata.create_all(engine)

# povoa as tabelas

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Add Shelters

maximumCapacity = randint(10,15)
shelter1 = Shelter(
    name = "Oakland Animal Services",
    address = "1101 29th Ave",
    city = "Oakland",
    state = "California",
    zipCode = "94601",
    website = "oaklandanimalservices.org",
    maximumCapacity = maximumCapacity,
    currentOccupancy = maximumCapacity - randint(1,5)
    )
session.add(shelter1)

maximumCapacity = randint(10,15)
shelter2 = Shelter(
    name = "San Francisco SPCA Mission Adoption Center",
    address="250 Florida St",
    city="San Francisco",
    state="California",
    zipCode = "94103",
    website = "sfspca.org",
    maximumCapacity = maximumCapacity,
    currentOccupancy = maximumCapacity - randint(1,5)
    )
session.add(shelter2)

maximumCapacity = randint(10,15)
shelter3 = Shelter(
    name = "Wonder Dog Rescue",
    address= "2926 16th Street",
    city = "San Francisco",
    state = "California",
    zipCode = "94103",
    website = "http://wonderdogrescue.org",
    maximumCapacity = maximumCapacity,
    currentOccupancy = maximumCapacity - randint(1,5)
    )
session.add(shelter3)

maximumCapacity = randint(10,15)
shelter4 = Shelter(
    name = "Humane Society of Alameda",
    address = "PO Box 1571",
    city = "Alameda",
    state = "California",
    zipCode = "94501",
    website = "hsalameda.org",
    maximumCapacity = maximumCapacity,
    currentOccupancy = maximumCapacity - randint(1,5)
    )
session.add(shelter4)

maximumCapacity = randint(10,15)
shelter5 = Shelter(
    name = "Palo Alto Humane Society",
    address = "1149 Chestnut St.",
    city = "Menlo Park",
    state = "California",
    zipCode = "94025",
    website = "paloaltohumane.org",
    maximumCapacity = maximumCapacity,
    currentOccupancy = maximumCapacity - randint(1,5)
    )
session.add(shelter5)

# Add Puppies
male_names = ["Bailey", "Max", "Charlie", "Buddy","Rocky","Jake", "Jack", "Toby", "Cody", "Buster", "Duke", "Cooper", "Riley", "Harley", "Bear", "Tucker", "Murphy", "Lucky", "Oliver", "Sam", "Oscar", "Teddy", "Winston", "Sammy", "Rusty", "Shadow", "Gizmo", "Bentley", "Zeus", "Jackson", "Baxter", "Bandit", "Gus", "Samson", "Milo", "Rudy", "Louie", "Hunter", "Casey", "Rocco", "Sparky", "Joey", "Bruno", "Beau", "Dakota", "Maximus", "Romeo", "Boomer", "Luke", "Henry"]
female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby', 'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess','Emma', 'Annie', 'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 'Madison', 'Stella', 'Penny', 'Belle', 'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']
puppy_images = ["http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct", "http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct","http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct","http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct","http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg","http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct","http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct","http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct","http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct","http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"]
puppy_needs = ["passear 3 vezes por dia", "tomar remedios", "evitar gluten"]
puppy_description = ["carinhoso", "fiel", "companheiro", "gosta de brincar"]

# Add adopters
adopters = ["Leonardo Eiji Koshimura", "Cristiane de Borba", "Helio Seiji Koshimura"]

# This method will make a random age for each puppy between 0-18 months(approx.)
# old from the day the algorithm was run.
def CreateRandomAge():
    today = datetime.date.today()
    days_old = randint(0,540)
    birthday = today - datetime.timedelta(days = days_old)
    return birthday

# This method will create a random weight between 1.0-40.0 pounds (or whatever
# unit of measure you prefer)
def CreateRandomWeight():
    return random.uniform(1.0, 40.0)

for i,x in enumerate(male_names):
    new_puppy = Puppy(
        name = x,
        gender = "male",
        dateOfBirth = CreateRandomAge(),
        shelter_id = randint(1,5),
        weight = CreateRandomWeight()
    )
    new_profile = PuppyProfile(
        puppy = new_puppy,
        picture_url = random.choice(puppy_images),
        description = new_puppy.name + ' ' + random.choice(puppy_description),
        special_needs = new_puppy.name + ' ' + random.choice(puppy_needs)
    )
    session.add(new_puppy)
    session.add(new_profile)
    session.commit()

for i,x in enumerate(female_names):
    new_puppy = Puppy(
        name = x,
        gender = "female",
        dateOfBirth = CreateRandomAge(),
        shelter_id = randint(1,5),
        weight = CreateRandomWeight()
    )
    new_profile = PuppyProfile(
        puppy = new_puppy,
        picture_url = random.choice(puppy_images),
        description = new_puppy.name + ' ' + random.choice(puppy_description),
        special_needs = new_puppy.name + ' ' + random.choice(puppy_needs)
    )
    session.add(new_puppy)
    session.add(new_profile)
    session.commit()

for i,x in enumerate(adopters):
    new_adopter = Adopter(
        name = x
    )
    session.add(new_adopter)
    session.commit()

qry = session.query(
    func.max(Adopter.id).label('adopter_max_id'),
    func.min(Adopter.id).label('adopter_min_id')
)
res = qry.one()
adopter_max_id = res.adopter_max_id
adopter_min_id = res.adopter_min_id

qry = session.query(
    func.max(Puppy.id).label('puppy_max_id'),
    func.min(Puppy.id).label('puppy_min_id')
)
res = qry.one()
puppy_max_id = res.puppy_max_id
puppy_min_id = res.puppy_min_id

for i in range(adopter_min_id, adopter_max_id + 1):
    print '-' * 10
    print 'i:' + str(i)
    num_puppies = randint(5,8)
    for j in range(1, num_puppies):
        print 'j:' + str(j)
        new_adoption = PuppyAdopter(
            adopter_id = i,
            puppy_id = randint(puppy_min_id, puppy_max_id)
        )
        session.add(new_adoption)
        session.commit()

adoptions = session.query(PuppyAdopter).all()
for a in adoptions:
    print str(a.adopter_id).rjust(3, '0') + ' - ' + a.adopter.name.ljust(25, ' ') + ': ' + str(a.puppy_id).rjust(3, '0') + ' - ' + a.puppy.name

