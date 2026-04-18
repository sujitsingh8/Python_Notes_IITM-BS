# Hybrid Inheritance
'''
Combination of two or more types of inheritance
(such as single, multiple, multilevel, hierarchical).
'''
''' In this example:
    - Hierarchical inheritance is used (Person → Student, Employee)
    - Multiple inheritance is used (Intern inherits from Student and Employee) '''

class Person: # Parent Class
    def show_person(self):
        print("This is Person")

class Student(Person): # Child class 1 for Person class, Parent class for Intern class
    def show_student(self):
        print("This is Student")

class Employee(Person): # Child class 2 for Person class, Parent class for Intern class
    def show_employee(self):
        print("This is Employee")

class Intern(Student, Employee): # Child class
    def show_intern(self):
        print("This is Intern")

i = Intern()
i.show_person()
# This is Person
i.show_student()
# This is Student
i.show_employee()
# This is Employee
i.show_intern()
# This is Intern

''' 
-> Is this example multilevel inheritance too?:
        -No, it is NOT multilevel inheritance.

Even though Student and Employee are both child and parent, the structure does not form a linear chain, which is compulsory for multilevel inheritance.
Multilevel inheritance must have a single straight line like this:
A → B → C

Our Hybrid example structure:
        Person
        /    \
   Student  Employee
        \    /
        Intern
'''