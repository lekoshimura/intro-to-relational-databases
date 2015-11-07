#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

c = sqlite3.connect('puppyshelter.db')
c.execute('alter table shelter add column maximum_capacity integer');
c.execute('alter table shelter add column current_occupancy integer');
c.execute('update shelter set maximum_capacity = id * 10')
c.execute('update shelter set current_occupancy = maximum_capacity - 3')
c.commit()
c.close()

print 'Acabou.'
