# #Primes
# for x in range(2,6):
#     for m in range(2,6):
#         print(str(x*m) + " ", end = "")

# print("\nSame list but as a set-- observe duplicates are removed")
# lmt = 6
# xlst = {x*m for m in range(2,lmt) for x in range(2,lmt)}
# print(xlst)
# xlst.add(1)
# print(xlst)
# primes = {p for p in range(1,lmt) if p not in xlst}
# print(primes)

# lmt = 50 
# no_primes = {x * multiplier for multiplier in range(2, lmt) for x  in range(2,lmt)}
# no_primes.add(1)
# primes = {p for p in range(1,100) if p not in no_primes}
# print(primes)

# x = [[row] for row in range(0,3)]
# print(x)
# x = [[1] if col == row else [0] for col in range(0,3) for row in range(0,3)]
# print(x)

# xlst = [4,3,2,7,9]

# y = [x for x in xlst]
# print(y)

# y = ["{0} is cool!".format(x) for x in xlst]
# print(y)

# import math
# y = ["{0}**2={1}".format(math.sqrt(x),x)for x in xlst if math.sqrt(x) == int(math.sqrt(x))]
# print(y)

# Select: ["{0}**2={1}".format(math.sqrt(x),x)
# From: for x in xlst
# Where: if math.sqrt(x) == int(math.sqrt(x))]

# x = [x for x in range(0,51) if x%7 == 0]
# print(x)

#Convergence
# f = lambda x: x**6 -x -1
# fp = lambda x: 6 * (x**5) -1

# def newton(f,fp,x,tau):
#     def n(x,i):
#         while f(x) > tau:
#             print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
#             x = x -f(x)/fp(x)
#             i += 1
#         return x
#     n(x,0)

# newton(f,fp,1.5,.001)

#OOD
# import pygame
# import sys

# pygame.init()               #Initial OOD

# BLACK = (0,0,0)
# WHITE= (255,255,255)
# BLUE = (0,0,255)
# GREEN = (0,255,0)
# RED = (255,0,0)
# YELLOW = (255,255,0)

# size = [1000,1000]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("C200 OOD Goodness")

# while True:             #Infinate Loop

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill(WHITE)

#     pygame.draw.rect(screen, RED, [0,0,200,200])
#     pygame.draw.rect(screen, BLUE, [100,300,500,100])
#     pygame.draw.rect(screen, YELLOW, [700,100,750,600])
#     pygame.draw.rect(screen, GREEN, [200,600,300,700])
#     pygame.display.flip()

# class Pet:
#     pass

# x = Pet()
# print(x)
#Output: <__main__.Pet object at 0x10786b1d0>; memory location

# class Pet:
#     #This is the Class Pet
#     def __init__(self,foo):     #__init__(self) is called only once when the object is created
#         self.name = foo
    
#     def get_name(self):
#         return self.name
    
# x = Pet("Ursala")
# y = Pet("Ursala")

# print(x)                #Creates two different instances
#                         #Instance x has a method get_name() that is called return variable self.name
# print(y)
# print(x == y)           #False, different objects; variable is self.variable

# if type(x) is Pet:
#     print("{0} is a Pet".format(x.get_name()))

# print(dir(Pet))            #dir lists all the top level attributes and function
# print(Pet.__dict__)
# print(Pet.__doc__)

# class Pet:
#     #This is the Class Pet
#     def __init__(self,foo):     
#         self.name = foo
    
#     def get_name(self):
#         return self.name
    
# x = Pet("Ursala","A12B")       # Even though they contain the same information ("Ursala", "A12B"),
# y = Pet("Ursala","A12B")       # The two instances are different

# if x == y:
#     print("They are the same.")
# else:
#     print("Different Dogs")

#Output: Different Dogs

# class Pet:
#     #This is class pet

#     def __init__(self,pname,tag):
#         self.name = pname
#         self.tag_id = tag

#     def get_name(self):
#         return self.name
    
#     def get_tag_id(self):
#         return self.tag_id

#     def set_tag_id(self, new_tag):
#         self.tag_id = new_tag

# x = Pet("Ursala", "A12B")
# z = x
# z.set_tag_id("C52C")
# print(z.get_tag_id())       # This assigns the memory location of x to z
#                             # This means they are identical
# if z == x:
#     print("They are the same")      # print(x.get_tag_id()--> C52C)
# else:
#     print("Different Dogs")

#Prints they are the same

# class Pet:
#     #This is class pet

#     def __init__(self,pname,tag):
#         self.name = pname
#         self.tag_id = tag

#     def get_name(self):
#         return self.name
    
#     def get_tag_id(self):
#         return self.tag_id
    
#     def __eq__(self,xpet):                          #Python allows you to determine when 2 objects
#         return self.tag_id == xpet.get_tag_id()     # are the same, here we've decided 
#                                                     # if the tages are the same

# x = Pet("Ursala", "A12B")
# y = Pet("Ursala", "A12B")

# if y == x:
#     print("They are the same")      
# else:
#     print("Different Dogs")

# #Output: They are the same

# class Person:
#     programmer = True

#     def __init__(self,x):
#         self.name = x
    
#     def get_name(self):
#         return self.name

# p1 = Person("Bach")
# p2 = Person("Ada")

# print(p1.get_name())
# print(p1.programmer)

# Person.programmer = False
# print(p2.programmer)

# from datetime import date

# class Person:
#     programer = True

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

#     def older(self,p):
#         return self.get_age() > p.get_age()

# p1 = Person("Bach",(3,31,1685))
# p2 = Person("Ada",(12,10,1815))

# print(p2.get_birthdate())
# print(p2.get_age())
# print(p1.older(p2))

# class Pet:

#     def __init__(self,pname,tag):
#         self.name = pname
#         self.tag_id = tag

#     def get_name(self):
#         return self.name

#     def get_tag_id(self):
#         return self.tag_id

# x = Pet("Ursala","A12B")
# y = Pet("Ursala", "A12B")

# print(x)
# print(y)

# if x == y:
#     print("same doggos")
# else:
#     print("different dawgs")
import numpy as np 
a = np.array([[0,1,],[1,0]])
print(a)
a = a.dot(a) + a
print(a)