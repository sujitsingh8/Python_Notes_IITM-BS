import random # It imports the 'random' library
print(random.random()) # prints random no. b/w 0 and 1 only, every time we excute it, it gives diff no.

# Let simulate a coin toss-
a=random.random() # It assigns random value b/w 0 and 1 to 'a'

if(a<0.5):
    print('Heads')
else:
    print('Tails')