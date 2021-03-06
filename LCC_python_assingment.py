#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:00:48 2018

@author: leacaterinacorsetti
"""

import json
with open('precipitation.json') as file:
    rain = json.load(file)

#rain_sample = dict(list(rain.items())[:20])

Seattle_station = 'GHCND:US1WAKG0038' #from the file
Seattle_precipitation = 0
Seattle = []
for item in rain:
    if item['station'] == Seattle_station:
        Seattle.append(item)
        Seattle_precipitation = Seattle_precipitation + item['value']

print(Seattle_precipitation) #total 11180

total_month_rain = []
list_months = ['01' , '02' , '03' , '04' , '05' , '06' , '07' , '08' , '09' , '10' , '11' , '12']
for month in list_months:
    monthly_rain = []
    for item in Seattle:
            if item['date'].split('-')[1] == month:
                monthly_rain.append(item['value'])
    total_month_rain.append(sum(monthly_rain))
print(total_month_rain)
# Values gained:
#1693
#730
#870
#752
#924
#601
#54
#104
#996
#908
#1192
#2356

#print(monthly_rain)

#part2:
#the total rainfall for Seattle was already calculated above, 
#therefore the individual monthly cifers would be compared to the calculated total
#this wopuld be done by running each individual month against the total
