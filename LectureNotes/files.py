# def myMax(x,y):
#     return (x>=y)*x + (x<y)*y

# print(myMax(88,12))

#Method 1
# def r1(old,new,xlst):
#     tmp = []
#     if xlst:
#         for i in xlst:
#             if old == i:
#                 tmp += [new]
#             else:
#                 tmp += [i]
#     return tmp

# #Method 2
# def r2(old,new,xlst):
#     xlst = xlist.copy
#     tmp = []
#     if xlst:
#         for i in range(0,len(xlst)):
#             if old == xlst[i]:
#                 tmp += [i]
#             else:
#                 tmp += [xlst[i]]
#     return tmp

# #Method 3 
# def w1(old,new,xlst):
#     i = 0
#     tmp = []
#     while xlst and 0 <= i and i < len(xlst):
#         if old == xlst[i]:
#             tmp += [new]
#         else:
#             tmp += [xlst[i]]
#         i+=1
#     return tmp

# #Method 4
# def w2(old,new,xlist):
#     i = 0
#     tmp = []
#     xlst = xlist.copy()
#     while xlst:
#         if xlst[0] == old:
#             tmp += [new]
#         else:
#             tmp += [xlst[0]]
#         xlst = xlst[1:]
#     return tmp

# #Method 5
# def fun1(old,new,xlist):
#     tmp = []
#     for i in xlist:
#         tmp += (i == old) * [new] + (i != old)
#     return tmp

# #Method 6: Recursion
# def fun2(old,new,xlist):
#     return ['z' if i == 'a' else i for i in x]

# def fun3(old,new,xlist):
#     xlst = xlist.copy()
#     def r(xlst):
#         if xlst:
#             if xlst[0] == old:
#                 return [new] + r(xlst[1:])
#             else:
#                 return [xlst[0]] + r(xlst[1:])
#     r(xlist)

#Arrays
# import numpy as np
# x = np.array([10,2,3,3])
# print(x)
# y =  np.array([[13,4],[42,5]])
# print(y)
# print(y[0])
# print(y[1])
# print(y[0][0])
# print(y[0][1])

#Histogram stuff
# import math
# import random as rn 
# import matplotlib.pyplot as plt 

# xlst = []

# for i in range(0,1000):
#     x = rn.random()
#     y = rn.random()
#     z0 = math.sqrt(-2.0*math.log(x))*math.cos(2.0*math.pi*y)
#     xlst.append(z0)

# num_bins = 100
# plt.hist(xlst,num_bins,facecolor="blue")
# plt.show()

#This one doesnt work :/
with open("c:C200-Assignments-alack\LectureNotes\doggy.txt", "r") as puppy:
    all_wolves = puppy.read()

print(all_wolves)

xlst = []

for i in all_wolves:
    xlst += [i.split(" ")]

print(xlst)

xtmp = xlst[:]
ysum,nsum = 0,0

while xtmp:
    x = int(xtmp[0][1])
    if xtmp[0][0] == "Yes":
        ysum += x
    else:
        nsum += x
    xtmp = xtmp[1:]
print("Yes = {0}; No = {1}".format(ysum,nsum))