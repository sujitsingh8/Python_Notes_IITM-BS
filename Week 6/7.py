# Generator-

def square(limit):
    x=0
    while x<limit:
        yield x*x
        yield x*x*x 
        x+=1
a=square(5)
print(next(a),next(a))
# 0 0
print(next(a),next(a))
# 1 1
print(next(a), next(a))
# 4 8

# Generator generates an iterator , here ‘a’ is an iterator.