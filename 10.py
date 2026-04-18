# Check if a given element k is present in a list l or not

def obvious_search(l,k):
    for x in l:
        if x==k:
            return True
    return False

l=list(range(101))   
print(l)
b=int(input('Enter a number to search in the list: '))
print(obvious_search(l,b))