#!/usr/bin/python3
""" Script that lists all states from database"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name = sys.arg[1:]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
