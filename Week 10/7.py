# What if an exception occurs in the finally block?

try:
    print(d)
except NameError:
    print('Variable d is not defined in try block')
    # This will run

finally:
    try:
        print(d)
    except NameError:
        print('Variable d is not defined in finally block')
        # This will run
        
'''
finally:
    print(d)
    ''' 
    # It will show an error