# String Methods:

a='My name is Sujit Singh 123'

print(a.lower()) # Converts a string into lower case
# my name is sujit singh
print(a.upper()) # Converts a string into upper case
# MY NAME IS SUJIT SINGH
print(a.capitalize()) # Converts the first character to upper case
# My name is sujit singh
print(a.title()) # Converts the first character of each word to upper case
# My Name Is Sujit Singh
print(a.swapcase()) # Swaps cases, lower case becomes upper case and vice versa
# mY NAME IS sUJIT sINGH

print(a.islower()) # Returns True if all characters in the string are lower case
# False
print(a.isupper()) # Returns True if all characters in the string are Upper case
# False
print(a.istitle()) # Returns True if the string follows the rules of a title
# False
print(a.isdigit()) # Return True if all characters in the string are digits
# False

print(a.isalpha()) # Return True if all characters in the string are alphabets
# False 
# It would be true if it was a='abc', gaps are counted in alphabets

print(a.isalnum()) # Return True if all characters in the string are alpha-numeric
# False
# It would be true if it was a='abc123', gaps are counted in alphabets or numbers

#...........................................................................................................

del a
a='+++Hello World+++'

print(a.strip('+')) # Returns a trimmed version of the string
# Hello World
print(a.lstrip('+')) # Returns a left trim version of the string
# Hello World+++
print(a.rstrip('+')) # Returns a right trim version of the string
# +++Hello World

print(a.startswith('+')) # Returns True if the string starts with the specified value
# True
print(a.endswith('+')) # Returns True if the string ends with the specified value
# True

print(a.count('l')) # Returns the number of times a specified value occurs in a string
# 3
print(a.index('rl')) # Searches the string for a specified value and returns the position of where it was found
# 11
print(a.replace('d','d!')) # Returns a string where a specified value is replaced with a specified value
# +++Hello World!+++