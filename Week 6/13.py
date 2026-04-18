# Approach 2: Menu driven code

import math

pi=math.pi
def circle_area(r):
    return(pi*r*r)

def circle_perimeter(r):
    return(2*pi*r)

def rectangle_area(l,b):
    return(l*b)

def rectangle_perimeter(l,b):
    return(2*(l+b))

polygon=''
while(polygon!='exit'):
    print('\nPOLYGONS\ncircle\nrectangle\nexit')
    polygon=input('\nChoose the polygon type or exit: ')
    property=''
    if(polygon=='circle'):
        r=float(input('\nEnter the radius of the circle: '))
        while(property==''):
            print('\nCIRCLE PROPERTIES\narea\nperimeter\nback')
            property=input('\nChoose the circle property or go back: ')
            if(property=='area'):
                cArea=circle_area(r)
                print(f'Area of circle with radius {r} = {cArea} sq. units')
                property=''
            elif(property=='perimeter'):
                cPerimeter=circle_perimeter(r)
                print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
                property=''
            elif(property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property=''
    elif(polygon=='rectangle'):
        l=float(input('\nEnter the length of the rectangle: '))
        b=float(input('\nEnter thr breadth of the rectangle: '))
        while(property==''):
            print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
            property=input('\nChoose the rectangle property or go back: ')
            if(property=='area'):
                rArea=rectangle_area(l,b)
                print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq. units')
                property=''
            elif(property=='perimeter'):
                rPerimeter=rectangle_perimeter(l,b)
                print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units')
                property=''
            elif(property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property=''
    elif(polygon=='exit'):
        break
    else:
        print('Please select the correct polygon type or exit')