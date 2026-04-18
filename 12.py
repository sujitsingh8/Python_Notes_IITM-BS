# Coversion of one data type to another (Type conversion or Type casting)

a=int(4.5) # converts float to int
b=int('10') # converts str to int, but we cannot convert "sujit" or any other characters to int
print(a,type(a))
# 4 <class 'int'>
print(b,type(b))
# 10 <class 'int'>

c=float(5) # converts int to float
d=float('10') # converts str to float
print(c,type(c))
# 5.0 <class 'float'>
print(d,type(d))
# 10.0 <class 'float'>

#...........................................................................................................

# Convert int to boolean:
e=bool(10)
print(e,type(e))
# True <class 'bool'>
f=bool(0)
print(f,type(f))
# False <class 'bool'>
g=bool(-10)
print(g,type(g))
# True <class 'bool'>

# The variable f is false because when computers convert integers into boolena every integer 
# except 0 is considered as true, 0 is the only value which gives a boolean value as false.

#...........................................................................................................

# Convert str to boolean:
h=bool('Hehe')
print(h,type(h))
# True <class 'bool'>
i=bool('10')
print(i,type(i))
# True <class 'bool'>
j=bool("10.5")
print(j,type(j))
# True <class 'bool'>
k=bool('0')
print(k,type(k))
# True <class 'bool'>

# Here, the variable k is true because the zero in variable k is neither integer nor float. 
# It is a string and string representation of boolean is always true except one condition: 
# if the string is empty the boolean representation of empty string will be false

l=bool('')
print(l,type(l))
# False <class 'bool'>

#...........................................................................................................

m=str(10) # converts int to str
print(m,type(m))
# 10 <class 'str'>
n=str(10.0) # converts float to str
print(n,type(n))
# 10.0 <class 'str'>
o=str(True) # converts bool to str
print(o,type(o))
# True <class 'str'>