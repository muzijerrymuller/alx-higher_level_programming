#!/usr/bin/python3
"""
This script takes in an argument and displays
all information from the database `hbtn_0e_0_usa`
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
