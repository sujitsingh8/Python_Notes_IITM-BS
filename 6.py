''' The actual code to find the number- '''

# Open the file 'contacts.txt' in read mode
f=open('contacts.txt','r')
flag=0

# Initialize s with a non-empty value so that while loop starts
s='0'

# Loop will run until end of file is reached, readline() returns empty string '' at End of File
while(s!=''):
    s=f.readline()
    if (s!=''):
        n=int(s)
        if n==9254019460:
            print('the number was found')
            flag=1
            break
if flag==0:
    print('the number was not found')