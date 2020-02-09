import Location
import random
import jsonpickle
from Location import Location
from Location import TerrainType
from random import randint
from colorama import Fore, Back, Style

class Map:

    def __init__(self, sizeX, sizeY):

        self.time = 0

        # size of the map
        self.sizeX = sizeX
        self.sizeY = sizeY

        # initialize the map
        self.rows = []
        self.globalAttribute = {}
        self.fireLocation = []
        element_init = []
        for i in range(1, sizeY+1):
            elements = element_init.copy()
            for j in range(1, sizeX+1):
                location = Location(i, j)
                elements.append(location)
            self.rows.append(elements)

    def timePass(self):
        self.time += 1

    def getLocation(self, x, y):
        if x<1 or y<1 or x>=self.sizeX+1 or y>=self.sizeY+1:
            return None
        return self.rows[x-1][y-1]

    def setGlobalAttribute(self, temp, relHumidity, wind, rain):
        self.globalAttribute['temp'] = temp
        self.globalAttribute['relHumidity'] = relHumidity
        self.globalAttribute['wind'] = wind
        self.globalAttribute['rain'] = rain

    def getGlobalAttribute(self):
        return [self.globalAttribute['temp'], self.globalAttribute['relHumidity'], self.globalAttribute['wind'], self.globalAttribute['rain']]

    def printMap(self):
        for i in self.rows:
            for j in i:
                # Back.RESET()
                if j.terrain == TerrainType.NotAssigned: # not assigned color
                    print(Back.WHITE, end="")
                elif j.terrain == TerrainType.River:
                    print(Back.BLUE, end="")
                elif j.terrain == TerrainType.Wetland:
                    print(Back.LIGHTGREEN_EX, end="")
                elif j.terrain == TerrainType.Forest:
                    print(Back.GREEN, end="")
                elif j.terrain == TerrainType.Field:
                    print(Back.YELLOW, end="")
                if j.onFire == True:
                    print(Back.RED, end="")
                print(j, end="")
            print(" ")

    # Draw a certain number of rivers on the map
    def drawRiver(self, rNum):
        x = randint(1, self.sizeX)
        y = randint(1, self.sizeY)
        directionX = randint(-1, 1)
        directionY = randint(-1, 1)
        for i in range(0, rNum):
            self.drawRiverRec(x, y, directionX, directionY)
        return None

    # Draw a river start from position (x,y) recursively
    def drawRiverRec(self, x, y, directionX, directionY):
        if (x <= 1) or (y <= 1) or (x > self.sizeX) or (y > self.sizeY):

            return None
        else:
            loc = self.getLocation(x, y)
            loc.terrain = TerrainType.River
            #self.drawwetland(x, y)
            # print("Drawn River at: " + str(x) + " " + str(y)) # for debug
            direction = randint(1, 4)
            if direction == 1:
                # print("River flowing to " + str(x+directionX) + " " + str(y+directionY))
                return self.drawRiverRec(x+directionX, y+directionY, directionX, directionY)
            elif direction == 2:
                # print("River flowing to " + str(x+directionX) + " " + str(y))
                return self.drawRiverRec(x+directionX, y, directionX, directionY)
            elif direction == 3:
                # print("River flowng to " + str(x) + " " + str(y+directionY))
                return self.drawRiverRec(x, y+directionY, directionX, directionY)
            elif direction == 4:
                return self.drawRiverRec(x+directionY, y+directionX, directionX, directionY)

    # draw wetland based on riverside based on random number
    def drawwetland(self, x, y):
        r1 = randint(-1,1)
        r2 = randint(-1,1)

        newX = x + r1
        newY = y + r2
        if newX>1 and newX<self.sizeX and newY>1 and newY<self.sizeX:
            loc = self.getLocation(newX, newY)
            if loc.terrain == TerrainType.NotAssigned:
                loc.terrain = TerrainType.Wetland

    def drawForest(self, fNum):
        while fNum > 0:
            x = randint(1, self.sizeX)
            y = randint(1, self.sizeY)
            loc = self.getLocation(x, y)
            if loc.terrain == TerrainType.NotAssigned:
                self.growForestRec(x, y, 0)
            fNum -= 1

    def growForestRec(self, x, y, generation):
        if (x <= 1) or (y <= 1) or (x > self.sizeX) or (y > self.sizeY):

            return None
        else:
            r0 = randint(0,99)
            if r0 > (15 * generation):
                loc = self.getLocation(x,y)
                loc.terrain = TerrainType.Forest
                dir_lst = ["N", "S", "E", "W"]
                while(len(dir_lst) > 0):
                    random.shuffle(dir_lst)
                    dir = dir_lst[0]
                    if dir == "N":
                        self.growForestRec(x, y+1, generation+1)
                    elif dir == "S":
                        self.growForestRec(x, y-1, generation+1)
                    elif dir == "E":
                        self.growForestRec(x+1, y, generation+1)
                    else:
                        self.growForestRec(x-1, y, generation+1)
                    dir_lst.pop(0)

    # field the rest as field land
    def fillField(self):
        for i in self.rows:
            for j in i:
                if j.terrain == TerrainType.NotAssigned:
                    j.terrain = TerrainType.Field

    def spawnFire(self):
        x = randint(1, self.sizeX)
        y = randint(1, self.sizeY)
        loc = self.getLocation(x, y)
        if loc.terrain != TerrainType.River or loc.terrain != TerrainType.Desert:
            if loc.onFire == False:
                self.burnLocation(loc)
                return
        self.spawnFire()

    def burnLocation(self, loc):
        loc.burn()
        self.fireLocation.append(loc)


    def firespread(self, total):
        while(len(self.fireLocation) < total): # when there is not enough fire
            for i in self.fireLocation:
                self.firespreadRec(i)
                if len(self.fireLocation) == total:
                    return



    def firespreadRec(self, loc):
        x = loc.x
        y = loc.y
        neighbor = []
        neighbor.append(self.getLocation(x-1, y-1))
        neighbor.append(self.getLocation(x, y-1))
        neighbor.append(self.getLocation(x+1, y-1))
        neighbor.append(self.getLocation(x-1, y))
        neighbor.append(self.getLocation(x+1, y))
        neighbor.append(self.getLocation(x-1, y+1))
        neighbor.append(self.getLocation(x, y+1))
        neighbor.append(self.getLocation(x+1, y+1))

        res_neigbhor = list(filter(None, neighbor))

        res_neigbhor.sort(key=generateFireValue)
        loc = res_neigbhor[0]
        self.burnLocation(loc)

    def toCsv(self):
        csv = []

        for i in self.rows:
            for j in i:
                s = str(j.x) + ", " + str(j.y) + ", " + str(j.terrain) + ", " + str(j.onFire) + ", " + str(self.time)
                csv.append(s)
        return csv

def generateFireValue(coe):
    r = randint(0, 9)
    return r * coe.getFireSpeadFactor()
