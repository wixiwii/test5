import sqlite3

conn = sqlite3.connect('weather.db')
c = conn.cursor()

c.execute('''CREATE TABLE temperatures
             (date text, time text, temperature real)''')

conn.commit()
conn.close()


