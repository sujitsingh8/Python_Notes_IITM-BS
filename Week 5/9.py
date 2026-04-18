''' Matrix Multiplication using functions: '''

# initialize c matrix to 0

def intialize_mat(dim):
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c

# consider two matrices a and b
# dot product of two lists

def dot_product(u,v):
    dim=len(u)
    ans=0
    for i in range(dim):
        ans += u[i]*v[i]
    return ans

# pick the ith row and jth column

def row(m,i):
    dim=len(m)
    l=[]
    for k in range(dim):
        l.append(m[i][k])
    return l
def column(m,j):
    l=[]
    dim=len(m)
    for k in range(dim):
        l.append(m[k][j])
    return l

# Matrix multiplication

def mat_mul(a,b):
    dim=len(a)
    c=intialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(a,i),column(b,j))
    return c

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,1],[3,1,7],[6,2,3]]

print(mat_mul(a,b))
# [[25, 10, 24], [55, 25, 57], [85, 40, 90]]