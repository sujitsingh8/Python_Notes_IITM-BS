# Appending a list in the beginning: 

def list_appendbefore(l,z):
    new_list=[]
    for i in range(len(z)):
        new_list.append(z[i])
    for i in range(len(l)):
        new_list.append(l[i])
    return new_list
z=[5,4,6]
l=[7,8,9]
print(list_appendbefore(l,z))
# [5, 4, 6, 7, 8, 9]