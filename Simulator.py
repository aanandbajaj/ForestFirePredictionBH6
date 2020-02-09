
from Map import Map

map = Map(30, 30)
map.drawRiver(2)
map.drawForest(5)
map.fillField()
map.spawnFire()
map.firespread(15)
map.printMap()

