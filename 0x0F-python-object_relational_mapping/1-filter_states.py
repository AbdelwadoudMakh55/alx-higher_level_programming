#!/usr/bin/python3
""" This is the 0-select_states module it lists all the states present in the
hbtn_0e_0_usa database """


import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
