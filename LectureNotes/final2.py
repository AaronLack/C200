#This is a review doc of all the code from previous slides
#If instructors see this then lol I'm still gonna fail your final 

# def f(n):
#     if n == 0:
#         return 1
#     else:
#         return 3*(f(n-1)**2)

# for i in range(0,4):
#     print(f(i))

# def a(n):
#     if n == 0:
#         return 2
#     else:
#         return 6*(a(n-1))

# for i in range(0,4):
#     print(a(i))

# def a(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2
#     else:
#         return a(n-1) + 3*a(n-2)

# for i in range(0,4):
#     print(a(i))

# def tail_rec_fac(n,v=1):
#     if n == 0:
#         return v
#     else:
#         return tail_rec_fac(n-1, n*v)

# for i in range(0,7):
#     print(tail_rec_fac(i))

# def fac2(n):
#     v = 1
#     for i in range(n,0,-1):
#         v *= i
#     return v

# for i in range(0,6):
#     print(fac2(i))

#remove an item

# def remove(lst,x):
#     if lst == []:
#         return []
#     else:
#         if lst[0] == x:
#             return remove(lst[1:],x)
#         else:
#             return [lst[0]] + remove(lst[1:],x)

# print(remove([1,2,1,3,1,2,1,"a"],1))

# def h():
#     x = 0
#     while True:
#         yield x
#         x = x+2

# x1 = h()
# print(next(x1))
# print(next(x1))
# print(next(x1))
# print(next(x1))

# def gen(start,stop,step):
#     while start < stop:
#         if start > stop:
#             return
#         yield round(start,2)
#         start += step

# for i in list(gen(0,1,.3)):
#     print(i)

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

# d = {0:1}
# def f(n):
#     if n in d.keys():
#         return d[n]
#     else:
#         d[n] = 3*(f(n-1)**2)
#         return d[n]

# for i in range(0,4):
#     print(f(i))

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
#         x1,x2 = x2, x1+x2

# def Fib(stop):
#     for i,j in zip(range(1,stop),fib()):
#         print("f({0}) = {1}".format(i,j))

# Fib(10)

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

# print([1 if i%2 == 0 else 0 for i in range(0,6)])

# tmp = []
# for i in range(1,5):
#     for j in range(0,i):
#         tmp.append(i*j)
# print(tmp)

# x = [i*j for i in range(1,5) for j in range(0,i)]
# print(x)

# x = [i for i in range(0,52) if i%2 == 0 if i%3 == 0]
# print(x)

# def example(x):
#     return 2*x if x>2 else x/2

# x = [example(i) for i in range(0,5)]
# y = [(lambda x:2*x if x>2 else x/2) (i) for i in range(0,5)]
# print(x)
# print(y)

# class Graph:
#     def __init__(self,nodes):
#         self.nodes = nodes
#         self.edges = {}
#         for i in self.nodes:
#             self.edges[i] = []
#     def add_edge(self,pair):
#         start,end = pair
#         self.edges[start].append(end)
#     def children(self,node):
#         return self.edges[node]
#     def nodes(self):
#         return str(self.nodes)
#     def __str__(self):
#         return str(self.edges)

# g = Graph([1,2,3,4,5])
# elst = [(1,2), (1,3), (2,4), (2,3), (4,1), (3,3), (3,4), (3,2), (5,4), (5,3)]
# for i in elst:
#     g.add_edge(i)
# print(g)

from Stack import Stack

# def dfs(g,node):
#     visited = []
#     s = Stack()
#     s.push(node)
#     while not s.isEmpty():
#         nnode = s.pop()
#         if nnode not in visited:
#             visited.append(nnode)
#             clist = g.children(nnode)
#             for n in clist:
#                 if n not in visited:
#                     s.push(n)

#     return visited
# print(dfs(g,1))
# print(dfs(g,2))
# print(dfs(g,3))
# print(dfs(g,4))
# print(dfs(g,5))

import sqlite3

dog = sqlite3.connect("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/LectureNotes/example2.db")
c = dog.cursor()

