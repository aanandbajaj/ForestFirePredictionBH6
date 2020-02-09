# over 6 month period, how fire spreads.
#

from enum import Enum
class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.terrain = TerrainType.NotAssigned
        self.onFire = False

    def __str__(self):
        string = "Location:\t" + str(self.x) + "\t" + str(self.y) + "; "
        string2 = ""
        return string

    def burn(self):
        self.onFire = True

class TerrainType(Enum):
    NotAssigned = 0
    Field = 1
    Forest = 2
    Desert = 3
    Wetland = 4
    River = 5
