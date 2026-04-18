# More examples on finction:

def list_min(l):
    mini=l[0]
    for i in range (len(l)):
        if l[i]<mini:
            mini=l[i]
    return mini

x=[1,45,67,-10,9]
print(list_min(x))
# -10