#!/usr/bin/python3

"""Lists all states starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE\
                name='{:s}' ORDER BY id ASC".format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state:
            print(row)
    cur.close()
    db.close()
