#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import random
from random import randint
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
    price = Column(Float(2))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    @property
    def serialize(self):
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course
        }

if __name__ == '__main__':
    #Cria banco de dados
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)

    # Cria sessão
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Povoando table de restaurantes

    restaurant_names = ["Sujinho", "Yano", "Fifties", "Franboi", "La Capella"]

    for restaurant_name in restaurant_names:
        restaurant = Restaurant()
        restaurant.name = restaurant_name
        session.add(restaurant)

    # Povoando table de menus
    menu_name = [
        "Batata Frita",
        "Sorvete",
        "Peixe Assado",
        "Chorico",
        "Misto Quente",
        "Pastel de Queijo",
        "Pastel de Carne",
        "Pastel de Frango",
        "Pastel de Pizza",
        "Feijoada Completa",
        "Feijoada Light",
        "Torta de Frango",
        "Strogonoff",
        "Beef Tartar",
        "Tsukemono",
        "Sunomono",
        "Yakissoba",
        "Tempura",
        "Onigiri",
        "Almondegas",
        "Bolo de Carne",
        "Salada de Atum",
        "Alface",
        "Tomate",
        "Alfafa",
        "Ovo Frito",
        "Ovo Cozido",
        "Ovo com Bacon",
        "Ovo de Codorna",
        "Filet de Frango",
        "Anchova",
        "Filet de Maminha",
        "Filet de Alcatra",
        "Picanha",
        "Linguica Toscana",
        "Linguica de Frango",
        "Contra Filet",
        "Milho Assado",
        "Milho Cozido",
        "Pamonha",
        "Cural",
        "Kibe",
        "Coxiha",
        "Asa de Frango",
        "Camarao Frito",
        "Bobo de Camarao",
        "Camarao Cozido",
        "Camarao Assado",
        "Esfiha de Carne",
        "Esfiha de Queijo",
        "Suco de Laranja",
        "Suco de Limao",
        "Suco de Abacaxi",
        "Caldo de Cana",
        "Suco de Limao com Hortela",
        "Suco de Uva",
        "Refrigerante",
        "Cafe",
        "Cha",
        "Cha Verde",
        "Bife a Milanesa",
        "Frango a Milanesa",
        "Peixe a Milanesa",
    ];

    def CreateRandomPrice():
        return randint(5, 50);

    for i,x in enumerate(menu_name):
        new_menu_item = MenuItem()
        s_menu = random.choice(menu_name)
        new_menu_item.name = s_menu;
        new_menu_item.description = "Refeicao deliciosa feita de " + s_menu
        new_menu_item.price = CreateRandomPrice()
        new_menu_item.course = "comida"
        new_menu_item.restaurant_id = randint(1,5)
        session.add(new_menu_item)

    session.commit()
