import math
from myutils import utils

def _remove_duplicates(l):
    return list(dict.fromkeys(l))


class Structure:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_border(self):
        return [(x,y)]

class RectangleStructure (Structure):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        super().__init__(x, y)

        self.w = w
        self.h = h

    def get_border(self):
        border = []

        for y in [self.y, self.y + self.h]:
            for x in range(self.x, self.x + self.w):
                border.append((x, y))
        for x in [self.x, self.x + self.w]:
            for y in range(self.y, self.y + self.h):
                border.append((x, y))

        return _remove_duplicates(border)

class CircleStructure (Structure):
    def __init__(self, x = 0, y = 0, r = 0):
        super().__init__(x, y)

        self.r = r
    
    def get_border(self):
        border = []
        for theta in range(0, 360):
            x = round(math.sin(math.radians(theta)) * self.r)
            y = round(math.cos(math.radians(theta)) * self.r)

            border.append((self.x + x, self.y + y))

        return _remove_duplicates(border)

class LineStructure (Structure):
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = x1

        self.x2 = x2 
        self.y2 = y2
    
    def get_border(self):
        border = []
        for x, y in zip(range(0, 100), range(0, 100)):
            nx = utils.map2range(x, 0, 100, self.x1, self.x2)
            ny = utils.map2range(y, 0, 100, self.y1, self.y2)
            border.append((nx, ny))
        return _remove_duplicates(border)
