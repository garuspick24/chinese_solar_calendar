from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime, dateJDN, jdnDate
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

date = Datetime('2024/05/05', '00:00', '+02:00')

pos = GeoPos('50n26', '30e31')



class BaZi:
    def __init__(self, date, pos):
        self.date = date.date
        self.time = date.time
        self.pos = pos
        self.chart = Chart(date, pos)
        self.sun = self.chart.get(const.SUN)
        self.j_date = date.jd + 0.5
        if date.time.toList()[1] >= 23:
            self.j_date = date.jd + 1

    def year_stem(self):
        if self.month_branch() in ["Zi", "Chou"]:
            year = self.date.toList()[1] - 1
        else:
            year = self.date.toList()[1]
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

    def year_branch(self):
        if self.month_branch() in ["Zi", "Chou"]:
            year = self.date.toList()[1] - 1
        else:
            year = self.date.toList()[1]
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

    def month_stem(self):
        heaven_stem = [
            "Jia", "Yi", "Bing", "Ding", "Wu",
            "Ji", "Geng", "Xin", "Ren", "Gui"
        ]

        earth_branch = [
            "Yin", "Mao", "Chen", "Si", "Wu", "Wei",
            "Shen", "You", "Xiu", "Hai", "Zi", "Chou"
        ]
        heaven_index = heaven_stem.index(self.year_stem())
        earth_index = earth_branch.index(self.month_branch())
        return heaven_stem[
            (heaven_index + (earth_index + heaven_index + 2)) % 10]

    def month_branch(self):
        branches = {
            (315, 345): "Yin",
            (345, 360): "Mao",
            (0, 15): "Mao",
            (15, 45): "Chen",
            (45, 75): "Si",
            (75, 105): "Wu",
            (105, 135): "Wei",
            (135, 165): "Shen",
            (165, 195): "You",
            (195, 225): "Xiu",
            (225, 255): "Hai",
            (255, 285): "Zi",
            (285, 315): "Chou"
        }
        for key, value in branches.items():
            if key[0] <= self.sun.lon < key[1]:
                return value

    def day_stem(self):
        stems = {
            1: "Jia",
            2: "Yi",
            3: "Bing",
            4: "Ding",
            5: "Wu",
            6: "Ji",
            7: "Geng",
            8: "Xin",
            9: "Ren",
            0: "Gui"
        }
        result = int(self.j_date) % 10
        return stems[result]

    def day_branch(self):
        branches = {
            11: "Zi",
            0: "Chou",
            1: "Yin",
            2: "Mao",
            3: "Chen",
            4: "Si",
            5: "Wu",
            6: "Wei",
            7: "Shen",
            8: "You",
            9: "Xiu",
            10: "Hai"
        }
        result = int(self.j_date) % 12
        return branches[result]

    def hour_stem(self):
        heaven_stem = [
            "Jia", "Yi", "Bing", "Ding", "Wu",
            "Ji", "Geng", "Xin", "Ren", "Gui"
        ]

        earth_branch = [
            "Zi", "Chou", "Yin", "Mao", "Chen", "Si",
            "Wu", "Wei", "Shen", "You", "Xiu", "Hai"
        ]
        heaven_index = heaven_stem.index(self.day_stem())
        earth_index = earth_branch.index(self.hour_branch())
        return heaven_stem[
            (heaven_index + (earth_index + heaven_index)) % 10]

    def hour_branch(self):
        branches = {
            (0, 1): "Zi",
            (1, 3): "Chou",
            (3, 5): "Yin",
            (5, 7): "Mao",
            (7, 9): "Chen",
            (9, 11): "Si",
            (11, 13): "Wu",
            (13, 15): "Wei",
            (15, 17): "Shen",
            (17, 19): "You",
            (19, 21): "Xiu",
            (21, 23): "Hai",
            (23, 24): "Zi"
        }
        for key, value in branches.items():
            if key[0] <= self.time.toList()[1] < key[1]:
                return value

    def __str__(self):
        return (f"Year: {a.year_stem()} {a.year_branch()}\n"
                f"Month: {a.month_stem()} {a.month_branch()}\n"
                f"Day: {a.day_stem()} {a.day_branch()}\n"
                f"Hour: {a.hour_stem()} {a.hour_branch()}\n")


a = BaZi(date, pos)


class DateSelection:
    def __init__(self, bazi: BaZi):
        self.year_stem = bazi.year_stem()
        self.year_branch = bazi.year_branch()
        self.month_stem = bazi.month_stem()
        self.month_branch = bazi.month_branch()
        self.day_stem = bazi.day_stem()
        self.day_branch = bazi.day_branch()
        self.hour_stem = bazi.hour_stem()

    def day_star(self):
        stars = ["jian", "chu", "man", "ping", "ding", "zhi", "po", "wei", "cheng", "shou", "kai", "bi"]
        branch = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xiu", "Hai"]
        index_month = branch.index(self.month_branch)
        index_day = branch.index(self.day_branch)

        return stars[((index_day - index_month) + 12) % 12]


print(a)
print(a.j_date)

a = DateSelection(BaZi(date, pos))
print(a.month_branch)
print(a.day_branch)
print(a.day_star())
