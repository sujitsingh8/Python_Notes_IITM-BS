# Hierarchical Inheritance
'''
Multiple child classes inherit from the same parent class.
Parent class  →  Child class 1, Child class 2, Child class 3, ...
'''

class Person: # Parent class
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person): # Child class 1
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

class Employee(Person): # Child class 2
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

s = Student("Rida", 250)
s.display()
# Rida 250

e = Employee("Harsh", 50000)
e.display()
# Harsh 50000