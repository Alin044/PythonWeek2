# multiple inheritance = inherit from more the one parent class
#                        C(A, B)

#super()

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def discribe(self):
        print(f"It is {self.color} and it is {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with the are of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with the area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with the area of {self.width * self.height / 2}cm^2")
        super().describe()



circle = Circle("red", True, 10)
print(circle.color)

square = Square("blue", False, 10)
print(square.color)
print(square.is_filled)
print(square.width)

triangle = Triangle("green", True, 10, 20)
print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)










#------------------------------------------
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

rabbit.eat()