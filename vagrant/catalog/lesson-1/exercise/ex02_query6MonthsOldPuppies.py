from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ex01_db_setup import Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')
session = sessionmaker(bind = engine)()

print '''
2. Query all of the puppies that are less than 6
months old organized by the youngest first
'''
six_months_ago = datetime.date.today() - datetime.timedelta(days = 30 * 6)

puppies = session.query(Puppy).filter(Puppy.dateOfBirth > six_months_ago)
for p in puppies:
    print str(p.id).rjust(3, '0') + ':' + p.name.rjust(10, ' ') + ' : ' + str(p.dateOfBirth)
