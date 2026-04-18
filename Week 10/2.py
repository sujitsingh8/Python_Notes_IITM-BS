''' Handling Exceptions: '''

a=int(input('Enter a Number: '))
b=int(input('Enter a Number: '))
try:
    c=a/b
    print(c)
    
# Division by zero Error
except ZeroDivisionError:
    print("Invalid input, divisor can not be zero")
    # If we will enter b=0 then output will be "Invalid input, divisor can not be zero"