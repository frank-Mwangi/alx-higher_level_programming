#!/usr/bin/python3

"""
Lists all cities by state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON\
                cities.states_id=states.id"))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state:
            print(row)
    cur.close()
    db.close()
