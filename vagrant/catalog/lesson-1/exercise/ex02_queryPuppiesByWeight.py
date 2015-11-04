from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ex01_db_setup import Puppy

engine = create_engine('sqlite:///puppyshelter.db')
session = sessionmaker(bind = engine)()

print '''
3. Query all puppies by ascending weight
'''

puppies = session.query(Puppy).order_by(Puppy.weight)
for p in puppies:
    print str(p.id).rjust(3, '0') + ':' + p.name.rjust(10, ' ') + ' : ' + str(p.weight)
