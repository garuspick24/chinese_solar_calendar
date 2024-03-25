from flatlib.chart import Chart
from flatlib.datetime import Datetime, dateJDN, jdnDate
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

date = Datetime('2024/01/01', '17:00', '+02:00')
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


def month_branch(day):
    branches = {
        (yin.jd, mao.jd): "Yin",
        (mao.jd, chen.jd): "Mao",
        (chen.jd, si.jd): "Chen",
        (si.jd, wu.jd): "Si",
        (wu.jd, wei.jd): "Wu",
        (wei.jd, shen.jd): "Wei",
        (shen.jd, you.jd): "Shen",
        (you.jd, xiu.jd): "You",
        (xiu.jd, hai.jd): "Xiu",
        (hai.jd, zi.jd): "Hai",
        (zi.jd, chou.jd): "Zi",
        (chou.jd, yin.jd): "Chou"
    }
    for key, value in branches.items():
        if key[0] <= day < key[1]:
            return value


def get_year_branch(year):
    branches = {
        4: "Zi",
        5: "Chou",
        6: "Yin",
        7: "Mao",
        8: "Chen",
        9: "Si",
        10: "Wu",
        11: "Wei",
        0: "Shen",
        1: "You",
        2: "Xiu",
        3: "Hai"
    }
    return branches[year % 12]


def get_year_stem(year):
    stems = {
        4: "Jia",
        5: "Yi",
        6: "Bing",
        7: "Ding",
        8: "Wu",
        9: "Ji",
        0: "Geng",
        1: "Xin",
        2: "Ren",
        3: "Gui"
    }
    return stems[year % 10]


def get_day_branch(j_date):
    branches = {
        0: "Zi",
        1: "Chou",
        2: "Yin",
        3: "Mao",
        4: "Chen",
        5: "Si",
        6: "Wu",
        7: "Wei",
        8: "Shen",
        9: "You",
        10: "Xiu",
        11: "Hai"
    }
    result = j_date % 12
    return branches[int(result)]


def get_day_stem(j_date):
    stems = {
        4: "Jia",
        5: "Yi",
        6: "Bing",
        7: "Ding",
        8: "Wu",
        9: "Ji",
        0: "Geng",
        1: "Xin",
        2: "Ren",
        3: "Gui"
    }
    return stems[j_date % 10]


def get_first_month_stem(year_stem):
    stems = {
        "Jia": "Bing",
        "Yi": "Wu",
        "Bing": "Geng",
        "Ding": "Ren",
        "Wu": "Jia",
        "Ji": "Bing",
        "Geng": "Wu",
        "Xin": "Geng",
        "Ren": "Ren",
        "Gui": "Jia"
    }
    return stems[year_stem]


def get_current_month_stem(year_stem, month_branch):
    if year_stem in ["Jia", "Ji"]:
        index = 1
    elif year_stem in ["Yi", "Geng"]:
        index = 2
    elif year_stem in ["Bing", "Xin"]:
        index = 3
    elif year_stem in ["Ding", "Ren"]:
        index = 4
    elif year_stem in ["Wu", "Gui"]:
        index = 0

    data = {
        "Yin": ("Jia", "Bing", "Wu", "Geng", "Ren"),
        "Mao": ("Yi", "Ding", "Ji", "Xin", "Gui"),
        "Chen": ("Bing", "Wu", "Geng", "Ren", "Jia"),
        "Si": ("Ding", "Ji", "Xin", "Gui", "Yi"),
        "Wu": ("Wu", "Geng", "Ren", "Jia", "Bing"),
        "Wei": ("Ji", "Xin", "Gui", "Yi", "Ding"),
        "Shen": ("Geng", "Ren", "Jia", "Bing", "Wu"),
        "You": ("Xin", "Gui", "Yi", "Ding", "Ji"),
        "Xiu": ("Ren", "Jia", "Bing", "Wu", "Geng"),
        "Hai": ("Gui", "Yi", "Ding", "Ji", "Xin"),
        "Zi": ("Jia", "Bing", "Wu", "Geng", "Ren"),
        "Chou": ("Yi", "Ding", "Ji", "Xin", "Gui")
    }
    return data[month_branch][index]


date_now = Datetime('2024/04/28', '17:00', '+02:00')
day_test = date_now.jd
print(day_test)
day = dateJDN(2024, 4, 28, calendar="GREGORIAN")
print(day)
print(jdnDate(day_test))
print(jdnDate(day))



print(date_now)
print(f"Year stem: {get_year_stem(2024)}")
print(f"Year branch: {get_year_branch(2024)}")
print(f"Current month stem: {get_current_month_stem(get_year_stem(2024), month_branch(day_test))}")
print(f"Month branch: {month_branch(day_test)}")
print(f"Day stem: {get_day_stem(day)}")
print(f"Day branch: {get_day_branch(day)}")


