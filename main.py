from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

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
