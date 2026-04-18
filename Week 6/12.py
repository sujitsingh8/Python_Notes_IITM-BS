# Write a python code using functions to calculate area and perimeter of circle and rectangle

# Approach 1: Standard code
pi=22/7
def circle_area(r):
    return(pi*r*r)

def circle_perimeter(r):
    return(2*pi*r)

def rectangle_area(l,b):
    return(l*b)

def rectangle_perimeter(l,b):
    return(2*(l+b))

r=float(input('\nEnter the radius of the circle: '))
cArea=circle_area(r)
print(f'\nArea of circle with radius {r} = {cArea} sq. units')
cPerimeter=circle_perimeter(r)
print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
b=float(input('\nEnter thr breadth of the rectangle: '))
l=float(input('\nEnter the length of the rectangle: '))
rArea=rectangle_area(l,b)
print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq. units')
rPerimeter=rectangle_perimeter(l,b)
print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units')