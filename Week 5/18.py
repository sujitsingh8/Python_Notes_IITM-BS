''' More on tuples: '''

# Tuples are immutable.
t=1,2,3 # we are packing these values to as single entity called tuple
print(t,type(t))
# (1, 2, 3) <class 'tuple'>

x,y,z=t # here we are unpacking this tuple into three independent integer values
print(x,y,z)
# 1 2 3

x=5
y=10
x,y=y,x # python is packing y,x into tuple and then unpacking it on the left hand side
print(x,y)
# 10 5

t=(10) # when we give a single value in the small brackets python considers it as a single value and not a tuple
print(t,type(t))
# 10 <class 'int'>

t=(10,) # we have to add a comma to create a tuple
print(t,type(t))
# (10,) <class 'tuple'>

t=([1,2],['a','b'])
# t[0]=[10,20] # we can not modify a tuple
t[0][1]=10 # but if the value inside a tuple is multiple we can modify that value
print(t)
# ([1, 10], ['a', 'b'])


''' Hashable: '''

t1=(1,2,3) # if the values inside a tuple are also imutable then tuple is considered as hashable
t2=([1,2,3]) # if the values inside a tuple are mutable then tuple is considered to be non-hashable
t2[0]=0
print(t2)
# [0, 2, 3]