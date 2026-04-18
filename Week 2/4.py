# Caesar-Cipher: More on strings

# It adss a key to the string and prints the encrypted string as the output-

alpha='abcdefghijklmnopqrstuvwxyz'
s='india'

t=''

i=0
k=27
t+=(alpha[(((alpha.index(s[i]))+k)%26)])
t+=(alpha[(((alpha.index(s[i+1]))+k)%26)])
t+=(alpha[(((alpha.index(s[i+2]))+k)%26)])
t+=(alpha[(((alpha.index(s[i+3]))+k)%26)])
t+=(alpha[(((alpha.index(s[i+4]))+k)%26)])

print('original string:',s)
# india
print('encrypted string:',t)
# joejb