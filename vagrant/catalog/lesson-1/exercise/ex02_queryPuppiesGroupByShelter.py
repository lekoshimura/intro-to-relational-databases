from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ex01_db_setup import Puppy, Shelter

engine = create_engine('sqlite:///puppyshelter.db')
session = sessionmaker(bind = engine)()

print '''
4. Query all puppies grouped by the shelter in which they are staying
'''
puppies = session.query(Puppy).order_by(Puppy.shelter_id)
for p in puppies:
    print str(p.id).rjust(3, '0') + ':' + p.name.rjust(10, ' ') + ' : ' + p.shelter.name
