import Location
from Location import Location

class Map:
    def __init__(self, sizeX, sizeY):

        # size of the map
        self.sizeX = sizeX
        self.sizeY = sizeY

        # initialize the map
        self.rows = []
        element_init = []
        for i in range(1, sizeY+1):
            elements = element_init.copy()
            for j in range(1, sizeX+1):
                location = Location(i, j)
                elements.append(location)
            self.rows.append(elements)

    def printMap(self):
        for i in self.rows:
            for j in i:
                print(j, end="")
            print(" ")