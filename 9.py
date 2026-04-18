# File handling, Genetic Sequences:

''' Using seek and read on 'text.txt'- '''

f=open('text.txt','r')
s=f.read(2) # it will read first 2 characters
print(s)
# 01
s=f.read(2) # it will read next 2 characters
print(s)
# 23
s=f.read(2) # it will read next 2 characters after 23
print(s)
# 45

s=f.seek(2) # it goes at the 2nd position, it is at '1' we can use seek to go to any position

s=f.read(2) # after '1' the next two are 23
print(s) # prints 23 and not 67, coz it was shifted to 4th position
# 23