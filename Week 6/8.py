''' Functional Programming (Part 3): '''

# Lambda functions-

# Python Lambda Functions are anonymous functions, meaning that the function is without a name.

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y

add=lambda x,y: x+y
sub=lambda x,y: x-y
mul=lambda x,y: x*y
div=lambda x,y: x/y

# Line 1 and 2 is similar to line 13, line 4 and 5 is similar to line 14 and so on

print(add(10,20))
# 30
print(sub(10,20))
# -10
print(mul(10,20))
# 200
print(div(10,20))
# 0.5