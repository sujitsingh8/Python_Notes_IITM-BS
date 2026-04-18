# recusion in python

def sum(a):
    if (a==1):
        return 1
    else:
        return a+sum(a-1) # Python lets you call the same function withion the function.

n=int(input('Enter a Number: '))
print('Sum of Numbers Till',n,'is',sum(n))