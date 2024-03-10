class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point): # This will check if the other object are Point object
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: 'Point' and '{}'".format(type(other).__name__))

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

point1 = Point(2,3) # This will be used as the `self` in __add__ function
point2 = Point(3,4) # This will be used as the `other` in __add__ function
point3 = point1 + point2 # This will called the __add__ method
print(point3) # This will call the __str__ method
print("Hello World!") # This return as the normal function