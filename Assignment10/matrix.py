import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    r1, c1 = a.shape
    r2, c2 = b.shape
    x = (r1, c2)
    y = np.zeros(x)
    for i in range(0,len(a)):
        for j in range(0, len(b[0])):
            Product = 0
            for k in range(0, len(b)):
                Product += a[i, k] * b[k, j]
            y[i][j] += Product
    return y


#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    r1, c1 = a.shape
    x = (r1, c1)
    y = np.zeros(x)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            y[i][j] += n * a[i][j]
    return y


#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    r1, c1 = a.shape
    x = (c1, r1)
    y = np.zeros(x)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            y[j][i] = a[i][j]
    return y

#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    r1, c1 = a.shape
    r2, c2 = b.shape
    x = (r1, c2)
    y = np.zeros(x)
    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            Sum = 0
            for k in range(0, len(b)):
                Sum = a[i, j] + b[i,j]
            y[i][j] = Sum
    return y


if __name__ == "__main__":
    a = np.array([[1,2,4],[3,4,3]])
    b = np.array([[-1,0],[1,-5],[-3,1]])

    print("numpy product\n", np.dot(a,b))
    d = mm(a,b)
    print(d)

    print("numpy scalar product\n", 4*a)
    e = sm(4,a)
    print(e)

    print("numpy tranpose\n", np.transpose(a))
    f = tp(a)
    print(f)

    print("numpy addition\n", a + a)
    g = add_m(a,a)
    print(g)