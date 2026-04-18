''' Handling Exceptions: '''

a=int(input('Enter a Number: '))
b=int(input('Enter a Number: '))
try:
    c=a/b
    print(c)
    print(d)
except ZeroDivisionError:
    print("Invalid input, divisor can not be zero")
    
# Name Error
except NameError:
    print('Variable not defined')
    # There is a Name Error in the code- print(d) as variable d is not defined 
    # The statement 'Variable not defined' will be shown only if there will be no error above print(d)