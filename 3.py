# How to write in next line:

s=open('newtext.txt','w')
s.write('first line')
s.write('\n')
s.write('second line')
s.write('\n')
s.write('third line')
s.close()

s=open('newtext.txt','r')
l=s.read()
print(l)
# first line
# second line
# third line
s.close()