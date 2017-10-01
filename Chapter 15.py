class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def DistanceFromOrigin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


p = Point(2, 1)         # Instantiate an object of type Point
print(p)

q = Point(3, 4)         # Instantiate an object of type Point
print(q)

r = p.halfway(q)        # Calling a method of our class using the objects we have created
print(r)

print(Point(3, 4).halfway(Point(5, 12)))        # A shorter method that involves no variables

