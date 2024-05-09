#!/usr/bin/python3
"""
This script retrieves and lists all cities from the 'hbtn_0e_4_usa' database.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
   
        with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
