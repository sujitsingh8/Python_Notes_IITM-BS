# OOP:

# Classes and Objects-
''' Object-> combination of attributes(variables) and behaviour (function), 
must have its own identity (own set of variables and functions).

Class->blueprint of the object '''

# How do we create a class and object?

class Student: # 1st letter always Capital
    roll_no = None
    name = None
    # now we can create as many objects as we want, each object will have diff variables i.e roll_no and name

s0 = Student() # object is created, # constructor
s0.roll_no = 0
s0.name = 'Sujit'
# object name, dot operator, variable name
print(s0.name,s0.roll_no)
# Sujit 0

s1 = Student()
print(s1.name,s1.roll_no)
# None None

s2 = Student()
s2.roll_no = 2
s2.name = 'Harshit'
print(s2.name,s2.roll_no)
# Harshit 2

s50 = Student()
s50.name = 'Saloni'
print(s50.name,s50.roll_no)
# Saloni None

''' This is not the efficient way of writing code for classes and objects! '''