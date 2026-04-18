''' Lists and Sets: '''

l=list(range(10))
print(l)

l.append('hey')
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'hey']

print(5 in l) # it will be true, in operator can be used in lists
# True
print('hey' in l)
# True

l[3]=100 # chnages the element at third place to 100, this can not happen in sets
print(l)
# [0, 1, 2, 100, 4, 5, 6, 7, 8, 9, 'hey']

l=list(range(100000))
print(l[len(l)-1]) # prints the last element in the list
#99999
print(l[9876])
# 9876
print('hey' in l) # this will take so much time to search for hey in the list as it will go through the entire list and search
# False

# is there a way in whuch we can quickly search?
l=[1,2,3,1]
s={1,2,3,1} # it is a set, by default it is sorted and does not repeat element
print(type(l))
# <class 'list'>
print(type(s))
# <class 'set'>
print(l)
# [1, 2, 3, 1]
print(s)
# {1, 2, 3}
print(1 in s) # in work with sets also
# True

''' Lists take longer time than Sets to search for elements in it. '''