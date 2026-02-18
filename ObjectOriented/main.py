from ObjectOriented.car import Car

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


car1 = Car("BMW", 2021, "blue", True)
car2 = Car("Audi", 2020, "red", False)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.stop()
car2.describe()