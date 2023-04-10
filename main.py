import requests
from bs4 import BeautifulSoup
import sqlite3

class SearchEngine:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS sites
                     (url text)''')
        conn.commit()
        conn.close()

    def add_site(self, url):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO sites VALUES (?)", (url,))
        conn.commit()
        conn.close()

    def clear_database(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM sites")
        conn.commit()
        conn.close()

    def search(self, term):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        sites = c.execute("SELECT * FROM sites").fetchall()
        results = []
        for site in sites:
            url = site[0]
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            count = soup.text.lower().count(term.lower())
            results.append((url, count))
        results.sort(key=lambda x: x[1], reverse=True)
        conn.close()
        return results

engine = SearchEngine('database.db')
engine.add_site('https://www.example.com')
engine.add_site('https://www.google.com')
results = engine.search('example')
print(results)
