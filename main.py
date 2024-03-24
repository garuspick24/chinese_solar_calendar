from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

# Build a chart for a date and location
date = Datetime('2024/03/24', '17:00', '+02:00')
pos = GeoPos('50n26', '30e31')
chart = Chart(date, pos)

# Визначили дати зміни місяців і років

print(nextSolarReturn(date, 15))
print(nextSolarReturn(date, 45))
print(nextSolarReturn(date, 75))
print(nextSolarReturn(date, 105))
print(nextSolarReturn(date, 135))
print(nextSolarReturn(date, 165))
print(nextSolarReturn(date, 195))
print(nextSolarReturn(date, 225))
print(nextSolarReturn(date, 255))
print(nextSolarReturn(date, 285))
print(nextSolarReturn(date, 315))
print(nextSolarReturn(date, 345))
