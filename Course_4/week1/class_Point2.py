class Point:
    """ Point class for representing and manipulating x,y coordinates"""

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY


p = Point(7, 6)
print(p.x)
print(p.y)
print(type(p))
