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

    # Povoando table de restaurantes

    restaurant_names = ["Sujinho", "Yano", "Fifties", "Franboi", "La Capella"]

    for restaurant_name in restaurant_names:
        print restaurant_name
        restaurant = Restaurant()
        restaurant.name = restaurant_name
        session.add(restaurant)

    # Povoando table de menus
    menu_name = [
        "Batata Frita",
        "Sorvete",
        "Peixe Assado",
        "Choriço",
        "Misto Quente",
        "Pastel de Queijo",
        "Pastel de Carne",
        "Pastel de Frango",
        "Pastel de Pizza",
        "Feijoada Completa",
        "Feijoada Light",
        "Torta de Frango",
        "Stroganoff",
        "Beef Tartar",
        "Tsukemono",
        "Sunomono",
        "Yakissoba",
        "Tempura",
        "Onigiri",
        "Almôndegas",
        "Bolo de Carne",
        "Salada de Atum",
        "Alface",
        "Tomate",
        "Alfafa",
        "Ovo Frito",
        "Ovo Cozido",
        "Ovo com Bacon",
        "Ovo de Codorna",
        "Filé de Frango",
        "Anchova",
        "Filé de Maminha",
        "Filé de Alcatra",
        "Picanha",
        "Linguiça",
        "Contra Filé",
        "Milho Assado",
        "Milho Cozido",
        "Pamonha",
        "Cural",
        "Kibe",
        "Coxiha",
        "Asa de Frango",
        "Camarão Frito",
        "Bobó de Camarão",
        "Camarão Cozido",
        "Camarão Assado",
        "Esfiha de Carne",
        "Esfiha de Queijo",
        "Suco de Laranja",
        "Suco de Limão",
        "Suco de Abacaxi",
        "Caldo de Cana",
        "Suco de Limão com Hortelã",
        "Suco de Uva",
        "Refrigerante",
        "Café",
        "Chá",
        "Chá Verde"
    ];

    def CreateRandomPrice():
        return randint(5, 50);

    for i,x in enumerate(menu_name):
        s_menu = random.choice(menu_name);
        new_menu_item = MenuItem (
            name = s_menu,
            description = "Refeição deliciosa feita de " + s_menu,
            price = CreateRandomPrice(),
            course = "comida, né?",
            restaurant = random.choice(restaurant_names)
        );
        session.add(new_menu_item)

    session.commit()
