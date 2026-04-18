# Binary Search Implementation:

# Checking if a given element is present in agiven list l or not using binary search:

''' This function is an alternative to the obvious search. 
It is more efficient for searching, it works on only sorted lists '''

def binary_search(l,k):
    
    # shrink the list using while loop
    begin=0 # first element in the list, l[0]
    end=len(l)-1 # last element of list, l[len(l)-1]
    
    # use while loop at the list and keep halving it.
    while(end-begin>1):
        mid=(begin+end)//2 # compute the mid which is midpoint of begin to end
        if l[mid]==k: # if mid is indeed k, return True
            return True
        
        if l[mid]>k: # if the middle element is greater than k, then cut the right side and retain the left side
            end=mid-1
        if l[mid]<k: # if the middle element is less than k, then cut the left side and retain the right side
            begin=mid+1

    # we are outside the while loop now. This means condition in while loop is voilated or the length of list is less than or equal to 1

    # if end-begin is equal to 1, that means there are exactly two elements
    if l[begin]==k or l[end]==k:
        return True
    else:
        return False

l=list(range(10000001))
print(binary_search(l,int(input('Enter a Number to search: '))))