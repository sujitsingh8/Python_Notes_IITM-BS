''' Functional Programming (Part 2): '''

# Iterator-
fruits=['mango','apple', 'banana','orange','pineapple','watermelon','guava','kiwi']

bascket=iter(fruits)
print(next(bascket))
# mango
print(next(bascket))
# apple
print(next(bascket))
# banana

# Suppose we want to distribute fruits to kids we come across one by one.
# For this we can use an iterator which converts the iterable list into an iterator 
# and executes using the ‘next’ function or gives the next output when we want. 