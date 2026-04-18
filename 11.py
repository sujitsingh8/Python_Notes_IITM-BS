import sys
l=[]
l1=[0]
l2=[1,0]
print(sys.getsizeof(l)) # it will print the size allocated to this list by computer
# 56
print(sys.getsizeof(l1)) # size will be greater than l as it has 1 element 
# 64
print(sys.getsizeof(l2)) # size will be greater than l1 as it has 2 elements
# 72

x= list(range(100))
s=set(range(100))
print('size of list', sys.getsizeof(x))
# size of list 856
print('size of set', sys.getsizeof(s))
# size of set 8408

print(x[0]) # lists work with indexes
# 0

# print(s[0]) # sets dont work with indexes


s={'sam','ram','joe'}
print(s)
# {'sam', 'ram', 'joe'}
print('sam' in s)
# True
s.add('sara') # it adds element in set
print(s)
# {'sara', 'sam', 'ram', 'joe'}