# g = lambda: 3
# h = g
# print(g() + 5)
# print(g() + h())
# g = lambda: 4
# print(g()+ 5)
# print(g()+h())
# h = lambda: 10
# print(g() + 5)
# print(g()+h())

# g = lambda: 3
# h = lambda: 4 + g()
# i = [g,h]
# j = i

# sum = 0
# for f in i:
#     sum += f()
# print(sum)
# sum = 0
# for f in j:
#     sum += f()
# print(sum)

# g = lambda: 10000
# sum = 0
# for f in i:
#     sum += f()
# print(sum)
# sum = 0
# for f in j:
#     sum += f()
# print(sum)

# import time

# def ftimer(f,args):
#     time_start = time.perf_counter()
#     f(args)
#     time_elapsed2 = (time.perf_counter() - time_start)
#     return time_elapsed2

# #Recursive
# def f(n):
#     if n == 0:
#         return 100
#     else:
#         return n - 10 + f(n-1)

# #Tail Recursive
# def ftr(n,s):
#     if n == 0:
#         return s + 100
#     else:
#         return ftr(n-1,s+n-10)

# #Tail recursive with helper
# def g(n):
#     def g_help(x,s):
#         if x == 0:
#             return s
#         else:
#             return g_help(x-1,s+x-10)
#     return g_help(n,100)

# #Memoization for loop
# def h(n):
#     d = {0:100}
#     for i in range(0,n+1):
#         if not i in d.keys():
#             d[i] = i + d[i-1] -10
#     return d[i]

# def m(n):
#     x,y = 100, 91
#     z = 0
#     if n == 0:
#         return x
#     elif n == 1:
#         return y
#     else:
#         for i in range(n,n+1):
#             x = y
#             y = x+i-10
#         return y

# flist = [f,lambda i: ftr(i,0), g,h,m]
# tlist = [round(ftimer(f,700)*10**5,2) for f in flist]
# print(tlist)

# # output:           [67.88, 24.83, 39.24, 30.52, 0.26]
# # Dr. D's output:   [79.13, 26.31, 31.92, 25.01, 8.25]

# Convergence

# Bounds example
# def i(x,left,right):
#     return left <= x and x <= right

# xlst = [-2,0,1,5]

# for x in xlst:
#     print(i(x,-1,1), i(x,0,10), i(x,0,1) or i(x,2,3))

# def t(x,right):
#     return x < right

# xlst = [-2,.5,.4,0]

# for x in xlst:
#     print(t(x,.5), t(x,-1))

# def b(n,alpha,tau):
#     def bp(n):
#         if n < tau:
#             return 0
#         else:
#             return 1 + bp(alpha*n)
#     return bp(n)

# tennis_ball = .53
# super_ball = .85
# tau = .1
# print(b(1,tennis_ball,tau))
# print(b(1,super_ball,tau))

# Output: 4,15 bounces

import numpy as np 
import matplotlib.pyplot as plt 

#Data from experiment

# x = np.array([1,2,3,4,5])
# y = np.array([.56,.3,.1,.04,0])

# f = lambda x,alpha: alpha**x

# plt.plot(x,y,'ro')
# #trying alpha = .59
# plt.plot(x,f(x,.59),'g')

# #trying alpha = .5295
# plt.plot(x,f(x,.5295), 'b')
# plt.show()

# def error(estimate,x):
#     return abs((estimate - x**2)/(2*x))

# def square_root(estimate,tau,start):
#     x = start
#     while error(estimate,x) > tau:
#         x = (x+estimate/x)*(1/2)
#     return x

# estimate,tau,start = 2,0.00005,2
# print(square_root(2,0.00005,2))


# def s_r(estimate,tau,start):
#     x = start
#     def s_r_help(x):
#         if error(estimate,x) > tau:
#             return s_r_help((x+estimate/x) * (1/2))
#         return x
#     return s_r_help(estimate)

# estimate,tau,start = 2, 0.00005, 2
# print(s_r(estimate,tau,start))

# import numpy as np
# import matplotlib.pyplot as plt 

# v = np.zeros(10)
# g = np.zeros(10)

# def error(estimate,x):
#     return abs((estimate - x**2)/(2*x))

# def square_root(estimate,tau,start):
#     x = start 
#     i = 0
#     v[i] = error(estimate,x)
#     g[i] = x
#     while error(estimate,x) > tau:
#         i += 1
#         x = (x+estimate/x) * (1/2)
#         v[i] = error(estimate,x)
#         g[i] = x
#     return x

# # t1 = np.arange(1,10,1)

# # plt.ylabel("Initial Estimate")
# # plt.xlabel("Iteratoins")
# # plt.title("Convergence of Square Root")

# # estimate,tau,start = 2, 0.00005, 2
# # print(square_root(estimate,tau,start))

# # plt.plot(t1,v[t1], 'r-o')
# # plt.plot(t1,g[t1], 'b-o')
# # plt.show()

# t1 = np.arange(1,8,1)

# plt.ylabel("Initial Estimate")
# plt.xlabel("Iterations")
# plt.title("Convergence of Square Root")

# print(square_root(1000,.00005,500))
# plt.plot(t1,v[t1],'r-o')

# print(square_root(1000,.00005,775))
# plt.plot(t1,v[t1],'b-o')

# print(square_root(1000,.00005,3))
# plt.plot(t1,v[t1],'g-o')

# plt.show()

# Map

# x = [1,4,2,3,1]
# y = [5,1,42,1,2]

# z_i = map((lambda x,y: y if y > x else x), x,y)
# z_l = list(map((lambda x,y: y if y > x else x), x,y))

# for i in z_i:
#     print(i)

# for i in z_l:
#     print(i)

# print(z_i)
# print(z_l)

# output: 
# 5
# 4
# 42
# 3
# 2
# 5
# 4
# 42
# 3
# 2

# x = [1,4,2,3,1]
# y = [5,1]

# z = map((lambda x,y: x-y),y,x)

# for i in z:
#     print(i)

# List Comprehension

# xlst = [4,3,2,7,9]

# y = [x for x in xlst]
# print(y)

# y = ["{0} is cool".format(x) for x in xlst]
# print(y)

# import math
# y = ["{0}**2 = {1}".format(math.sqrt(x),x) for x in xlst if math.sqrt(x) == int(math.sqrt(x))]
# print(y)

#Nest Comprehensions

# x = [[row] for row in range(0,3)]
# print(x)

# x = [[1 if row == col else 0 for col in range(0,3)] for row in range(0,3)]
# print(x)