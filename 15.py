# Binary Search the Recursion Way

# Code of binary search using recursion:

def rbinarysearch(l,k,begin,end):
    
    ''' this will recursively compute binary search '''
    if begin==end:
        if l[begin]==k: # If begin and end are the same, then we ned to just check l[begin]
            return True
        return False
    
    if (end-begin)==1:
        if l[begin]==k or l[end]==k: # If begin and end are consecutive, then check them individually
            return True
        else:
            return False
        
    if (end-begin)>1:
        # Compute the middle element
        mid=(begin+end)//2
        if l[mid]>k:
            end=mid-1 # discard the right and retain the left
        if l[mid]<k:
            begin=mid+1 # discrad the left and retain the right
        if l[mid]==k:
            return True
        
    if (end-begin)<0:
        return False
    
    return rbinarysearch(l,k,begin,end)

l=list(range(1000))
end=len(l)-1
a=int(input('Enter a number to search: '))
print(rbinarysearch(l,a,0,end))