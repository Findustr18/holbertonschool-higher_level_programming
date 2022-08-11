#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usalists
Script should take 4 arguments: mysql username,
mysql password, database name and state name (SQL injection free!)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # create cursor to exec queries using SQL
    cursor = db.cursor()
    check = (argv[4], )
    cursor.execute("SELECT * FROM cities JOIN states\
            ON cities.state_id=states.id WHERE states.name = %s\
            ORDER BY cities.id ASC", check)
    cities = []
    for r in cursor.fetchall():
        if r[4] == check[0]:
            cities.append(r[2])
    print(', '.join(cities))
    cursor.close()
    db.close()
