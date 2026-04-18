''' More on lists: '''

# Operations on lists:

# Addition:

l1=[1,2,3]
l2=[10,20,30]
l12=l1+l2 # it will print the list with the elements of l1 followed by l2
l21=l2+l1 # it will print the list with the elements of l2 followed by l1
print(l12,l21)
# [1, 2, 3, 10, 20, 30] [10, 20, 30, 1, 2, 3]

# Replication:

l=[0] *10
print(l)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l3=[1,2,3]*5
print(l3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# Logical operators:

l1=[1,2,3]
l2=[10,20,30]
print(l1==l2)
# False
print(l1==[1,2,3])
# True

print([1,2]<[2,1]) # it compared 1st element of 1st list with first element of second list
# True
print([1]<[1,2,3]) # in this 1 of l1 is equal to 1 of l2 amd l1 has no other element to be compared so it is true
# True
print([2,3]<[3]) # 2 is less than 3
# True
print([]<[1]) # empty list is less than every list
# True

# Mutability:
l=[1,2,3]
print(l)
# [1, 2, 3]
l[2]=9 # python allows us to change values in place hence list is mutable
print(l)
# [1, 2, 9]

# Integers are immutable
x=5
y=x
x=10
print(x,y)
# 10 5
# This is how we change the values of integer variables.

#...........................................................................................................

l1=[1,2,3]
l2=l1 # instead of creating a new memory location, computer simply adds one more name to the same memory location
l1[0]=100
print(l1)
# [100, 2, 3]
print(l2)
# [100, 2, 3]

#...........................................................................................................

''' How to create a seperate copy? '''
# There are three ways-

l1=[1,2,3]
l2=list(l1) # 1st way
l3=l1[:] # 2nd
l4=l1.copy() # 3rd

l2[0]=100
l3[1]=200
l4[2]=300

print(l1,l2,l3,l4)
# [1, 2, 3] [100, 2, 3] [1, 200, 3] [1, 2, 300]

#...........................................................................................................

''' How do we know if two lists have the same memory location? '''

l5=l1
print(l1 is l2)
# False
print(l1 is l3)
# False
print(l1 is l4)
# False
print(l1 is l5) # l1 and l5 have same memory location
# True

#...........................................................................................................

''' if function type is mutable it is called by reference otherwise it is called by value'''

def add(x):
    x+=1 # local
    return x
x=5 # global
print(add(x)) # local x has value 6
# 6
print(x) # global x has value 5
# 5

def add(x):
    x.append(1)
    return x

x=[5]
print(add(x)) # we are not passing the value of x we are passing the whole list
# [5, 1]
print(x)
# [5, 1]

#...........................................................................................................

''' List methods: '''

#append()(inserts the element in the last)
#remove()(this will remove element from list)

l=[1,2,3]
l1=l.copy()

# similar to append
l.insert(2,9) # inserts 9 at 2nd index
print(l)
# [1, 2, 9, 3]
l.pop(0) # removes element at zeroth index
print(l)
# [2, 9, 3]

l=[1,6,78,43]
l.sort(reverse=True) # sorts in descending
print(l)
# [78, 43, 6, 1]
l.sort()
print(l) # sorts in ascending
# [1, 6, 43, 78]
l.reverse() # reverses the list
print(l)
# [78, 43, 6, 1]