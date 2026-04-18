# Let’s write a program  to remove all the unwanted symbols from the string:

import string
s=string.ascii_letters # it creates a string of lower and uper case letters
s=set(s) # converting that string to a set
alpha=tuple(s) # converting that string to a tuple

x='heytherewassup(){}#@4india' # Assuming it as the input string
l=list(x)
r=[]

for p in l:
    if p in alpha: # alpha is fixed, when you want something to be fixed we use tuples
        r.append(p)
print(r)
# ['h', 'e', 'y', 't', 'h', 'e', 'r', 'e', 'w', 'a', 's', 's', 'u', 'p', 'i', 'n', 'd', 'i', 'a']

# Tuples have less size than lists.