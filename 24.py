# using user-defined modules and object-oriented programming (OOP) in Python.

''' Importing Student class from Student.py file '''
from Student import Student
''' Importing Employee class from Employee.py file '''
from Employee import Employee

s = Student('Rida', 20, 250)
s.display()
# Rida 20
# 250

e = Employee('Harsh', 30, 50000)
e.display()
# Harsh 30 50000