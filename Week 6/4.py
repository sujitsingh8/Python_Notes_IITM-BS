''' Scope of a variable: '''

# The region in the code where a name can be referenced is called its scope. If we try to reference a variable outside its scope, 
# the interpreter will throw a NameError.

# Local vs Global:

def func():
    x=1
    print(f'This x is local for function func, x=x{x}')
func()
# This x is local for function func, x=x1
# print(x) # This will throw an error


# In the above example, the scope of the name x is local to the function; x has a meaningful existence only inside the function 
# and any attempt to access it from outside the function is going to result in an error

def func():
    x=1
    print(f'This x is local for function func, x={x}')
func()
# This x is local for function func, x=1

y=10
def func():
    x=1
    print('I can access both x and y')
    print(f'x={x},y={y}')
func()
# I can access both x and y
# x=1,y=10

# The name y is accessible from within the function as well. We say that the scope of y is global. That is, it can be referenced from anywhere within the program — even inside a 
# function — after it has been defined for the first time.