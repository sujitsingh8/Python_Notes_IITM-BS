# Some concepts about strings:

s='good'
print(s*4) # It concatenates the same string with itself for 4 times, 
           # we can multiply string and int but not string and string
# goodgoodgoodgood
print(s[0]*4) # It will print the letter at index 0 of the string for 4 times
# gggg

#...........................................................................................................

x='India'
print(x=='India')
# True
print(x=='india') # It will be false as the first letter is in lowercase
# False


print('apple'>'one')
# False
# When we use comparison operators with strings it works differently, it will compare the string
# character by character.
# Here, the first letter of 'apple' is 'a' which is being compared with the first letter 'o' of the word
# 'one' , As 'a' comes before ‘o’ ,  so it can not be greater than the letter 'o'. Hence, it gives the
# output as False.

print('abcdef'>'abcde')
# True
# In —>print('abcdef' < 'abcde') <—  Letter 'f' on the left side  has  no letter left on the right side to
# be compared with. Therefore, 'f' can not be smaller than nothing. Hence, It is false.

print('four'<'ten')
# True

#...........................................................................................................

p='python'

print(p[0])
# p
print(p[1])
# y
print(p[2])
# t
print(p[3])
# h
print(p[4])
# o
print(p[5])
# n

print(p[-1])
# n
print(p[-2])
# o
print(p[-3])
# h
print(p[-4])
# t
print(p[-5])
# y
print(p[-6])
# p

#...........................................................................................................

s='watertheplants'
print(len(s)) # 'len' is for length, it tells how many letters a string has.
# 14

# length starts from 1 but the index starts from 0
# The above string contains 14 letters that means the indexes are from 0-13