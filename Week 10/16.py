# Why in output it prints class?

i=int()
print(type(i))
# <class 'int'>

s=str()
print(type(s))
# <class 'str'>

l=list()
print(type(l))
# <class 'list'>

d=dict()
print(type(d))
# <class 'dict'>

''' This happens because in Python everything is an object, and every object is created from a class.

When we write:
    i = int()
we are calling the constructor of the int class to create an integer object.
So i is not “just a value” — it is an instance of the int class.

What type() actually returns?
The type() function returns the class to which an object belongs.

<class 'int'>  →  i is an object of class int
<class 'str'>  →  s is an object of class str
<class 'list'> →  l is an object of class list
<class 'dict'> →  d is an object of class dict '''