# Creating our own exceptions: User Defined Exceptions-

a=int(input('Enter your age: '))
if a<18:
    raise Exception('You are underage, can not vote!')

print('You are eligible to vote')