#!/usr/bin/python3
"""
This script takes in an argument and displays
all information from the database `hbtn_0e_0_usa`
"""

import MySQLdb
import sys

if __name__ == '__main__':
    
     db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    
    for row in rows_selected:
        print(row)
