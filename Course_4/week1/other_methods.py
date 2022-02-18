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

"""The default functionality provided by Python tells you that p is an object of type Point. However, it does not tell you anything about the specific state of the point.

We can improve on this representation if we include a special method call __str__. Notice that this method uses the same naming convention as the constructor, that is two underscores before and after the name. It is common that Python uses this naming technique for special methods.

The __str__ method is responsible for returning a string representation as defined by the class creator. In other words, you as the programmer, get to choose what a Point should look like when it gets printed. In this case, we have decided that the string representation will include the values of x and y as well as some identifying text. It is required that the __str__ method create and return a string.

Whatever string the __str__ method for a class returns, that is the string that will print when you put any instance of that class in a print statement. For that reason, the string that a class’s __str__ method returns should usually include values of instance variables. If a point has x value 3 and y value 4, but another point has x value 5 and y value 9, those two Point objects should probably look different when you print them, right?"""
