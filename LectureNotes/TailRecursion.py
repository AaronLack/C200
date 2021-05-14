# Base Case: f0 = 2
# Induction: fn = 3*(f(n-1)**2)

# def f(n):
#     if n == 0:
#         return 1
#     else:
#         return 3*(f(n-1)**2)

# for i in range(0,4):
#     print("f({0}) = {1}".format(i,f(i)))

# def a(n):
#     if n == 0:
#         return 2
#     else:
#         return 6*a(n-1)

# for i in range(0,4):
#     print("f({0}) = {1}".format(i,a(i)))

# def a(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2
#     else:
#         return a(n-1) + 3*a(n-2)

# for i in range(0,4):
#     print("f({0}) = {1}".format(i,a(i)))

# def a(n):
#     if n == 0 or n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return a(n-1) - a(n-2) + a(n-3)

# for i in range(3,7):
#     print("f({0}) = {1}".format(i,a(i)))


# def j(n):
#     if n == 1:
#         return 1
#     else:
#         return n**2 + j(n-1)

# sum = j(5)

# print(sum)

# Analytial Solution

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n+f(n-1)

# ans = f(5)
# print(ans)

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n + f(n-1)

# #solution
# def g(n):
#     return (n*(n+1))//2

# print(f(5),g(5))

# def j(n):
#     if n == 1:
#         return 1
#     else:
#         return n**2 + j(n-1)

# g = lambda n: (n*(n+1)*(2*n+1))//6

# print(j(5),g(5))

# Tail recursion for factorial
# def tail_rec_fac(n, v=1):
#     if n == 0:
#         return v
#     else:
#         return tail_rec_fac(n-1, n*v)

# for i in range(0,10):
#     print("{0}! = {1}".format(i,tail_rec_fac(i)))

# This program shows the time it takes to generate factorial answers

# import time

# #Traditional Recurion
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)

# #Tail Recursion
# def tail_rec_fac(n,v=1):
#     if n == 0:
#         return v
#     else:
#         return tail_rec_fac(n-1, n*v)

# #For-Loop
# def fac2(n):
#     v = 1
#     for i in range(n,0,-1):
#         v *= i
#     return v

# time_start = time.perf_counter()
# tail_rec_fac(700)
# time_elapsed1 = (time.perf_counter()-time_start) # Traditional
# time_elapsed2 = (time.perf_counter()-time_start) # Tail Recursion
# time_elapsed3 = (time.perf_counter()-time_start) # For Loop


# xtimes = [time_elapsed1, time_elapsed2, time_elapsed3]

# print(xtimes)
# print([i/min(xtimes) for i in xtimes])

# def remove(lst,x,acc):
#     if lst == []:
#         return acc
#     else:
#         if lst[0] == x:
#             return remove(lst[1:],x,acc)
#         else:
#             return remove(lst[1:],x,acc + [lst[0]])

# x = [1,2,1,3,2,1,'a']
# print(remove(x,1,[]))

# Generators:

# def h():
#     x = 0
#     while True:
#         yield x
#         x = x + 2

# # Start Generator
# x1 = h()
# for i in range(0,6):
#     print(next(x1))

# def h():
#     x = 0
#     while True:
#         yield x
#         x = x + 2

# # For:
# def g(xstop):
#     for i in h():
#         if i > xstop:
#             return i
#         else:
#             yield i

# for i in g(10):
#     print(i)

# def gen(start,stop,step):
#     while start < stop:
#         if start > stop:
#             return
#         yield round(start,2)
#         start += step

# for i in list(gen(0,1,.3)):
#     print(i)

def gen(start,stop,f,step):
    while start < stop:
        if start > stop:
            return
        yield float(round(start,2))
        start = f(start,step)

for i in list(gen(0.1,1.1, lambda x,y: x**2+2*y,.2)):
    print(i)

# def s(f,x):
#     for i in range(0,x):
#         print("f({0}) = {1}".format(i,f(i)))

# def a(n):
#     if n == 0:
#         return 3
#     else:
#         return 2*a(n-1)-1

# s(a,5)

# def aline(n):
#     return (n==0)*3 or 2*aline(n-1)-1

# for i in range(0,5):
#     print("aline({0}) = {1}".format(i,aline(i)))


# import time

# d = {0:3, 1:9}

# def b(n):
#     for i in range(0,n+1):
#         if not i in d.keys():
#             d[i] = 2*d[i-1] -1
#         else:
#             return d[i]

# time_start = time.perf_counter()
# b(900)
# time_elapsed1 = (time.perf_counter()-time_start)
# print(time_elapsed1)

# def c(n):
#     e = {0:3, 1:9}
#     for i in range(0,n+1):
#         if not i in e.keys():
#             e[i] = 2*e[i-1] -1
#         else:
#             return e[i]

# time_start = time.perf_counter()
# b(900)
# time_elapsed2 = (time.perf_counter()-time_start)
# print(time_elapsed2)

# xtimes = [time_elapsed1, time_elapsed2]
# print(xtimes)
# print([i/min(xtimes) for i in xtimes])

# def s(f,sa,st):
#     for i in range(sa,st):
#         print("f({0}) = {1}".format(i,f(i)))

# def b(n):
#     if n == 1:
#         return 2
#     elif n == 2:
#         return 3
#     else:
#         return 3*b(n-1) - b(n-2)


# s(b,1,6)

# def s(f,sa,st):
#     for i in range(sa,st):
#         print("{0}({1})={2}".format(f.__name__,i,f(i))) # We are asking the object what its name is

# def x(n):
#     if n == 0:
#         return 3
#     else:
#         return 2*x(n-1) -1

# def x_prime(n):
#     if n == 0:
#         return 1
#     else:
#         return 2*x_prime(n-1) -1

# s(x,0,5)
# s(x_prime,0,5)

# def s(f,sa,st):
#     for i in range(sa,st):
#         print("f({0}) = {1}".format(i,f(i)))

# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# s(f,1,10)

#Using generators for previous problem
# def fib():
#     x1,x2 = 1,1
#     while True:
#         yield x1
#         x1,x2 = x2,x1+x2

# def Fib(stop):
#     for i,j in zip(range(1,stop),fib()):
#         print("f({0}) = {1}".format(i,j))

# Fib(10)

# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# import math

# def F(n):
#     phi = (1+math.sqrt(5))/2
#     return (phi**n - (1-phi)**n)/math.sqrt(5)

# for i in range(1,10):
#     print("{0} {1}".format(f(i), F(i)))

# c = 1
# def T(n):
#     if n == 1:
#         return c
#     else:
#         return T(n//2) + c

# print(256, T(256))
# print(100, T(100))
# print(64, T(64))
# print(8, T(8))

# def Line(n):
#     if n == 0:
#         return 1
#     else:
#         return Line(n-1) + n

# def Linew(n):
#     sum = 1
#     while n > 0: 
#         sum += n
#         n -= 1
#     return sum

# def L(n):
#     return n*(n+1)/2 + 1

# for i in range(0,6):
#     print("Line({0}) = {1} {2} {3}".format(i,Line(i),L(i),Linew(i)))