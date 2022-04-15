


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
      return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        sum = Point(0,0)
        sum.x = self.x + other.x 
        sum.y = self.y + other.y
        return sum
point1 = Point(4, 5)
point2 = Point(3, 4)
point3 = Point(3, 4)

## False! Because two different references in memory. (They point to difference stores of memory)
# magic method to compare  __eq__ to allow comparision between objects
print(point2 == point3)

sum_point = (point1 + point2)
print(sum_point)

