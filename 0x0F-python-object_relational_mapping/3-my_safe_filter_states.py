#!/usr/bin/python3
"""Sript that takes in an argument and displays all values in the states"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name, state_name_search = sys.argv[1:]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE %s ORDER BY states.id""", (state_name_search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
