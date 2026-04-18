def sum(a):
    ans=0
    for i in range(a):
        ans=ans+(i+1)
    return ans

n=int(input('Enter a Number: '))
print('Sum of numbers till',n,'is',sum(n))