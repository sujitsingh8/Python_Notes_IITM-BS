''' Reading in a file: '''

g=open('mytext.txt','r') # it opens the text file in read mode
h=g.read() # it reads the data in the file
print(h)
g.close()
''' 
l=g.read() it will show an error as we have closed the file
'''

# It prints the content written in the file:
# hey there it's me

''' If you update something manually in the text file and come back to the terminal and rewrite the
commands to read the same file, it will show the updated data! '''