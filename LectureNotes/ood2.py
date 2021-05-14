#Imaginary numbers and OOD:

# class MyCN:
#     def __init__(self,rpart,ipart):
#         self.rpart = rpart
#         self.ipart = ipart
#         self.cn = [self.rpart,self.ipart]

#     def get_real(self):
#         return self.rpart
    
#     def get_imag(self):
#         return self.ipart

#     def __str__(self):
#         return str(self.cn)


#     def add(self, ix):
#         real_part = self.get_real() + ix.get_real()
#         imag_part = self.get_imag() + ix.get_imag()
#         iy = MyCN(real_part,imag_part)
#         return iy 


#     def __add__(self, ix):
#         real_part = self.get_real() + ix.get_real()
#         imag_part = self.get_imag() + ix.get_imag()
#         iy = MyCN(real_part,imag_part)
#         return iy 

#     def __mul__(self,other):
#         real_part = self.get_real() * other.get_real() - self.get_imag() * other.get_imag()
#         imag_part = self.get_real() * other.get_imag() + self.get_imag() * other.get_real()
#         iy = MyCN(real_part, imag_part)
#         return iy

# a1 = MyCN(3,-1)
# b1 = MyCN(0,6)
# c1 = a1.add(b1)
# print("{0} + {1} = {2}".format(a1,b1,c1))

# d1 = a1+b1
# print("{0} + {1} = {2}".format(a1,b1,d1))

# e1 = a1*b1
# print("{0} + {1} = {2}".format(a1,b1,e1))

# The Book Problem
# import numpy as np 
# class Book:
#     def __init__(self,title,author,pages,keywords):
#         self.title = title
#         self.author = author 
#         self.pages = pages
#         self.keywords = keywords

# # In the list, its title, author, pages, and keywords. 
# # We set self.whatever = whatever to tell python its OOD.  

#     def __str__(self):          # You're requirement is that you must return a string
#         return " '{0},' by {1}. pages: 1-{2}".format(self.title, self.author, self.pages)

#     def search(self,kwlst):
#         cnt = 0
#         for i in kwlst:
#             cnt += (i in self.keywords) *1
#         return cnt

# blist = [
#     ["Green Eggs & Ham", "Dr. Seus", 62,["foods","colors","health"]],
#     ["Dick & Jane Jump & Run", "Gray & Sharp", 32,["sports", "health"]],
#     ["In Search of Lost Time", "Proust", 4251, ["colors", "health"]]
#         ]

# # dtype Indicates the array we want
# bkarray = np.empty(len(blist), dtype = Book)

# # Creates instances
# for i in range(0,len(blist)):
#     data = blist[i]
#     bkarray[i] = Book(data[0],data[1],data[2],data[3])

# bklst = list(bkarray)

# search_terms = input("Words: ").split(" ")

# bsearch = lambda y: bklst.sort(key = lambda x: x.search(y), reverse=True)
# # We use y for the list of our key terms

#       # In this case, we're return the count of the intersection of the class we wrote
# bklst.sort(key = lambda x: x.search(["colors", "health"]), reverse=True) 
# #This puts in decending order

# bsearch(search_terms) #This sorts the list

# print("HITS TITLE")
# for i in bklst:
#     print("{0}  {1}".format(i.search(["colors", "health"]), i))

# # Prints memory locations without __str()__
# # for i in range(0,3):
# #     print(bkarray[i])

# Stacks

# class Stack: 
#     def __init__(self,):
#         self.stack = []

#     def pop(self):
#         if not self.empty():
#             top = self.stack[0]
#             self.stack = self.stack[1:]
#             return top

#         else:
#             pass

#     def push(self,item):
#         self.stack.insert(0,item)

#     def empty(self):
#         return self.stack == []

#     def get_stack(self):
#         return self.stack

# # s = Stack()
# # t = Stack()

# # s.push(3)
# # s.push(4)
# # s.pop()
# # t.push(":")
# # s.push(t.pop())

# # We can use this to check a balance of ()

# x = ["()(()())", "((()", "())))"]

# balanced = True
# for j in x:
#     s = Stack()
#     for i in j:
#         if i == "(":
#             s.push(i)
#         elif s.empty():
#             balanced = False
#             break
#         else:
#             s.pop()
#     print(balanced and s.empty())

# Matricies

# def mm(a,b):
#     r1,c1 = a.shape
#     r2,c2 = b.shape
#     d = np.zeros(shape=(r1,c2))

#     return d

# import numpy as np 

# a = np.array([[1,2,4],[3,4,3]])
# b = np.array([[-1,0],[1,-5],[-3,1]])
# c = np.dot(a,b)
# print(c)
# d = mm(a,b)
# print(d)