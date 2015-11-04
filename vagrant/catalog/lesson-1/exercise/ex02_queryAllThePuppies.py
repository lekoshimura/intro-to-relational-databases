from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ex01_db_setup import Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
# DBSession = sessionmaker(bind = engine)
# session = DBSession()
session = sessionmaker(bind = engine)()

print '''
1 . Query all of the puppies and return the results
in ascending alphabetical order
'''

puppies = session.query(Puppy).order_by(Puppy.name).all()
for p in puppies:
    print str(p.id).rjust(3, '0') + ':' + p.name
