# Using a function with input statements-

def discount(cost,d):
    ans=cost-(cost*(d/100))
    return ans
c=int(input('Enter the cost price: '))
disc=int(input('Enter the discount: '))

print('Discount is :', discount(c,disc))