# c.execute('''CREATE TABLE Account1(Name text, Checking real, Savings real)''')
# c.execute("INSERT INTO Account1 Values('Ursala', 1000, 400)")
# c.execute("INSERT INTO Account1 Values('Kaiser', 200, 100)")
# c.execute("INSERT INTO Account1 Values('Shilah', 500, 200)")
# c.execute('SELECT * FROM Account1 WHERE Checking > 200')
# print(c) #prints a memory location
# print(list(c))  #prints what we want

# c.execute('SELECT Account1.Name FROM Account1 WHERE Checking != 1000')
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())

# c.execute('SELECT Account1.Name FROM Account1 WHERE Checking != 1000')
# i = 1
# x = c.fetchone()
# while x:
#     print("{0} {1}".format(i,x))
#     i += 1
#     x = c.fetchone()

# houses = [('123 Mockingird Lane', 100, 2.5), ('5040 RR2 Canine', 400, 1), ('1 Paw Manor', 400, .25), ('1600 Pen Ave', 750, 3), ('107 S Indiana', 850, 2)]

# # c.execute('''CREATE TABLE M (Address text, Price real, Acres real)''')

# # c.executemany('INSERT INTO M VALUES (?,?,?)', houses)

# x = c.execute("SELECT Account1.Name, M.Address FROM Account1, M WHERE Account1.Savings + Account1.Checking > M.Price*.5")

# for i in x:
#     print(i)

# dog.commit()

# # for i in c.execute('SELECT * FROM M'):
# #     print(i)

# dog.close()

# g = lambda: 3
# h = g
# print(g()+ 5)
# print(g() + h())
# g = lambda: 4
# print(g()+5)
# print(g()+h())
# h = lambda: 10
# print(g() + 5)
# print(g()+h())

#Covergence
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
# print(b(1, super_ball, tau))

# x = [1,4,2,3,1]
# y = [5,1,42,1,2]

# z_i = map((lambda x,y: y if y > x else x), x, y)
# z_l = list(map((lambda x,y: y if y > x else x), x, y))

# for i in z_i:
#     print(i)
# for i in z_l:
#     print(i)

# print(z_i)
# print(z_l)

# xlst = [4,3,2,7,9]
# y = [x for x in xlst]
# print(y)


# x = [[row] for row in range(0,3)]
# print(x)

# x = [[1 if row == col else 0 for col in range(0,3)] for row in range(0,3)]
# print(x)

#This is cool!
# import random as rn 
# xlst = []
# for i in range(0,20):
#     xlst.append(rn.randint(0,100))
# print("Unsorted Random List:")
# print(xlst)

# def quicksort(xlst):
#     if len(xlst) == 0:
#         return []
#     elif len(xlst) == 1:
#         return [xlst[0]]
#     else:
#         pivot = xlst[0]
#         rest = xlst[1:]
#         left = []
#         right = []
#         for i in rest:
#             if i <= pivot:
#                 left.append(i)
#             else:
#                 right.append(i)

#         return quicksort(left) + [pivot] + quicksort(right)
# ylst = quicksort(xlst)
# print("Sorted List")
# print(ylst)

# class Account:
#     def __init__(self, name, chekcing, savings):
#         self.name = name
#         self.checking = chekcing
#         self.savings = savings

#     def deposit(self,account,amount):
#         if account == "checking":
#             self.checking += amount
#         elif account == "savings":
#             self.savings += amount

#     def get_name(self):
#         return self.name

#     def cut_cheeck(self,amt):
#         if amt <= self.checking:
#             self.checking -= amt
#             return amt
#         else:
#             return 0

#     def withdrawal(self,amt):
#         if amt <= self.savings:
#             self.savings -= amt
#             return amt
#         else:
#             return 0

#     def transfer(self,act,amt):
#         if act == "checking":
#             if amt <= self.checking:
#                 self.savings += amt
#                 self.checking -= amt
#                 return True
#             else:
#                 return False
#         elif act == "savings":
#             if amt <= self.savings:
#                 self.checking += amt
#                 self.savings -= amt
#                 return True
#             else:
#                 return False

