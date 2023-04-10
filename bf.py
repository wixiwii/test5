import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE cars (id INTEGER PRIMARY KEY, name TEXT)')

cars = [
    'Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Kia',
    'Mercedes-Benz', 'Nissan', 'Toyota', 'Volkswagen'
]
for car in cars:
    cursor.execute('INSERT INTO cars (name) VALUES (?)', (car,))

cursor.execute('DELETE FROM cars WHERE name IN (?, ?)', ('Ford', 'Nissan'))

cursor.execute('UPDATE cars SET name = ? WHERE name IN (?, ?, ?)', ('Chevrolet', 'Honda', 'Hyundai', 'Kia'))

cursor.execute('DROP TABLE cars')

conn.commit()
conn.close()