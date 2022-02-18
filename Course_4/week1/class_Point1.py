# Scratch file

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):  # the initializer method, aka constructor

        self.x = 0
        self.y = 0


p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)

"""A function like Point that creates a new object instance is called a constructor. Every class automatically uses the name of the class as the name of the constructor function. The definition of the constructor function is done when you write the __init__ function (method) inside the class definition."""

"""It may be helpful to think of a class as a factory for making objects. The class itself isn’t an instance of a point, but it contains the machinery to make point instances. Every time you call the constructor, you’re asking the factory to make you a new object. As the object comes off the production line, its initialization method is executed to get the object properly set up with it’s factory default settings."""

"""The combined process of “make me a new object” and “get its settings initialized to the factory default settings” is called instantiation."""
