# Finding the maximum element in the list:

def list_max(l):
    maxi=l[0]
    for i in range(len(l)):
        if l[i]>maxi:
            maxi=l[i]
    return maxi
m=[1,65,45,32]
print(list_max(m))
# 65