#!/usr/bin/python3
"""Sript that takes in an argument and displays values"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name, state_name_search = sys.argv[1:]
    cmd = """SELECT * FROM states
    WHERE name LIKE BINARY '{:s}'
    ORDER BY states.id""".format(state_name_search)
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
