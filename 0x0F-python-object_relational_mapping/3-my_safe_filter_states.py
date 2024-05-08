#!/usr/bin/python3
"""
Displays all values in the states
& is safe from SQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306,
                            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
