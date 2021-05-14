import matplotlib.pyplot as plt 
import numpy as np 

# x = np.arange(10)

# plt.gca().set_prop_cycle('color', ['red', 'green', 'blue', 'yellow'])

# plt.plot(x, 3*x -1)
# plt.plot(x, -2*x + 3)

# plt.legend(['y=3*x-1', 'y=-2*x + 3'], loc='upperleft')

# plt.show()

#OOD Version

# abscissa = np.arange(20)
# plt.gca().set_prop_cycle('color', ['red', 'green', 'blue', 'yellow'])

# class MyLine:

#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#         self.slope = (p2[1] - p1[1] / p2[0] - p1[0])
#         self.intercept = p1[1] - self.slope*p1[0]
#         self.line = lambda x: self.slope * x + self.intercept

#     def draw(self):
#         plt.plot(abscissa, self.line(abscissa))

#     def get_line(self):
#         return "y = {0:.2f}m + {1:.2f}".format(self.slope,self.intercept)
    
#     def __str__(self):
#         return get_line()

# x1 = MyLine((0,0),(5,5))
# x1.draw()
# x2 = MyLine((5,0),(1,1))
# x2.draw()
# x3 = MyLine((0,5),(1,4))
# x3.draw()

# plt.legend([x1.get_line(), x2.get_line(), x3.get_line()], loc = 'upper left')

#Intersections
# x1 = MyLine((0,0),(5,5), options = "2pts")
# x1.draw()

# x2 = MyLine((5,0), -1/4, options = "point-slope")
# x2.draw()
# if x1*x2:
#     print("The lines\n{0}\n{1}\nintersect at {2}".format(x1,x2,x1*x2))

# x3 = MyLine("(-4/5)*x+5", options = "lambda")
# x3.draw()

# plt.show()

    

# Multiple Arguments
# **x creates a dictionary, *x creates a tuple

# def f(**x):
#     print(x)
#     print(x['good'])
#     print(x.get('good'))

# f(good='ugly', bad=1, love=True)

# output:
# {'good': 'ugly', 'bad': 1, 'love': True}
# ugly
# ugly

# def f(*x):
#     print(x)

# f()
# f(1,2,3)
# f("dog", True, 1)

# output:
# ()
# (1, 2, 3)
# ('dog', True, 1)'

# def f(*x):
#     print(x)

# print("Example 1 -------------------")
# f()
# f(1)
# f(1,"cat")
# f("dog",43,[1,2])

# def f1(*x, **y):
#     if y.get("animal") == "check":
#         if 'dog' in x or 'cat' in x:
#             print("cuteness detected")
#         else:
#             print("Nothing here, citizen")

    
# print("Exmple 2 ---------------------")
# f1(animal = "check")
# f1(1,animal = "check")
# f1(1,"cat",animal="check")
# f1("dog",43,[1,2],animal="check")

# def g1(*x, **options):
#     if options.get("operation") == "sum":
#         return sum(list(x))
#     elif options.get("operation") == 'prod':
#         xp = 1
#         for i in x:
#             xp *= i
#         return xp
#     else:
#         return "No operation specified"

# print("Example 3 ----------------")
# print(g1(1,2,3,4,5))
# print(g1(1,2,3,4,5, operation = "sum"))
# print(g1(1,2,3,4,5, operation = "prod"))


# class Queue:

#     def __init__(self):
#         self.q = np.zeros(size,dtype = int)
#         self.ptr = 0
#         self.empty = True
#         self.full = False

#     def enqueue(self, x):
#         if not self.full:
#             self.q[self.ptr] = x
#             self.ptr += 1
#             self.empty = False
#             if self.ptr == size:
#                 self.full = True
#                 self.ptr = 1 
#         else:
#             print("{0} cannot be added to Q full".format(x))

#     def dequeue(self):
#         if not self.empty:
#             front = self.q[0]
#             self.ptr -= 1
#             self.full = False
#             if self.ptr == -1:
#                 self.empty = True
#                 self.ptr = 0
#             else:
#                 for i in range(1,size):
#                     self.q[i-1] = self.q[i]
#             return front
#         else:
#             return "Q is empty"

#         return "=>{0} empty({1}) full({2}) \ n{3}".format(self.ptr, self.empty, self.full, self.q)

# x = Queue()
# print(x)
# x.enqueue(13) #1st item
# print(x)
# x.enqueue(34) #2nd
# print(x)
# x.enqueue(1000) #3rd
# print(x)
# x.enqueue(-1000) #4th
# print(x)
# x.enqueue(823) #5th
# print(x)
# x.enqueue(794) #full
# print(x)
# ###########
# print("\nremoving\n")
# y = x.dequeue()
# print(y)
# print(x)
# y = x.dequeue()
# print(y)
# print(x)
# y = x.dequeue()
# print(y)
# print(x)
# y = x.dequeue()
# print(y)
# print(x)
# y = x.dequeue()
# print(y)
# print(x)
# y = x.dequeue()
# print(y)
# print(x)

#I have no idea what is wrong with this, this stuff makes no sense; ask

#Queue with lists
# class Queue:
#     def __init__(self):
#         self.q = []
#     def enqueue(self,x):
#         self.q.append(x)
#     def dequeue(self):
#         return self.q.pop(0)
#     def empty(self):
#         return len(self.q) == 0
#     def size(self):
#         return len(self.q)


#Merge Sort

def merge(L,R):
    lst = []
    while not (len(L) == 0 or len(R) == 0):
        if L[0] < R[0]:
            lst.append(L[0])
            L.remove(L[0])
        else:
            lst.append(R[0])
            R.remove(R[0])
    if not len(L) == 0 or not len(R) == 0:
        lst.extend(R or L)
    return lst

def ms(a):
    q = Queue()
    aa = [q.enqueue([x]) for x in a]
    while q.size() > 1:
        L = q.dequeue()
        R = q.dequeue()
        q.enqueue(merge(L,R))
    return q.dequeue()

print("Non-recursive Merge Sort")
a = gen_data()
print(a)
a = ms(a)
print(a)
    