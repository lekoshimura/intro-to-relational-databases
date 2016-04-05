#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppy import Base, Puppy, Shelter, PuppyProfile, Adopter, PuppyAdopter

from datetime import datetime

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puppy/list')
def puppyList():
    puppies = session.query(Puppy).all()
    return render_template('puppy-list.html', puppies = puppies)
    
@app.route('/puppy/view/<int:puppy_id>')
def puppyView(puppy_id):
    puppy = session.query(Puppy).get(puppy_id)
    return render_template('puppy-view.html', puppy = puppy)

@app.route('/puppy/create', methods = ['GET', 'POST'])
def puppyCreate():
    if request.method == 'POST':
        puppy = Puppy(
            name = request.form['name'], 
            dateOfBirth = datetime.strptime(request.form['dateOfBirth'], '%Y-%m-%d'),
            breed = request.form['breed'],
            gender = request.form['gender'],
            weight = request.form['weight']
        )
        session.add(puppy)
        session.commit()
        flash('New puppy created')
        return redirect(url_for('puppyView', puppy_id = puppy.id))
    else:
        return render_template('puppy-create.html');

@app.route('/puppy/edit/<int:puppy_id>', methods = ['GET', 'POST'])
def puppyEdit(puppy_id):
    if request.method == 'POST':
        puppy = session.query(Puppy).get(puppy_id);
        puppy.name = request.form['name'];
        puppy.dateOfBirth = datetime.strptime(request.form['dateOfBirth'], '%Y-%m-%d');
        puppy.breed = request.form['breed'];
        puppy.gender = request.form['gender'];
        puppy.weight = request.form['weight'];
        session.commit();
        flash('Puppy edited');
        return redirect(url_for('puppyView', puppy_id = puppy.id))
    else:
        puppy = session.query(Puppy).get(puppy_id);
        return render_template('puppy-edit.html', puppy = puppy)

@app.route('/puppy/delete/<int:puppy_id>', methods = ['GET', 'POST'])
def puppyDelete(puppy_id):
    if request.method == 'POST':
        puppy = session.query(Puppy).get(puppy_id)
        session.delete(puppy);
        session.commit();
        flash('Puppy deleted');
        return redirect(url_for('puppyList'))
    else:
        puppy = session.query(Puppy).get(puppy_id)
        return render_template('puppy-delete.html', puppy = puppy)
    
        
        
@app.route('/shelter/list')
def shelterList():
    shelters = session.query(Shelter).all()
    return render_template('shelter-list.html', shelters = shelters)
    
@app.route('/shelter/view/<int:shelter_id>')
def shelterView(shelter_id):
    shelter = session.query(Shelter).get(shelter_id)
    return render_template('shelter-view.html', shelter = shelter)

@app.route('/shelter/create', methods = ['GET', 'POST'])    
def shelterCreate():
    if request.method == 'POST':
        shelter = Shelter(
            name = request.form['name'],
            address = request.form['address'],
            city = request.form['city'],
            state = request.form['state'],
            zipCode = request.form['zipCode'],
            website = request.form['website'],
            email = request.form['email'],
            maximumCapacity = request.form['maximumCapacity']
        );
        session.add(shelter);
        session.commit();
        flash('New shelter created');
        return redirect(url_for('shelterView', shelter_id = shelter.id))
    else:
        return render_template('shelter-create.html');

@app.route('/shelter/edit/<int:shelter_id>', methods = ['GET', 'POST'])
def shelterEdit(shelter_id):
    if request.method == 'POST':
        shelter = session.query(Shelter).get(shelter_id);
        shelter.name = request.form['name'];
        shelter.address = request.form['address'];
        shelter.city = request.form['city'];
        shelter.state = request.form['state'];
        shelter.zipCode = request.form['zipCode'];
        shelter.website = request.form['website'];
        shelter.email = request.form['email'];
        shelter.maximumCapacity = request.form['maximumCapacity'];
        session.commit();
        flash('Shelter edited')
        return redirect(url_for('shelterView', shelter_id = shelter.id))
    else:
        shelter = session.query(Shelter).get(shelter_id);
        return render_template('shelter-edit.html', shelter = shelter)

@app.route('/shelter/delete/<int:shelter_id>', methods = ['GET', 'POST'])
def shelterDelete(shelter_id):
    if request.method == 'POST':
        shelter = session.query(Shelter).get(shelter_id);
        session.delete(shelter);
        session.commit();
        flash('Shelter deleted');
        return redirect(url_for('shelterList'))
    else:
        shelter = session.query(Shelter).get(shelter_id);
        return render_template('shelter-delete.html', shelter = shelter)
            
    

@app.route('/adopter/list')
def adopterList():
    adopters = session.query(Adopter).all()
    return render_template('adopter-list.html', adopters = adopters)

@app.route('/adopter/view/<int:adopter_id>')
def adopterView(adopter_id):
    adopter = session.query(Adopter).get(adopter_id);
    return render_template('adopter-view.html', adopter = adopter)

@app.route('/adopter/create', methods = ['GET', 'POST'])
def adopterCreate():
    if request.method == 'POST':
        adopter = Adopter(
            name = request.form['name']
        );
        session.add(adopter);
        session.commit();
        flash('New adopter created');
        return redirect(url_for('adopterView', adopter_id = adopter.id))
    else:
        return render_template('adopter-create.html')

@app.route('/adopter/edit/<int:adopter_id>', methods = ['GET', 'POST'])
def adopterEdit(adopter_id):
    if request.method == 'POST':
        adopter = session.query(Adopter).get(adopter_id);
        adopter.name = request.form['name'];
        session.commit();
        flash('Adopter edited')
        return redirect(url_for('adopterView', adopter_id = adopter.id))
    else:
        adopter = session.query(Adopter).get(adopter_id);
        return render_template('adopter-edit.html', adopter = adopter)
        
@app.route('/adopter/delete/<int:adopter_id>', methods = ['GET', 'POST'])
def adopterDelete(adopter_id):
    if request.method == 'POST':
        adopter = session.query(Adopter).get(adopter_id);
        session.delete(adopter);
        session.commit();
        flash('Adopter deleted');
        return redirect(url_for('adopterList'))
    else:
        adopter = session.query(Adopter).get(adopter_id);
        return render_template('adopter-delete.html', adopter = adopter)

@app.route('/adopter/<int:adopter_id>/puppies')
def puppiesByAdopter(adopter_id):
    puppies = session.query(PuppyAdopter).filter_by(adopter_id = adopter_id).all()
    adopter = session.query(Adopter).get(adopter_id)
    return render_template('puppies-by-adopter.html', adopter = adopter, puppies = puppies)



# http://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session
# Note to Heroku [|c0.io] users ending up here: I did not get the example here 
# to work until I moved app.secret_key = ... out of the if block – which in 
# hindsight makes sense since Heroku runs the app via gunicorn, which means the 
# if __name__ == "__main__": block is never entered.
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
