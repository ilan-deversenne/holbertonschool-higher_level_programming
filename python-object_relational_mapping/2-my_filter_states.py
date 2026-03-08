#!/usr/bin/python3

"""
Fetch all states where name equals to argv 4
"""

import MySQLdb
import sys


def main():
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

    name = sys.argv[4].replace("'", '')

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(name))

    for row in c.fetchall():
        print(row)

    c.close()
    db.close()


if __name__ == '__main__':
    main()
