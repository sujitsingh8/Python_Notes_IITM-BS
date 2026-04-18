''' Functional Programming (Part 1): '''

# Inline statements-

# If-else-
a=100
b=20
'''
if a<b:
    small=a
else:
    small=b
'''
small=a if a<b else b
print(small)
# 20

# While-
a=5
while a>0:
    print(a); a-=1
    # 5
    # 4
    # 3
    # 2
    # 1