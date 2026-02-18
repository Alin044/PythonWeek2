#Static Methods

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

pos = Employee.is_valid_position("Manager")
print(pos)

employee1 = Employee("Radu", "Manager")
employee2 = Employee("Mihai", "Cook")
employee3 = Employee("Ioana", "Janitor")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())