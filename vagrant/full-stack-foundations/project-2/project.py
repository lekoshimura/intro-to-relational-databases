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
        sDateOfBirth = datetime.strptime(request.form['dateOfBirth'], '%d/%m/%Y')
        puppy = Puppy(
            name = request.form['name'], 
            dateOfBirth = sDateOfBirth,
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
