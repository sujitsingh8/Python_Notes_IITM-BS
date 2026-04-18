''' Sorting using functions: '''

# Obvious sort:
# Find the minimum element in the list l, append that element in the list x, remove that element in the list l

def obvious_sort(l):
    x=[]
    while len(l)>0:
        mini=l[0]
        for i in range(len(l)):
            if l[i]<mini:
                mini=l[i]
        x.append(mini)
        l.remove(mini)
    return x
l=[10,2,65,9,11]
print(obvious_sort(l))
# [2, 9, 10, 11, 65]

''' Another Way '''

def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini=l[i]
    return mini
def obvious_sort(l):
    x=[]
    while len(l)>0:
        mini=list_min(l) # we used list_min function to get the minimum element
        x.append(mini)
        l.remove(mini)
    return x
l=[3,78,65,43]
print(obvious_sort(l))
# [3, 43, 65, 78]