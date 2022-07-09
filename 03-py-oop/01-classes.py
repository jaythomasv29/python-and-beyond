class Robot:

    def __init__(self, name, team, weight, price):
        self.is_on = False
        self.name = name
        self.team = team
        self.weight = weight
        self.price = price

    def toggleOn(self):
      self.is_on = not self.is_on
r1 = Robot('wall-e', 'red-team', 200, 199.99)
print(r1.__dict__)

class Drone(Robot):
    def __init__(self, name, team, weight, price):
      super().__init__(name, team, weight, price)
      self.is_flying = False

d1 = Drone('d1r', 'automation', 200, 999.99)
d1.toggleOn()
print(d1.__dict__)