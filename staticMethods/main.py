#Class methods

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}" #this is an instance method

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average class gpa :  {cls.total_gpa / cls.count}"

student1 = Student("Radu", 3.5)
student2 = Student("Mihai", 4.0)
print(Student.get_count())

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