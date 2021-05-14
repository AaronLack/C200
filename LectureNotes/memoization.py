# d = {0:1, 1:3}

# def f(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         d[n] = 3*(d[n-1]**2)
#         return d[n]

# for i in range(0,4):
#     print("f({0}) = {1}".format(i,f(i)))

# print(d[3])


# d = {0:2, 1:12}

# def a(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         d[n] = 6*d[n-1]
#         return d[n]

# for i in range(0,4):
#     print("a({0}) = {1}".format(i,a(i)))

# d = {0:1, 1:2}

# def a(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         d[n] = d[n-1] + 3*d[n-2]
#         return d[n]

# for i in range(0,4):
#     print("a({0}) = {1}".format(i,a(i)))


# d = {0:1, 1:1, 2:2}

# def a(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         d[n] = d[n-1] - d[n-2] + d[n-3]
#         return d[n]

# for i in range(3,7):
#     print("a({0}) = {1}".format(i,a(i)))

# This one has to be done bottom up
# d = {1:1}

# def j(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         for i in range(2,n+1):
#             d[i] = i**2 + d[i-1]
#         return d[n]

# sum = j(5)
# print(sum)

# def fib():
#     x1,x2 = 1,1
#     while True:
#         yield x1
#         x1,x2 = x2,x1+x2

# def Fib(stop):
#     for i,j in zip(range(1,stop),fib()):
#         print("f({0}) = {1}".format(i,j))

# Fib(10)

# Binary Search

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

# import math
# c = 1

# def T(n):
#     if n == 1:
#         return c
#     else:
#         return T(n//2) + c

# def t(n):
#     return math.log2(n) + c

# print(256, T(256), t(256))
# print(100, T(100), t(100))
# print(64, T(64), t(64))
# print(8, T(8), t(8))


# Making a list inside out
# tmp = []
# for i in range(0,6):
#     tmp.append(i**2)

# print(tmp)

# print([i**2 for i in range(0,6)])

# def squares(n):
#     return [i**2 for i in range(0,n+1)]

# print(squares(5))

# tmp = []

# for i in range(0,6):
#     if i % 2 == 0:
#         tmp.append(1)
#     else:
#         tmp.append(0)
# print(tmp)

# tmp = []

# for i in range(0,6):
#     if i % 2 == 0:
#         tmp.append(1)
#     else:
#         tmp.append(0)
# print(tmp)

# print([1 if i%2 == 0 else 0 for i in range(0,6)])

# tmp = []
# xlst = list(range(0,6))
# ylst = list(range(6,0,-1))
# for i,j in zip(xlst,ylst):
#     if i == j:
#         tmp.append("Y")
#     else:
#         tmp.append("N")
# print(tmp)

# x = ["Y" if i == j else "N" for i,j in zip(xlst,ylst)]
# print(x)

# x = [i for i in "bigword"]
# print(x)

# x = [x for x in "bigword"]
# print(x)

# x = [i for i in range(0,52) if i%2 == 0 if i%3 == 0]
# print(x)

# x = [i for i in range(2,51)]

# def e(xlst):
#     def d(xlst,x):
#         if xlst:
#             return (xlst[0] % x != 0) * [xlst[0]] + d(xlst[1:],x)
#         else:
#             return []
#     if xlst:
#         return [xlst[0]] + e(d(xlst[1:],xlst[0]))
#     else:
#         return []

# primes = e(x)

# print(primes)


# def edits1(words):
#    "All edits that are one edit away from 'word'"
#    letters      = 'abcdefghijklmnopqrstuvwxyz'
#    splits       = [(word[:i], word[i:])         for i in range(len(word) + 1)]
#    deletes      = [L + R[1:]                    for L, R in splits if R]
#    transposes   = [L + R[1] + R[0] + R[2:]      for L, R in splits if len(R) > 1]
#    replaces     = [L + c + R[1:]                for L, R in splits if R for c in letters]
#    inserts      = [L + c + R                    for L, R in splits for c in letters]
#    return set(deletes + transposes + replaces + inserts)

# def edits2(word):
#     "All edits that are two edits away from word."
#     return (e2 for e1 in edits(word) for e2 in edits1(e1))