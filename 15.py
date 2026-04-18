''' Attributes and Methods '''

class Student:
    def __init__(self,roll_no,name,total):
        self.roll_no=roll_no
        self.name=name
        self.total=total
        
    def display(self):
        print(self.roll_no,self.name,self.total)
        
    def result(self):
        if self.total>120:
            print('Pass')
        else:
            print('Fail')

s0=Student(0,'Sujit',100)
s0.display()
# 0 Sujit
s0.result()
# Fail

s1=Student(1,'Harshit',150)
s1.display()
# 1 Harshit
s1.result()
# Pass

''' Method 'result' in line 11 is a behavior.

In Object-Oriented Programming (OOP), behaviour means what an object can do.

What is Behaviour?
    Behaviour = actions or operations performed by an object
    In Python, behaviours are defined using methods (functions inside a class)

So:
    Data / Properties → stored using variables
    Behaviour → defined using methods

Data (Attributes)
    These store information about a student:
        roll_no
        name
        total

Behaviour (Methods)
    These define actions a student can perform:
        display() → shows student details
        result() → checks pass or fail

Why is result() called a behaviour?
Because:
    It acts on the data (self.total)
    It decides something (Pass / Fail)
    It represents an action, not information '''