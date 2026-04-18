# Reading writing to a file:

''' Code for Writing to a file- '''

f=open('mytext.txt','w') # it opens the text file in the writing mode and assign it to the variable 'f'
f.write("hey there it's me") # here we write in the file using the variable
f.close() # here we closed the file

# Output:
''' 
After running this code, a new file named mytext.txt will be created in the same folder
where our Python file is present.

The content of mytext.tx will be: 
hey there it's me '''