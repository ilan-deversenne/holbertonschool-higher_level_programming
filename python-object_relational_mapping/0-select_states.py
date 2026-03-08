#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(
    host="localhost",
    username=sys.argv[1],
    password=sys.argv[2],
    database=sys.argv[3],
    port=3306
)

c = db.cursor()
c.execute("SELECT * FROM states;")

for row in c.fetchall():
    print(row)

c.close()
db.close()
