#!/usr/bin/python3
"""
Lists all states in ascending order by states.id
"""
import sys
import MySQLdb

def list_states(mysql_username, mysql_password, db_name):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )

        # Create cursor
        cur = conn.cursor()

        # Execute SQL query to select states
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

        # Close cursor and connection
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))

if __name__ == "__main__":
    # Extract MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, db_name)
