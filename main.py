from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime, dateJDN, jdnDate
from flatlib.ephem.ephem import nextSolarReturn
from flatlib.geopos import GeoPos

date = Datetime('2024/01/01', '22:20', '+02:00')
pos = GeoPos('50n26', '30e31')


class BaZi:
    def __init__(self, date, pos):
        self.date = date
        self.pos = pos
        self.chart = Chart(date, pos)
        self.sun = self.chart.get(const.SUN)
        if date.time.toList()[1] >= 23:
            self.j_date = date.jd + 1
        else:
            self.j_date = date.jd

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

    def get_year_branch(self):
        if self.month_branch() in ["Zi", "Chou"]:
            year = self.date.date.toList()[1] - 1
        else:
            year = self.date.date.toList()[1]
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

    def get_year_stem(self):
        if self.month_branch() in ["Zi", "Chou"]:
            year = self.date.date.toList()[1] - 1
        else:
            year = self.date.date.toList()[1]
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

    def get_day_branch(self):
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

    def get_day_stem(self):
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

    def get_first_month_stem(self):
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
        return stems[self.get_year_stem()]

    def get_current_month_stem(self):
        heaven_stem = [
            "Jia", "Yi", "Bing", "Ding", "Wu",
            "Ji", "Geng", "Xin", "Ren", "Gui"
        ]

        earth_branch = [
            "Yin", "Mao", "Chen", "Si", "Wu", "Wei",
            "Shen", "You", "Xiu", "Hai", "Zi", "Chou"
        ]
        heaven_index = heaven_stem.index(self.get_year_stem())
        earth_index = earth_branch.index(self.month_branch())
        return heaven_stem[
            (heaven_index + (earth_index + heaven_index + 2)) % 10]

    def get_hour_branch(self):
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
            if key[0] <= self.date.time.toList()[1] < key[1]:
                return value

    def get_hour_first_stem(self):
        stems = {
            "Jia": "Jia",
            "Yi": "Bing",
            "Bing": "Wu",
            "Ding": "Geng",
            "Wu": "Ren",
            "Ji": "Jia",
            "Geng": "Bing",
            "Xin": "Wu",
            "Ren": "Geng",
            "Gui": "Ren"
        }
        return stems[self.get_day_stem()]

    def get_current_hour_stem(self):
        heaven_stem = [
            "Jia", "Yi", "Bing", "Ding", "Wu",
            "Ji", "Geng", "Xin", "Ren", "Gui"
        ]

        earth_branch = [
            "Zi", "Chou", "Yin", "Mao", "Chen", "Si",
            "Wu", "Wei", "Shen", "You", "Xiu", "Hai"
        ]
        heaven_index = heaven_stem.index(self.get_day_stem())
        earth_index = earth_branch.index(self.get_hour_branch())
        return heaven_stem[
            (heaven_index + (earth_index + heaven_index)) % 10]


a = BaZi(date, pos)
