#!/usr/bin/python3

"""
Lists all cities in given state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    state = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name\
        FROM cities JOIN states ON\
        cities.state_id=states.id\
        WHERE states.name= %s\
        ORDER BY cities.id", (state,))
    query_rows = cur.fetchall()
    i = 0
    for row in query_rows:
        if i > 0:
            print(", ", end="")
        print(row[0], end="")
        i += 1
    print("")
    cur.close()
    db.close()
