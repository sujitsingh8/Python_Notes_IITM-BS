# Why is searching using binary search more efficiebt than obvious sort?

import time

def binary_search(l,k):
    begin=0 
    end=len(l)-1
    while(end-begin>1):
        mid=(begin+end)//2 
        if l[mid]==k:
            return True   
        if l[mid]>k:
            end=mid-1
        if l[mid]<k: 
            begin=mid+1
    if l[begin]==k or l[end]==k:
        return True
    else:
        return False
    
def obvious_search(l,k):
    for x in l:
        if x==k:
            return True
    return False

l=list(range(1000000001))

a=time.time()
print(obvious_search(l,999999999))
b=time.time()

c=time.time()
print(binary_search(l,999999999))
d=time.time()

print('Binary Search Timing=',d-c)
print('Obvious Search Timing=',b-a)

''' Obvious search took nearly 113.8521499633789 seconds to search whereas searching was done in almost 0 seconds using binary search.

In obvious search, it goes through the entire list.
In binary search, it uses the principle of halving the list. '''