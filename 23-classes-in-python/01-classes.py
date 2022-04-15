# Classes are a blue print for creating and object

# Objects are instances of Classes

# Creating a class
class Point:
    default_color = "red" # class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod # decorator
    def zero(cls): # factory method
        return cls(0, 0)

    def draw(self):
        return(f"Point {self.x}, {self.y}")


p1 = Point(1, 2)
p1.draw()
print(p1.default_color)
print(Point.default_color)
p1.z = 10 # instance attributes
point = Point.zero() # calling factory method
print(point.draw())
# print(type(p1))
# print(isinstance(p1, Point))
