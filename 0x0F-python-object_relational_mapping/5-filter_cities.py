#!/usr/bin/python3
""" script that takes in name of state as arg and lists cities of that db"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name, state_name = sys.argv[1:]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
    JOIN states ON state_id = states.id
    WHERE states.name LIKE %s ORDER BY cities.id""", (state_name,))

    rows = cur.fetchall()
    flattened_list = [element for tupl in rows for element in tupl]
    print(", ".join(flattened_list))

    cur.close()
    db.close()
