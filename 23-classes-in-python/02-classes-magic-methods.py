class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Point ({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

point = Point(3, 4)

# print(point.draw())

print(point)

