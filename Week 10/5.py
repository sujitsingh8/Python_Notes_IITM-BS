# What if we get an error which is not listed?

''' Handling Exceptions: '''

a=int(input('Enter a Number: '))
b=int(input('Enter a Number: '))
try:
    c=a/b
    print(c)
    # print(d)
    # f=open('abc.txt','r')
except ZeroDivisionError:
    print("Invalid input, divisor can not be zero")
except NameError:
    print('Variable not defined') 
except FileNotFoundError:
    print("Invalid file name. Please check again")
    
except:
    print('Something went wrong')
    # We can write a common exception handling block!