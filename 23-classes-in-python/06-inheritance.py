class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal : Parent / Base
# Mammal & Fish: Child / Sub class


class Mammal(Animal):
    def __init__(self):
        super().__init__() # give access to base class
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")


m = Mammal()
print(m.weight)
m.eat()


f = Fish()
print(f.age)

print(isinstance( m, object))
o = object()