# class MyCN:
#     def __init__(self, rpart, ipart):
#         self.rpart = rpart
#         self.ipart = ipart
#         self.cn = [self.rpart,self.ipart]
#     def get_real(self):
#         return self.rpart
#     def get_imag(self):
#             return self.ipart
#     def __str__(self):
#         return str(self.cn)

#     def add(self,ix):
#         real_part = self.get_real() + ix.get_real()
#         imag_part = self.get_imag() + ix.get_imag()
#         iy = MyCN(real_part, imag_part)
#         return iy
# a1 = MyCN(3,-1)
# b1 = MyCN(0,6)
# c1 = a1.add(b1)
# print("{0} + {1} = {2}".format(a1,b1,c1))
# from datetime import date

# class Person:
#     programmer = True

#     def __init__(self,x,d):
#         self.name = x
#         self.bd = date(d[2],d[0],d[1])

#     def get_name(self):
#         return self.name
    
#     def get_birthdate(self):
#         return self.bd 

#     def get_age(self):
#         today = date.today()
#         return today.year - self.bd.year

# p1 = Person("Bach",(3,31,1685))
# p2 = Person("Ada",(12,10,1815)) 

# # print(p2.get_name())
# # print(p1.programmer)

# print(p2.get_birthdate())
# print(p2.get_age())

# s = Stack()
# t = Stack()

# s.push(3)
# s.push(4)
# s.pop()
# t.push(':')
# s.push(t.pop())

# Fibbonocci
# n = 10
# a = [0,1]
# for i in range(2,n):
#     a.append(a[i-1] + a[i-2])

# print(a)

# def f(**x):
#     print(x)
# f(good = 'ugly', bad = 1, love = True)

# def f(*x):
#     print(x)

# f()
# f(1,2,3)
# f("dog", True, 1)


#IMPORTANT
# def f(*x):
#     print(x)

# print("EX1")
# f()
# f(1)
# f(1,'cat')
# f("dog",43,[1,2])

# def f1(*x, **y):
#     if y.get("animal") == "check":
#         if 'dog' in x or 'cat' in x:
#             print("Cute")
#         else:
#             print("dupe")

# print("Example2")
# f1(animal = "check")
# f1(1,animal="check")
# f1(1,"cat", animal = "check")
# f1("dog", 43,[1,2], animal = "check")

# def g1(*x,**options):
#     if options.get("operation") == "sum":
#         return sum(list(x))
#     elif options.get("operation") == "prod":
#         xp = 1
#         for i in x:
#             xp *= i
#         return xp
#     else:
#         return "none"

# print("example 3")
# print(g1(1,2,3,4,5))
# print(g1(1,2,3,4,5, operation = "sum"))
# print(g1(1,2,3,4,5, operation = "prod"))

# def g(n):
#     if n == 0:
#         return 1
#     else:
#         prod = 1
#         for i in range(2,n+1):
#             prod *= i
#         return prod

# def h(n):
#     prod = 1
#     while n:
#         prod *= n
#         n -= 1
#     return prod

# def hp(n):
#     prod = 1
#     cnt = 1
#     while cnt < n + 1:
#         prod *= cnt
#         cnt += 1
#     return prod

# def f(n):
#     if n == 0:
#         return 1
#     else:
#         return n*f(n-1)

# def ftail(n, x=1):
#     if n == 0:
#         return x
#     else:
#         return ftail(n-1,n*x)

# def a():
#     prod = 1
#     n = 1
#     while True:
#         yield prod
#         prod *= n
#         n += 1
# x = a()
# for i in range(0,10):
#     print(next(x))

# import math
# math.exp(1)

# def approx_e():
#     n = 1
#     prod = 1
#     sum = 0
#     while True:
#         sum += 1/prod
#         yield sum
#         prod *= n 
#         n += 1

# x = approx_e()
# for i in range(0,7):
#     print(next(x))

x = "1ABC"
for i in range(0,len(x)-2):
    print(int(x[i]+x[i+1]+x[i+2],16))

