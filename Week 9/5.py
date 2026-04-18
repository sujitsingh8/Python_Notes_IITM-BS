# Big text file handling-

''' we have a text file of 231 mb which has phone numbers and
we want to find a particular phone number in this file: '''

# Some basics-
f=open('contacts.txt','r')
f.readline() # reads the first line
f.readline() # this reads the second line
f.readline() # this read the third line
f.close()