import json
import sys
import jsonpickle
import csv
from Regression import predictBurnedArea
from Map import Map
from flask import Flask, jsonify, request, render_template

map = Map(30, 30)

temp = int(sys.argv[1]) # 2 to 30
relHumidity = int(sys.argv[2]) # 15 to 100
wind = int(sys.argv[3]) # 1 to 9
rain = int(sys.argv[4]) # 0 to 6

map.setGlobalAttribute(temp, relHumidity, wind, rain)
map.drawRiver(2)
map.drawForest(5)
map.fillField()

csv_file = [map.toCsv()]

map.timePass()

map.spawnFire()
csv_file.append(map.toCsv())
map.timePass()


i = 3

p = map.getGlobalAttribute()
area = predictBurnedArea(p[0], p[1], p[2], p[3])
area_f = area * 10
while(i < area_f):
    map.firespread(i)
    i += 1
    csv_file.append(map.toCsv())
    map.timePass()

with open('mapfile.csv', 'w') as outfile:
    for lines in csv_file:
        for line in lines:
            outfile.write('%s\n' % line)

