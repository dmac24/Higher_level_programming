#!/usr/bin/python3
'''displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.'''

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=argv[3])

    name = argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""".format(name))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
