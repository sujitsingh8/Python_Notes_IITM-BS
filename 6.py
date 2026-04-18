# What if we get an error which is not listed?

''' Handling Exceptions: '''

a=int(input('Enter a Number: '))
b=int(input('Enter a Number: '))
try:
    with open("sample.txt", "w") as f: # Created a file named sample.txt now if we run f=open('sample.txt','r') 
        # it will not show an error
        f.write('I created a txt file using python file handling.')
    f.close
    
    f=open('sample.txt','r') # Will not show an error
    
    c=a/b
    print(c)
    print(d)
except ZeroDivisionError:
    print("Invalid input, divisor can not be zero")
except NameError:
    print('Variable not defined') 
except FileNotFoundError:
    print("Invalid file name. Please check again")
except:
    print('Something went wrong')

finally:
    f.close()
    print('Finally block excuted!')

''' Here, line 17 throws an error, so anything after that will not execute, we open a file in line 13,
It remains open until we close it.
To close that we can use finally block which executes irrespective of whether there is an error or not. '''