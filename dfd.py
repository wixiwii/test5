import os
import requests
from bs4 import BeautifulSoup
import sqlite3


class WebSearch:
    def __init__(self, db_path):
        self.db_path = db_path

    def search(self, nyam):

        conn = sqlite3.connect(self.db_path)
        lol = conn.cursor()

        lol.execute("SELECT url FROM sites")
        urls = lol.fetchall()
        results = {}
        for url in urls:
            page = requests.get(url[0])
            soup = BeautifulSoup(page.content, 'html.parser')
            text = soup.get_text()
            count = text.count(nyam)
            if count > 0:
                results[url[0]] = count
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
        return sorted_results

    def add_site(self, url):
        if not os.path.exists(self.db_path):

            self.create_database()

        conn = sqlite3.connect(self.db_path)
        lol = conn.cursor()
        lol.execute("SELECT * FROM sites WHERE url=?", (url,))
        if lol.fetchone() is not None:
            print(f"{url} is already in the database")
            return

        lol.execute("INSERT INTO sites (url) VALUES (?)", (url,))
        conn.commit()
        print(f"{url} has been added to the database")

    def clear_database(self):

        conn = sqlite3.connect(self.db_path)
        lol = conn.cursor()
        lol.execute("DELETE FROM sites")
        conn.commit()
        print("Database has been cleared")

    def create_database(self):
        conn = sqlite3.connect(self.db_path)
        lol = conn.cursor()
        lol.execute('''CREATE TABLE sites
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      url TEXT UNIQUE)''')
        conn.commit()
        print(f"Database {self.db_path} has been created")

web_search = WebSearch('sites.db')

web_search.add_site('https://instagram.com')
web_search.add_site('https://www.google.com/?hl=ru')

results = web_search.search('Domovoy')
print(results)

web_search.clear_database()
