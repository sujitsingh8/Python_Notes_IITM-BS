# Sorting

def mini(l): # Find the minimum element in the list l
    m=l[0]
    for x in l:
        if (x<m):
            m=x
    return m

def sort(l): # recursively sort the list l
    if len(l)==0:
        return []
    m=mini(l) # find minimum number in l every time the sort function will run
    l.remove(m) # removes minimum number from list l
    return [m]+sort(l) # append that minimum number in list m in ascending order

# Take input from user
n = int(input("Enter number of elements: "))
lst = []

print("Enter elements:")
for i in range(n):
    lst.append(int(input()))
    
print('List:',lst)
print('After sorting:',sort(lst))