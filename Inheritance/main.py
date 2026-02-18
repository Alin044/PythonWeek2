# Inheritance = Allows a class to inherit attributes and methods from another class
# Class (Child / parent)

class Animal:
    def __init__(self, name):
            self.name = name
            self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")


class Dog(Animal):
    def speek(self):
        print("Woof")

class Cat(Animal):
    def speek(self):
        print("Meow")

class Mouse(Animal):
    def speek(self):
        print("Squeak")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.eat()
mouse.speek()