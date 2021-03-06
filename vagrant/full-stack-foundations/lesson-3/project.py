#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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
    if COM_TEMPLATE:
        return render_template('menu.html', restaurant = restaurant, items = items)
    else:
        output = '<h1>Restaurant: ' + restaurant.name + '</h1>'
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
        flash('New menu item created')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id = restaurant_id)

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).get(menu_id);
    if request.method == 'POST':
        if (request.form['name']):
            item.name = request.form['name'];
        session.add(item);
        session.commit();
        flash('Menu item edited')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template(
            'editMenuItem.html',
            restaurant_id = restaurant_id,
            menu_id = menu_id,
            i = item
        );

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).get(menu_id);
    if request.method == 'POST':
        session.delete(item);
        session.commit();
        flash('Menu item deleted')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template(
            'deleteMenuItem.html',
            restaurant_id = restaurant_id,
            menu_id = menu_id,
            item = item
        );

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id);
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MeunItems = [i.serialize for i in items])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).get(menu_id)
    return jsonify(MenuItem = item.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
