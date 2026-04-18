# Factorial of a number uisng recursion

def fact(n):
    if (n==1):
        return 1
    else:
        return (fact(n-1)*n)

a=int(input('Enter a Number: '))
print('Fcatorial of',a,'is:',fact(a))