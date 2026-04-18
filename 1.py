''' Introduction to functions: '''

# a function which prints addition of two numbers
def add(a, b):
    ans = a + b
    print(ans)

add(10,12)
# 22

''' If we run the block [1] code, we will not get any output. Functions are not executed
unless they are called. '''

''' add(10,12) is a function call, and
10,12 are the values that are passed to the function in the call and are known as
arguments. '''

''' a,b are the parameters. '''

# add(10,12)+10
''' Here we wanted to add 10 and 12 first and then add 10 to it.
Why couldnot we do it?'''

def add(a,b):
    ans = a+b
    return ans
add(10,12)+10
# 22
c=add(10,12)+10
print(c)
# 32

''' Earlier we used print(ans) but now we used return ans
Return statement simply returns the values as output whereas the print() function simply
prints the value. '''