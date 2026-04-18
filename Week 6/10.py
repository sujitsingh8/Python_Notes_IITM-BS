# Filtering-

import math

a=[25,-16,9,81,-100]

def sqaure_root(n):
    return math.sqrt(n)

def is_positve(n):
    if n>=0:
        return n
    
c=map(sqaure_root,filter(is_positve,a))
print(list(c))
# [5.0, 3.0, 9.0]

# We want to write a list with sq. roots of the given list
# Since a given list may have negative numbers, we may get an error using library functions. 
# So we will use the filter function!