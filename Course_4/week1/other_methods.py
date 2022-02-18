class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(7, 6)
# print(p.getX())
# print(p.getY())
# print(p.distanceFromOrigin())
print(p)
p2 = Point(8, 9)
print(p2)
