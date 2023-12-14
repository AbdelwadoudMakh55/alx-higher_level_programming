#!/usr/bin/python3
""" This is the 3-my_safe_filter_states module it lists the states based
on user input safely in hbtn_0e_0_usa database """


import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    if ';' not in sys.argv[4]:
        cur.execute("SELECT * FROM states WHERE name = %s", [sys.argv[4]])
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()
