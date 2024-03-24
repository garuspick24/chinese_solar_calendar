import sqlite3
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS calendar (
        id INTEGER PRIMARY KEY,
        date TEXT,
        year_stem TEXT,
        year_branch TEXT
    )
''')
conn.commit()

# Build a chart for a date and location
date = Datetime('2024/03/24', '17:00', '+02:00')
pos = GeoPos('50n26', '30e31')
chart = Chart(date, pos)

# Визначили дати зміни місяців і років
yin = nextSolarReturn(date, 315)
mao = nextSolarReturn(date, 345)
chen = nextSolarReturn(date, 15)
si = nextSolarReturn(date, 45)
wu = nextSolarReturn(date, 75)
wei = nextSolarReturn(date, 105)
shen = nextSolarReturn(date, 135)
you = nextSolarReturn(date, 165)
xiu = nextSolarReturn(date, 195)
hai = nextSolarReturn(date, 225)
zi = nextSolarReturn(date, 255)
chou = nextSolarReturn(date, 285)

year_stem = "Jia"
year_branch = "Zi"

data = (str(date), year_stem, year_branch)

cursor.execute(
    'INSERT INTO calendar (date, year_stem, year_branch) VALUES (?, ?, ?)',
    data)
conn.commit()

# Закриття підключення
conn.close()
