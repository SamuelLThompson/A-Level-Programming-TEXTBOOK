import copy

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

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

box = Rectangle(Point(0, 0), 100, 200)
print("box: ", box)
box.grow(25, -10)
print("box: ", box)

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 is p2)
same_coordinates(p1, p2)

p1 = Point(3, 4)
p2 = copy.copy(p1)
print(p1 is p2)
same_coordinates(p1, p2)

box2 = copy.deepcopy(box)
print(box is box2)

