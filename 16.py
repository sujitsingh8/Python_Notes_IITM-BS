# Indexing, Slicing and more on Strings:

s='coffee'
t='bread'

print(s[0]) # it prints 0th letter of the word coffee
# c
print(s[2]) 
# f
print(s[1:5]) # It prints the letter from 1st to the 4th position
# offe

#...........................................................................................................

l='0123456789'
a=l[4]
b=l[7]

print(a)
# 4
print(b)
# 7
print(a+b) # Here numbers are in string so it will not add them it will concatenate them
# 47

h='0123456789'
c=int(h[4]) # converted string to int
d=int(h[7]) # converted string to int
print(c+d)
# 11

i='0123456789'
k=int(i[3])
p=int(i[8])
n=k+p #11
print(n,"data type of",n,"is",type(n),"and the data type of",k,"and",p,"is",type(k),"and",type(p),"respectively")
# 11 data type of 11 is <class 'int'> and the data type of 3 and 8 is <class 'int'> and <class 'int'> respectively

k=i[3]
p=i[8]
n=k+p # 38
print(n,"data type of",n,"is",type(n),"and the data type of",k,"and",p,"is",type(k),"and",type(p),"respectively")
# 38 data type of 38 is <class 'str'> and the data type of 3 and 8 is <class 'str'> and <class 'str'> respectively