# Caesar Cipher:

''' Suppose there is a file in which there is a paragraph written, 
we want to encrypt that file in such a way that each letter in that file shifts by 3 letters 
(a becomes d, g becomes j, z becomes c and so on) '''

import string

def create_caeser_dict():
    l=string.ascii_lowercase # Get all lowercase English letters: 'a' to 'z'
    l=list(l) # Convert string to list so we can access by index
    d={} # set to store letters after shifted
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26] # Shift each letter to the letter 3 positions ahead, %26 ensures wrap-around (z->c)
    return d

f=open('file.txt','r') # text file that contains the paragraph
g=open('encrypted.txt','w') # the encrypted file which we will create

d=create_caeser_dict()
c=f.read(1) # read 1 character at a time
while(c!=''):
    g.write(d[c])
    c=f.read(1) # read next character

f.close()
g.close()