# Approach 2: Using slope of lines connecting two points

import math

def slope(xi,yi,xj,yj):
    if(xi==xj):
        return(math.inf)
    else:
        return((yj-yi)/(xj-xi))
    
x1=float(input('Enter x coordinate of 1st point: '))
y1=float(input('Enter y coordinate of 1st point: '))
x2=float(input('\nEnter x coordinate of 2nd point: '))
y2=float(input('Enter y coordinate of 2nd point: '))
x3=float(input('\nEnter x coordinate of 3rd point: '))
y3=float(input('Enter y coordinate of 3rd point: '))
s1=slope(x1,y1,x2,y2)
print(f'\nSlope of the line connecting points ({x1}, {y1}) and ({x2}, {y2}) = {s1}')
s2=slope(x2,y2,x3,y3)
print('\nSlope of the line connecting points ({x2}, {y2}) and ({x3}, {y3}) = {s2}')
if(s1!=s2):
    print('\nTriangle')
else:
    print('\nNot a triangle')