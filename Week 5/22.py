''' More on sets: '''

s={1,2,3,4,5,1,2,3,4,5} # set donot allow duplicity
print(s)
# {1, 2, 3, 4, 5}

# Set is an unordered entity; we can not say that 1 is at zeroth index or is the first element in the set.

# Set itself is mutable but values inside set have to be immutable and hashable , hence, we can
# not add a dictionary or list or tuple containing a list or dict to a set.

''' Set methods- '''

a={1,3,5,6}
b={1,2,3,4,5}
print(a.issubset(b))
# False
print(a.issuperset(b))
# False
print(b.issuperset(a))
# False

c=a.union(b)
d=a|b # operator for union
print(c,d)
# {1, 2, 3, 4, 5, 6} {1, 2, 3, 4, 5, 6}

e=a.intersection(b)
f=a&b
print(e,f)
# {1, 3, 5} {1, 3, 5}

g=a.difference(b)
h=a-b
print(g,h)
# {6} {6}