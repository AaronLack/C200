# # Recursion
# def Box(k):
#     if k == 0:
#         return 0
#     else:
#         return Box(k-1) + 1

# # For
# def fBox(k):
#     sum = 0
#     for i in range(1,k+1):
#         sum += 1
#     return sum

# def wBox(k):
#     sum = 0
#     while k:
#         sum += 1
#         k -= 1
#     return sum

# d = [Box(6), fBox(6), wBox(6)]
# print("I ate {0} donuts".format(d))

# def f(xlist):
#      sum = 0
#      for i in xlist:
#          sum += i
#      return sum

# xlist = [4+10+0+-1+2]
# print(f(xlist))

# def f(xlist):
#     if len(xlist) == 1:
#         return xlist[0]

# xlist = [2]
# print(f(xlist))

# def f(xlist):
#     if len(xlist) == 1:
#         return xlist[0]
#     else:
#         return xlist[0] + f(xlist[1:])

# # This trace is the code for what I solved for in my lecutre notes
# def trace(f):
#     f.segment = 0
#     def mid(x):
#         print('| ' * (f.segment) + 'Segment {0}'.format(f.segment), "{0}({1})".format(f.__name__, x))
#         f.segment += 1
#         return_value = f(x)
#         print('| ' * f.segment + '|...','return',repr(return_value))
#         f.segment -=1
#         return return_value
#     return mid

# xlist = [4,6,-2]
# f = trace(f)
# print(f(xlist))

# Factorial using while
# def fac1(n):
#     p = 1
#     while n > 0:
#         p = p*n
#         n -= 1
#     return p

# # Factorial using for
# def fac2(n):
#     p = 1
#     for i in range(n,0,-1):
#         p = p*i
#     return p

# for i in range(0,10):
#     print("{0}! = {1} = {2}".format(i,fac1(i),fac2(i)))

# # Recursion

# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)

# print(fac(5))

# def f(j,k):
#     if j == 0:
#         return 0
#     else:
#         return k + f(j-1,k)
    
# for i in range(2,5):
#     for j in range(2,5):
#         print("{0:<} {1:<}, {2:<} {3:<}".format(i,j,f(j,i),f(i,j)))

# def f(x,y):
#     if y == 0:
#         return x
#     else:
#         return f(x-1,y-1)

# print(f(4,10), f(10,4), f(3,0))
# import math

# def gw(n):
#     s = 0
#     while n > 0:
#         s = s + 2*n
#         n = n // 2
#     return s

# def gf(n):
#     if n == 0:
#         return 0
#     else:
#         s = 0
#         cnt = math.floor(math.log2(n) + 1)
#         for i in range(cnt,0,-1):
#              s = s+ 2*n
#              n = n//2
#         return s

# def gr(n):
#     if n == 0:
#         return 0
#     else:
#         return 2*n + gr(n//2)

# for i in range(0,6):
#     print("{0:<5} {1:<5} {2:<5}".format(gf(i),gw(i),gr(i)))

# def remove(lst,x):
#     if lst == []:
#         return []
#     else:
#         if lst[0] == x:
#             return remove(lst[1:],x)
#         else:
#             return [lst[0]] + remove(lst[1:],x)

# print(remove([1,2,1,3,2,1,'a'],1))

# With a helper function

# def remove(lst,x):
#     def remHelp(lst):
#         if lst == []:
#             return []
#         else:
#             if lst[0] == x:
#                 return remHelp(lst[1:])
#             else:
#                 return [lst[0]] + remHelp(lst[1:])
#     return remHelp(lst)

# print(remove([1,2,1,3,2,1,'a'],1))