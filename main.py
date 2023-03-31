import sqlite3
connection=sqlite3.connect("itstep_DB.sl3",5)
cur = connection.cursor()

cur.execute("CREATE TABLE first table (name TEXT);")
connection.commit()

connection.close()