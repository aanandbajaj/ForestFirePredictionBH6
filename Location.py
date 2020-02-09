# over 6 month period, how fire spreads.
#

from enum import Enum
class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.terrain = TerrainType.NotAssigned

    def __str__(self):
        string = "Location: " + str(self.x) + " " + str(self.y) + " type: "
        return string

class TerrainType(Enum):
    NotAssigned = 0
    Field = 1
    Forest = 2
    Desert = 3
    Wetland = 4
    River = 5
