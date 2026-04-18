''' Types of finction arguments: '''

# Positional arguments: 

# All functions that we have seen so far have used positional arguments. Here, the position of an argument in the function call determines the parameter to which it is passed.

def add(a,b,c):
    return a+b-c

print(add(20,30,40)) # 20 is passed to a, 30 is passed to b, 40 is passes to c
# 10
print(add(30,20,60)) # 30 is passed to a, 20 is passed to b, 60 is passed to c
# -10

# Keyword arguments:

# Keyword arguments introduce more flexibility while passing arguments.
def add(a,b,c):
    return a+b-c
print(add(c=40,a=10,b=50)) # keyword
# 20
print(add(10,50,40)) # positional
# 20

# Default arguments:

# Parameters that are assigned a value in the function definition are called default parameters.
# An argument corresponding to a default parameter can be passed as a positional argument or as a keyword argument.
# Default parameters always come at the end of the parameter list in a function definition.

def add(c,a=20,b=30):
    return a+b-c

print(add(40)) # 40 is passed to c, a is 20 and b is 30
# 10
print(add(40,10)) # 40 is passed to c and 10 is passed to a,b is 30
# 0
print(add(40,10,50))
# 20
print(add(40,a=10,b=50)) # 40 is positional and a and b are keyword arguments
# 20