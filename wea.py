import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather
             (date text, time text, temperature real)''')

url = 'https://www.gismeteo.ru/weather-baku-4669/now/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

temperature = soup.find('span', class_='js_value tab-weather__value_l').text

now = datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')

c.execute("INSERT INTO weather VALUES (?, ?, ?)", (date, time, temperature))

conn.commit()
conn.close()
