# Multilevel Inheritance
'''
A child class becomes a parent for another class.
Parent class  →  Intermediate class  →  Child class
'''

class Person: # Parent class
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person): # Intermediate class, act as Parent class for Result class and Child class for Person class
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class Result(Student): # Child class
    def __init__(self, name, marks, status):
        super().__init__(name, marks)
        self.status = status

    def display(self):
        print(self.name, self.marks, self.status)

r = Result("Rida", 250, "Pass")
r.display()
# Rida 250 Pass