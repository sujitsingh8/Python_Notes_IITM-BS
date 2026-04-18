# Single Inheritance
'''
One child class inherits from one parent class.
Parent class  →  Child class
'''

class Person: # Parent class
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person): # Child class
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        super().display()
        print("Marks:", self.marks)

s = Student("Rida", 250)
s.display()
# Name: Rida
# Marks: 250