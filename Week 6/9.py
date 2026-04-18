# Enumerate-
fruits=['mango','apple','banana','orange','pineapple','watermelon','guava','kiwi']

for fruit in enumerate(fruits):
    print(fruit)
    # (0, 'mango')
    # (1, 'apple')
    # (2, 'banana')
    # (3, 'orange')
    # (4, 'pineapple')
    # (5, 'watermelon')
    # (6, 'guava')
    # (7, 'kiwi')

# We want to group values from two different lists (zip)-
size=[5,5,6,6,9,10,5,4]
print(list(zip(fruits,size)))
# [('mango', 5), ('apple', 5), ('banana', 6), ('orange', 6), ('pineapple', 9), ('watermelon', 10), ('guava', 5), ('kiwi', 4)]

# The list Fruits is coupled with the list size.

#...........................................................................................................

# Creating third list using previous two (map)-
a=[10,20,30,40,50,60]
b=[6,19,12,25,29,37]

def sub(x,y):
    return x-y

c=map(sub,a,b)
print(list(c))
# [4, 1, 18, 15, 21, 23]

# It maps the function with the parameters passed.