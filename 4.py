# Compute compund intrest by assuming the intrest to be 10%

def comp(p,n):
    if (n==1):
        return p*(1.1)
    else:
        return comp(p,n-1)*1.1
    
a=int(input('Enter principle amount: '))
b=int(input('Enter years: '))
print('Total amount to be paid after',b,'years:',comp(a,b))

# 2000*1.1 = 2200.0
# 2000*1.1*1.1 = 2420.0
# 2000*1.1*1.1*1.1 = 2662.0