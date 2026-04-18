# Multiple Inheritance
'''
One child class inherits from more than one parent class.
Parent class 1 + Parent class 2  →  Child class
'''

class Student: # Parent class 1
    def __init__(self, marks):
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)

class Employee: # Parent class 2
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print("Salary:", self.salary)

class PersonDetails(Student, Employee): # Child class
    def __init__(self, marks, salary):
        Student.__init__(self, marks)
        Employee.__init__(self, salary)

    def display(self):
        self.show_marks()
        self.show_salary()

p = PersonDetails(250, 50000)
p.display()
# Marks: 250
# Salary: 50000