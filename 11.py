# How much time does it take to find an element using obvious sort?

def obvious_search(l,k):
    for x in l:
        if x==k:
            return True
    return False

l=list(range(100000))   
print(l)
b=int(input('Enter a number to search in the list: '))

import time
time.time() # returns the time as a floating point number expressed in seconds since the epach,in UTC

a=time.time()
print(obvious_search(l,b))
c=time.time()
print(c-a) # it returns the diffrence of the time before execution of obvious_search and after execution