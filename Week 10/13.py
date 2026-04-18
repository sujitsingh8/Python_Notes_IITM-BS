''' Attributes and Methods '''

class Student:
    def __init__(self,roll_no,name): # self stores s0,s1
        self.roll_no=roll_no # here it means s1.roll_no or s0.roll_no
        self.name=name
    
    def display(self):
        print(self.roll_no,self.name)
    
s0=Student(0,'Sujit')
s0.display()
# 0 Sujit

s1=Student(1,'Harshit')
s1.display()
# 1 Harshit

''' roll_no and name are the variables inside the init function and they belong to individual objects like s0 and s1.
They are object attributes.

The __init__ function is called every time and object is created from a class.
The __init__ method lets the class initialize the object's attributes and serves no other purpose.
It is only us within classes.

SELF represents the instance of class. 
This handy keyword allows you to access variables, attributes, and methods of a defines class in Pyhon '''