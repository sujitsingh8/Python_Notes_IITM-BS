# Inheritance and Method Overriding:

# Parent class
class Person:
    
    # Constructor to store name and age
    def __init__(self, name, age):
        self.name = name   # save name
        self.age = age     # save age
    
    # Method to print name and age
    def display(self):
        print(self.name, self.age)


# Student class is a child of Person
class Student(Person): # Child class 1
    
    # Constructor for Student
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # call Person constructor
        self.marks = marks           # save marks in Student class
    
    # This method replaces Person's display method
    def display(self):
        super().display()   # print name and age first by calling display method of Parent class
        print(self.marks)   # then print marks


# Employee class is also a child of Person
class Employee(Person): # Child class 2
    
    # Constructor for Employee
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # call Person constructor
        self.salary = salary         # save salary in Employee class
    
    # This method replaces Person's display method
    def display(self):
        print(self.name, self.age, self.salary)  # print all details from Employee class 
        # instead of calling printing from parent class


# Create Student object
s = Student('Rida', 20, 250)
s.display()   # show student details
# Rida 20
# 250

# Create Employee object
e = Employee('Harsh', 30, 50000)
e.display()   # show employee details
# Harsh 30 50000