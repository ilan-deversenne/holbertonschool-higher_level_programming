#!/usr/bin/python3

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect("localhost", username, password, database)

c = db.cursor()
c.execute("SELECT * FROM states;")

for row in c.fetchall():
    print(row)
