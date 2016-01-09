#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return 'Hello World!'

@app.route('/restaurant/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    COM_TEMPLATE = True
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = '<h1>Restaurant: ' + restaurant.name + '</h1>'
    if COM_TEMPLATE:
        return render_template('menu.html', restaurant = restaurant, items = items)
    else:
        for i in items:
            output += str(i.id)
            output += '<br />'
            output += i.name
            output += '<br />'
            output += i.description
            output += '<br />'
            output += '{:10.2f}'.format(i.price)
            output += '<br />'
            output += '<br />'
        return output

# Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new', methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newMenuItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
        session.add(newMenuItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id = restaurant_id)

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
   return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
   return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
