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
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name\
            FROM cities JOIN states ON\
            cities.state_id=states.id\
            WHERE states.name LIKE %s\
            ORDER BY cities.id", (state_name,))
    query_rows = cur.fetchall()
    end = ""
    for row in query_rows:
        end += row[0] + ", "
        print(end[0:-2:)
    cur.close()
    db.close()
