#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

if __name__ == '__main__':
    #Cria banco de dados
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
    
    # Cria sessão
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    # Povoando dados
    
    restaurant_names = ["Sujinho", "Yano", "Fifties", "Franboi", "La Capella"]
    
    for restaurant_name in restaurant_names:
        print restaurant_name
        restaurant = Restaurant()
        restaurant.name = restaurant_name
        session.add(restaurant)
    
    session.commit()