#!/usr/bin/python3

"""
Fetch all states
"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

c = db.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")

for row in c.fetchall():
    print(row)

c.close()
db.close()
