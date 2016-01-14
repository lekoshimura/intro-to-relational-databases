#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppy import Base, Puppy, Shelter, PuppyProfile, Adopter, PuppyAdopter

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

@app.route('/shelter/list')
def shelterList():
    shelters = session.query(Shelter).all()
    return render_template('shelter-list.html', shelters = shelters)

@app.route('/adopter/list')
def adopterList():
    adopters = session.query(Adopter).all()
    return render_template('adopter-list.html', adopters = adopters)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
