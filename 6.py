# Code to check if a given list has 0 in it or not.
# If it has 'zero in it, we return True, otherwise we return False

# We have to write a code of a recursive function which will return false if 0 is not present in the list and return true if it is present.

def check0(l):
    if (len(l)==0):
        return 0 #  If the list is empty, return False
    if (l[0]==0):
        return True # If the first element is zero then return True
    else:
        return check0(l[1:len(l)]) # l[1:len(l)] means check from 2nd element in the list
    # the above code simply outsources.
    
ans=(check0([1,2,3,0,24,56,87,5,3]))
print(ans)