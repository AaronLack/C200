import numpy as np

# a = np.arange(10)
# print(a)
# print(a.size)
# # Outputs [0 1 2 3 4 5 6 7 8 9], with a size #10

# a = np.arange(10)
# print(a)
# print(a.size)
# print("The shape of a {0}".format(a.shape[0]))

# a = np.arange(15).reshape(5,3)
# print(a)

# rows = a.shape[0]
# columns = a.shape[1]

# for i in range(0,rows):
#     for j in range(0,columns):
#         print("a[{0}][{1}]={2}".format(i,j,a[i][j]), end ="")
#     print()

# a = np.arange(15).reshape(3,5)
# print(a)
# a = np.arange(15).reshape(5,3)
# print(a)
# print(a.shape)
# print(a[0])
# print(a[:,0]) #Slicing

# a = np.arange(12).reshape(3,4)
# print(a)

# b = a.sum(axis=0)
# c = a.sum(axis=1)
# print(b)
# print(c)
#Adds up all the columns together

# np.random.seed(0) # reproduce "random"

# a = np.random.randint(9, size=(3,2,4))
# print(a)
# print("Dimensions={0}".format(a.ndim))
# print("Shape={0}".format(a.shape))
# print("Size = {0}".format(a.size))

#This produces 3 rows, 2 columns and the 4th one is a box (think div class = container)

#Generate a 3D array
#Method 1: for loops with the index

# np.random.seed(0)

# a = np.random.randint(9, size=(3,2,4))

# print(a)

# min,max = a[0][0][0],a[0][0][0]

# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         for k in range(a.shape[2]):
#             if a[i][j][k] < min:
#                 min = a[i][j][k]
#             elif a[i][j][k] > max:
#                 max = a[i][j][k]
# difference = max-min
# print("Diffreence = {0}".format(difference))

#Finds the max and min elements in the arrays, max is 8, min is 0, difference is 8.

#Method 2:
#Loops refering to variables
# np.random.seed(0)

# a = np.random.randint(9, size=(3,2,4))

# print(a)

# min,max = a[0][0][0],a[0][0][0]

# for i in a:
#     for j in i:
#         for k in j:
#             if k<min:
#                 min = k
#             elif k > max:
#                 max = k
# diffrence = max-min
# print("Diffreence = {0}".format(difference))

#if you set min and max to i or j: you get an error
#error The truth value of an array with more than one element is ambiguous. Usa a.any() or a.all()

#Given temp data from25 stations in a 5x5 grid (hundreds of miles)
# This is cool!

# import matplotlib.pyplot as plt 
# np.random.seed(0) # reproduce "random"
# a = np.random.randint(9,size=(5,5))
# sum = 0

# for i in a:
#     for j in i:
#         sum += j
# ave = sum/25

# for i in range(0,a.shape[0]):
#     for j in range(0,a.shape[1]):
#         if a[i][j] >= ave:
#             plt.plot(i,j,'bo')
#         else:
#             plt.plot(i,j,'rx')
# plt.show()

# import matplotlib.pyplot as plt
# np.random.seed(0) # reproduce "random"
# a = np.random.randint(9,size=(5,5))
# print("The data")
# print(a)

# def ave(xarray):
#     sum = 0
#     size = xarray.shape[0]*xarray.shape[1]
#     yarray = xarray.reshape(size)
#     for i in yarray:
#         sum += i
#     return sum/size

# def myplot(xarray):
#     xave = ave(xarray)
#     for i in range(0,xarray.shape[0]):
#         for j in range(0,xarray.shape[1]):
#             if a[i][j] >= xave:
#                 plt.plot(i,j,'bo')
#             else:
#                 plt.plot(i,j,'rx')
#     plt.show()

# #Program
# print("The average = {0}".format(ave(a)))
# myplot(a)

# def foo(x):
#     return x + 2

# print(2+4)
# print(2+9)
# print(foo(4))
# print(foo(9))
# print((lambda x: x+2)(4))
# print((lambda x: x+9)(9))
# Lambda is an anymous function.  

# def f(x,y):
#     return x*y
# def g(x,y):
#     return x+y
# def h(x,y):
#     return x-y

# xflst = [f,g,h]
# xlst = [1,2,3]
# ylst = [2,3,4]

# for f in xflst:
#     for i,j in zip(xlst,ylst):
#         print(f(i,j))
