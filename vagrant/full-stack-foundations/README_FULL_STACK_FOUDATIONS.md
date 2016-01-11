# Full Stack Foundations

# Procedimentos

## Máquina Virtual Vagrant

* [Home do Vagrant](https://www.vagrantup.com/)
* [Intruções de instalação da VM Vagrant]( https://www.udacity.com/wiki/ud197/install-vagrant)
* _If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site_
* Obs: a vm já foi instalada para o curso _Intro to Relational Database_ e, por isso, os fontes estão no diretório ```[home]/intro-to-relational-databases/```
* Para iniciar a VM:
```bash
local$ cd [home]/intro-to-relational-databases/fullstack/vagrant/
local$ vagrant up
local$ vagrant ssh
```

## SQLite
```bash
# Instalação do console
$ sudo apt-get install sqlite3

# Console
$ sqlite [path_do_banco]

# DDL de todas as tabelas
sqlite>.dump
# DDL de uma tabela
sqlite>.dump [nome da tabela]
```


# SQLAlchemy

## Database Configuration

__/lesson-1/database_setup.py__

```python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
```
----------
```bash
# Iniciar a VM Vagrant  
# Executar o comando python abaixo para criar o banco de dados
$ cd /vagrant/catalog/lesson-1
$ python database_setup.py
```

## Povoando Banco de Dados Através do Console Python e SQLAlchemy

```python
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker
# Importar as classes do projeto. Estão no diretório /catalog/lesson_1
>>> from database_setup import Base, Restaurant, MenuItem
# Qual banco?
>>> engine = create_engine('sqlite:///restaurantmenu.db')
# Tem que ligar as classes à banco
>>> Base.metadata.bind = engine
# e instanciar o objeto session (responsável pelas transações)
>>> DBSession = sessionmaker(bind = engine)
>>> session = DBSession()
# Inserindo um resgistros
>>> myFistRestaurant = Restaurant(name = "Pizza Palace")
>>> session.add(myFistRestaurant)
>>> session.commit()
```

## Consultando Através do Console Python e SQLAlchemy
```python
>>> restaurant = session.query(Restaurant).all()
>>> restaurant[0].name
"Pizza Palace"
# ou
>>> restaurant = session.query(Restaurant).first()
>>> restaurant.name
# ou
>>> veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
>>> for v in veggieBurgers:
...    print v.id
...    print v.name
...    print v.price
...    print v.restaurant.name
...    print '-' * 10
...
```
## Atualizando
```python
b = session.query(MenuItem).filter_by(id = 10).one()
b.price = '$2.99'
session.add(b)
session.commit()
```

## Deletando
```python
>>> spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
>>> spinach.restaurant.name
u"Auntie Ann's Diner' "
>>> session.delete(spinach)
>>> session.commit()
```

# Flask


# Referências
* [Solution Code to Full Stack Foundations (ud088)](https://github.com/lobrown/Full-Stack-Foundations)
* [Vagrant](https://www.vagrantup.com/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
