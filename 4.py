''' Handling Exceptions: '''

a=int(input('Enter a Number: '))
b=int(input('Enter a Number: '))
try:
    c=a/b
    print(c)
    # print(d)
    f=open('abc.txt','r')
except ZeroDivisionError:
    print("Invalid input, divisor can not be zero")
except NameError:
    print('Variable not defined')

# File not found
except FileNotFoundError:
    print("Invalid file name. Please check again")
    # There is a File not found error in the code- f=open('abc.txt','r')
    # The statement 'Inavlid file name. Please check again' will be shown only 
    # if there will be no error above f=open('abc.txt','r')