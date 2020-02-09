import json
import sys
import jsonpickle
from Regression import predictBurnedArea
from Map import Map
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

map = Map(30, 30)



temp = int(sys.argv[1])
relHumidity = int(sys.argv[2])
wind = int(sys.argv[3])
rain = int(sys.argv[4])


map.setGlobalAttribute(temp, relHumidity, wind, rain)
map.drawRiver(2)
map.drawForest(5)
map.fillField()

map_list = []

map_list.append(jsonpickle.encode(map))

map.spawnFire()

map_list.append(jsonpickle.encode(map))

i = 3
p = map.getGlobalAttribute()
area = predictBurnedArea(p[0], p[1], p[2], p[3])
while(i < area):
    map.firespread(i)
    i += 1
    map_list.append(jsonpickle.encode(map))

with open('mapfile.txt', 'w') as outfile:
    json.dump(map_list, outfile)