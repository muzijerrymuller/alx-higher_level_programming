#!/usr/bin/python3
"""
Lists all states in ascending order by states.id
"""


import sys
import MySQLdb

def list_states(mysql_username, mysql_password, db_name):
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )

        cur = conn.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cur.fetchall()

        for row in rows:
            print(row[1])

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py mysql_username mysql_password db_name")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(mysql_username, mysql_password, db_name)
