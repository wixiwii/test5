import sqlite3
import requests

conn = sqlite3.connect('bazadanix.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS websites
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT)''')

cursor.execute('''INSERT INTO websites(url) VALUES ('https://www.google.com/')''')

poisk = input("напишите слово для поиска")

cursor.execute("SELECT * FROM websites WHERE url = 'https://www.google.com/'")
for row in cursor:
    url = row[1]
    response = requests.get(url)
    if poisk in response.text:
        print(f"мы нашли это слово '{poisk}' в нашей базе {url}")
else:
    print("извините такого слова нет в нашей базе")

conn.close()
