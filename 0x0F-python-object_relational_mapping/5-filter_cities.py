#!/usr/bin/python3
""" This is the 5-filter_cities module it lists all the cities
in a state in hbtn_0e_0_usa database """


import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    if ';' not in sys.argv[4]:
        cur.execute("SELECT cities.name FROM states \
                    INNER JOIN cities ON states.id = cities.state_id \
                    WHERE states.name='{0}' \
                    COLLATE utf8mb4_0900_as_cs \
                    ORDER BY cities.id".format(sys.argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
            if query_rows.index(row) != len(query_rows) - 1:
                print(f"{row[0]}, ", end='')
            else:
                print(f"{row[0]}")
    cur.close()
    conn.close()
