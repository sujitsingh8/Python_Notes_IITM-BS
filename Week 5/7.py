# Appending a list in the end

def list_appendend(l,z):
    new_list=[]
    for i in range(len(l)):
        new_list.append(l[i])
    for i in range(len(z)):
        new_list.append(z[i])
    return new_list
z=[5,4,6]
l=[7,8,9]
print(list_appendend(l,z))
# [7, 8, 9, 5, 4, 6]