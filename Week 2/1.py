# More on Variables, Operators and Expressions :


# In Python, there are some words like and, or, not, if, else, for, while,... which are referred
# to as 'Keywords'.
# We can not use these keywords as variable names

#...........................................................................................................

# Rules for writing variable names :
# 1. Variable names can contain alphanumeric (all alphabets from A-Z in lower and
# uppercase and numbers 0-9) characters and underscores.
# 2. We can start a variable name with an alphabet or an underscore but we cannot
# start it with a number.
# 3. Variable names are case sensitive

roll=5
ROLL=10
Roll=15
print(roll,ROLL,Roll)
# 5 10 15

# Even though the spellings are the same, the computer treats all three variables as
# unique variables. This shows that in Python variable names are case sensitive

#...........................................................................................................

# Multiple Assignment:

x,y=1,2
print("Value of x is",x)
# Value of x is 1
print("Value of y is",y)
# Value of y is 2

# Note that the order matters. The following code assigns 1 to the variable x and 2 to the variable y

#...........................................................................................................

x=y=z=1
print(x,y,z)
# 1 1 1

#...........................................................................................................

# Swapping the values of the variables:

x,y=1,2
x,y=y,x # it swaps the values of x and y
print(x,y)
# 2 1

#...........................................................................................................

x=5
print(x)
# 5
del x
# print(x)
# error

#...........................................................................................................

# Shorthand Operators:

z=0
z+=1 # we read this as (z equals to z plus 1)
z+=1
z+=1
z+=1
print(z)
# 4

a=2
a*=2 # it is similar to (a=a*2)
print(a)
# 4

#...........................................................................................................

# in Operator:

print('alpha' in 'we can use alpha-numeric characters.')
# True
print('alpha' in 'We can usd letters and numeric.')
# False

#...........................................................................................................

# Chaining operators:

x=5
print(1<x<10)
# True
print(10<x<20)
# False
print(x<10<x*10<100)
# True
print(10>x<=9)
# True
print(5==x>4)
# True