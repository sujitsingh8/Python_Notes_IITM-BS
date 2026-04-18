''' Tuples: '''

t=(1,2,3,1,5,4,5)
print(t)
# (1, 2, 3, 1, 5, 4, 5)

# in list we can append copy remove but in tuples we can not

# t.append(12) # this will not work
# t.remove(4) # this will not work 

print(t[0]) # tuples are like strings
# 1

''' Tuples are like strings we can use indexing and slicing in tuples. '''

l=list(range(10)) # flexible
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t=tuple(range(10)) # not flexible (sometime you dont want to change things)
print(t)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# In lists we can update the values but once a tuple is created we can not change its values.