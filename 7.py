# Code to check if a given list has 0 in it or not.
# If it has zero in it, return True, otherwise False

def check0(l):
    if len(l) == 0:
        return False
    if l[0] == 0:
        return True
    else:
        return check0(l[1:len(l)])


# Take input from user
n = int(input("Enter number of elements: "))
lst = []

print("Enter elements:")
for i in range(n):
    lst.append(int(input()))

ans = check0(lst)
print(ans)