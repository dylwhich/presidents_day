#!/usr/bin/env python3

import datetime
import math
import csv

presidents = []

class President:
    def __init__(self, order, name, birthdate, days_in_office, favorability):
        self.order = order
        self.name = name
        self.birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.days_in_office = int(days_in_office.replace(',', ''))
        self.favorability = int(favorability)

    def day_of_year(self):
        feb_28 = self.birthdate.replace(month=2, day=28)
        leap_day = feb_28 + datetime.timedelta(days=1)

        # If the day after feb 28 is in feb still, then it's a leap year
        leap_year = leap_day.month == 2

        year_start = self.birthdate.replace(month=1, day=1)
        day_of_year = (self.birthdate - year_start).days
        
        if not leap_year and self.birthdate > feb_28:
            return day_of_year + 1
        else:
            return day_of_year

with open('birthdays.csv', newline='') as f:
    pres_reader = csv.DictReader(f)
    for row in pres_reader:
        presidents.append(President(*row.values()))

pres_x = []
pres_y = []
pres_days = []
pres_favs = []

for pres in presidents:
    print(pres.name,
          pres.birthdate,
          pres.day_of_year(),
          datetime.date(year=2000, day=1, month=1) + datetime.timedelta(days=pres.day_of_year()))
    
    theta = 2 * math.pi * (pres.day_of_year() / 365)
    x, y = math.cos(theta), math.sin(theta)
    
    pres_x.append(x)
    pres_y.append(y)
    pres_days.append(pres.days_in_office)
    pres_favs.append(pres.favorability)

def get_date(xs, ys, weight=None):
    if weight is None:
        weight = [1] * len(xs)

    x_mean = sum((x * w for x, w in zip(xs, weight))) / sum(weight)
    y_mean = sum((y * w for y, w in zip(ys, weight))) / sum(weight)
    theta = math.atan2(y_mean, x_mean)
    days = theta / (2 * math.pi) * 365
    date = datetime.date(year=2000, month=1, day=1) + datetime.timedelta(days=int(days))

    return date

date_weighted_days = get_date(pres_x, pres_y, pres_days)
date_weighted_fav = get_date(pres_x, pres_y, pres_favs)
date_weighted_both = get_date(pres_x, pres_y, [d * f for d, f in zip(pres_days, pres_favs)])
date_unweighted = get_date(pres_x, pres_y)

print("******************")
print("Weighted (Days):        ", date_weighted_days)
print("Weighted (Favorability):", date_weighted_fav)
print("Weighted (both):        ", date_weighted_both)
print("Unweighted:             ", date_unweighted)
 
