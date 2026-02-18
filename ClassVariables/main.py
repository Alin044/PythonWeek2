#class variables = shared amon all instances of a class
#                  defined outside the constructor
#                   allow u to share data among all objects created from the class


class Student :

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Radu", 21)
student2 = Student("Mihai", 20)
student3 = Student("Ioana", 22)
student4 = Student("Cristian", 23)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.class_year)
print(Student.num_students)