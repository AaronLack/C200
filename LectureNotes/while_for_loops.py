#Lecture 8, 9/23/19

'''
def generic_function(a,b):
    x = a + b*2
    x = x *3
    return b*2 + a + x

x = 1
y = 2
z = generic_function(x,y)
print(z)

x = "up "
y = "down "
z = generic_function(x,y)
print(z)

x = ["joy", "sun", [1,2]]

#loop over index
print("Loop over Index")
for i in range(0,len(x)):
    print(x[i])

#loop over container
print("Loop over Container")
for i in x:
    print(i)

print("Loop 1")
print(list(range(5)))
for i in range(5):
    print(i)

print("\nLoop 2")
print(list(range(1,5)))
for i in range(1,5):
    print(i)

print("\nLoop 3")
print(list(range(1,5,2)))
for i in range(1,5,2):
    print(i)

print(list(range(5)))
for kitty in range(5):
    print(kitty)

print("\n")
for kitty in range(5):
    print(kitty)
    kitty = 100

print("\n")
for kitty in range(5):
    kitty = 100
    print(kitty)

print("\n")
for kitty in range(5):
    print(kitty)
    kitty = 100
    print(kitty)


import random as rn
xlst = []

for i in range(0,10):
    xlst = xlst + [rn.randint(0,100)]

print(xlst)

import random as rn

def min2(x,y):
    if x>y:
        return y
    else:
        return x

xlst = []

for i in range(0,10):
    xlst = xlst + [rn.randint(0,100)]

print(xlst)

smallest = xlst[0]
for i in range(0,len(xlst)):
    smallest = min2(smallest,xlst[i])

print(smallest)

smile = ":)"
x = ["):", ":)", "(:", ":)", "><"]

cnt = 0
for j in x:
    if smile == j:
        cnt = cnt + 1
print("There are ", str(cnt), smile)


for i in range(0,4,1):
    for j in range(10,14,2):
        print("i = {0}, j = {1}" .format(i,j))


def remove(x,xlst):
    tmp = []
    for i in xlst:
        if i != x:
            tmp += [i]
    return tmp
xlst = [1,2,3,2,1,2,1,2,2,3]

print("original list", xlst)
print(remove(2, xlst))
print(remove(4, xlst))
print(remove(1, xlst))


def double(xlst):
    tmp = []
    for i in range(0,len(xlst)):
        tmp += 2*[xlst[i]]
    return tmp

xlst = [1,"dog",[1,2],"e"]

print("Origional list", xlst)
print(double(xlst))


def keep(xlst):
    tmp = []
    for i in xlst:
        if len(i) <= 2:
            tmp += [i]
    return tmp

xlst = [[1,2,3],["a","b"], [],[1,2,3,4]]

print("origoinal list", xlst)
print(keep(xlst))

def rs(xlst):
    tmp = []
    for i in range(0,len(xlst)):
        if not isinstance(xlst[i],str):
            tmp += [xlst[i]]
    return tmp

x = ["a",1,10,"b",34,3,"c","d"]
print("origional list", x)
print(rs(x))

def merge(xlst, ylst):
    tmp = []
    for i in range(0,len(xlst)):
        tmp += [xlst[i]] + [ylst[i]]
    return tmp

xlst = ["a","b","c"]
ylst = [1,2,3]

print("original lists", xlst)
print("original lists", ylst)
print(merge(xlst,ylst))


def product(xlst,ylst):
    tmp = []
    for i in range(0, len(xlst)):
        tmp += [xlst[i]*ylst[i]]
    return tmp

xlst = [2,1,4,5]
ylst = [1,2,3,6]

print("original lists", xlst)
print("original lists", ylst)
print(product(xlst,ylst))

smile = ":)"
x = ["):", ":)", "(:", ":)", "><"]

cnt = 0
while x:
    j = x[0]
    if j == smile:
        cnt = cnt + 1
    x = x[1:]
print("There are ", str(cnt), ":)")

smile = ":)"
x = ["):", ":)", "(:", ":)", "><"]

def f(x):
    if x:
        if x [0] == smile:
            return 1 + f(x[1:])
        else:
            return f(x[1:])
    else:
        return 0

print("There are ", str(f(x)), ":)")


#Lecture 9, 9/25/19

#Slide 3

for j in range(4):
    for k in range (0,j):
        for m in range (0,k):
            print("{0} {1} {2} {3}".format(j,k,m,j+k+m)) #{0-3} are formal paramaters

A = {1,2,3,4,5,6,7,8,9,10}
B = {5,4,10,124,23,6,9}
for i in A:
    if not i in B:
        print("*",end="")


# Slide 4
def replace(old,new,xlst):
    xtmp = []
    for i in xlst:
        if i == old:
            xtmp += [new]
        else:
            xtmp += [i]
    return xtmp

#Data
x = ["dog",1,2,3,1,2,300,"dog"]
y = ["dog",1,2,3,4,300,400]

for i in y:
    print("\nReplacing {0} with '#'".format(i))
    print(replace(i,"#",x))
'''
#Slide 5: Brute Force

'''
import numpy as np
x = np.arange(1.0,2.0,.1)
y = np.arange(3,4,.1)
def f(x,y):
    return 3*(x**2) - (4*x*y) + 3*(y**2) + 8*x - 17*y +30
a,b = (0,0)

for i in x:
    for j in y:
        if f(i,j) < f(a,b):
            a,b = (i,j)

print(a,b)
print(f(a,b))
print(f(1,7/2))
'''
#Slide 13
'''
from tkinter import *
window = Tk()
window.geometry('350x350')
window.title = ('C200 is worth every penny I spend')

myLabel = Label(window, text="Hello Universe!", font=("Arial Bold", 20))
myLabel.grid(column=0, row=0)

def ClicktheButton():
    myLabel.configure(text="Creativity\nPersistence")

btn = Button(window, text="Click Me", command = ClicktheButton)
btn.grid(column=0,row=7)

window.mainloop()
'''

#Slide 18
'''
x = False
while x:
    print("Hello World!")
print("Yabadabado!")

x = True
while x:
    print("Hello World!")
print("Yabadabado!")

#Slide 27

for i in range(1,5,2):
    print(i)

for i in [1,3]:
    print(i)

i = 1
while i < 5:
    print(i)
    i = i + 2


#Slide 28
#Suppose you have a list of numbers [x,y...z]
#Want to remove w from list
#Have For loop index, for loop list, while loop index, while loop list

def remove_for_index(x,xlst):
    if xlst:
        tmp = []
        for i in range(0,len(xlst)):
            if xlst[i] != x:
                tmp += [xlst[i]]
        return tmp

def remove_for_list(x,xlst):
    if xlst:
        tmp = []
        for i in xlst:
            if i != x:
                tmp += [i]
        return tmp

def remove_while_index(x,xlst):
    i = 0
    tmp = []
    while 0 <= i and i < len(xlst):
        if xlst[i] != x:
            tmp += [xlst[i]]
        i += 1
    return tmp

def remove_while_list(x,xlst):
    i = 0
    tmp = []
    while xlst:
        if xlst[0] != x:
            tmp += [xlst[0]]
        xlst = xlst[1:]
    return tmp


xlst = [1,2,2,4,1,5]

print(remove_for_index(1,xlst))
print(remove_for_list(1,xlst))
print(remove_while_index(1,xlst))
print(remove_while_list(1,xlst))
'''

#Slide 34
'''
for duck in range(3,19,4):
    print(duck)

duck = 3
while duck < 19:
    print(duck)
    duck +=4
'''
#Slide 38
#This loop finds the smallest number in the list
'''
x = [3,0,5,-1]
c = x[0]
for i in range(1,len(x),1):
    if c > x[i]:
        c = x[i]
print(c)

x = [3,0,5,-1]
c = x[0]
i = 1
while i < len(x):
    if c > x[i]:
        c = x[i]
    i += 1
print(c)
'''
# Slide 43
# Example of incorrect calling of list
'''
def f(xlist):
    xtemp = xlist
    xtemp[0] = 34

x = [1,2,3,4]
print(x)
f(x)
print(x)

#To fix
def f(xlist):
    xtemp = xlist[: ] #This makes a so called shllow copy - a different list location
    xtemp[0] = 34

x = [1,2,3,4]
print(x)
f(x)
print(x)
'''
# Slide 45
# Given list xlist and value v, write a function f(xlist, v)
# that returns true if v is in the list, fale otherwise or if list is empty
'''
def f(xlist, v):
    found = False
    if xlist:
        for i in xlist:
            if i == v:
                found = True
    return found

print( f([1,4,2,1],0) ) #False
print( f([1,4,2,1],1) ) #True
print( f([1,4,2,1],[2]) ) #False
print( f([],1) ) #False

#Rewrite as While Loop

def f(xlist, v):
    xtemp =xlist
    found = False
    while xtemp and not found:
        if v == xtemp[0]:
            found = True
        xtemp = xtemp[1:]
    return found

print( f([1,4,2,1],0) ) #False
print( f([1,4,2,1],1) ) #True
print( f([1,4,2,1],[2]) ) #False
print( f([],1) ) #False

def f(xlist, v):
    i = 0
    found = False
    while i < len(xlist) and not found:
        if v == xlist[i]:
            found = True
        i += 1
    return found

print( f([1,4,2,1],0) ) #False
print( f([1,4,2,1],1) ) #True
print( f([1,4,2,1],[2]) ) #False
print( f([],1) ) #False
'''

# Slide 48
# Given a list xlist and value v write a function cnt(xlist,v) that
# returns the number of times v occurs in xlist
'''
def cnt(xlist, v):
    c = 0
    for i in xlist:
        if i == v:
            c = c + 1
    return c

print( cnt([1,4,2,1],0) ) #0
print( cnt([1,4,2,1],1) ) #2
print( cnt([1,4,2,1],[2]) ) #0
print( cnt([],1) ) #0

#Rewrite as a while loop:

def cnt(xlist, v):
    c = 0
    xtemp = xlist[:]
    while xtemp:
        if v == xtemp[0]:
            c += 1
        xtemp = xtemp[1:]
    return c

print( cnt([1,4,2,1],0) ) #0
print( cnt([1,4,2,1],1) ) #2
print( cnt([1,4,2,1],[2]) ) #0
print( cnt([],1) ) #0
'''

#Slide 56: Random number guessing game
'''
import random
x = random.randint(1,100)

g = int(input("Guess: 1-100: "))

while g != x:
    if g > x:
        print("Too high")
        g = int(input("Guess agian "))
    else:
        print("Too low")
        g = int(input("Guess again "))

print("Great job!")
'''

#Slide 58
'''
for big in range(0,4,3):
    print("$", end="")
print()
print(big)

#Rewrite using while loop
big = 0
while big < 4:
    print("$", end="")
    big = big + 3
print()
print(big-3)

#Rewrite using if statements
big = 0
if big < 4:
    print("$", end="")
    big = big + 3
if big < 4:
    print("$", end="")
    big = big + 3
print()
print(big-3)
'''

#Slide 63
'''
i = 10
while i <= 22:
    print(":)", end="")
    i = i + 4

print()

for i in range(0,13,4):
    print(":)", end="")
'''
#Slide 71
'''
t = [[2,5,2],[4],[.4,.1,5]] 
u = []

while t:
    x = t[0]
    y = 1
    while x:
        y = y*x[0] #Multiplies the values in each list per index (2*5*2 is 20, etc)
        x = x[1:]
    u = u + [round(y,2)]
    t = t[1:]

print(u)
'''
#Slide 91
'''
x = {1:"no",2:"yes",3:"maybe"}
print(x)
print(x.keys())
print(x.values())
for i in x:
    print(i)

for i in x:
    print("{0}:{1}".format(i,x[i]))

#Slide 93
x = {1:"no",2:"yes",3:"maybe"}
print("Current dictionary {0}.".format(x))
x[1] = "possibly"
del x[3]

print("Current dictionary {0}.".format(x))

#Slide 95
x = {1:"no",2:"yes",3:"maybe"}

for k,v, in x.items():
    print("The kye is {0} and the value is {1}".format(k,v))

'''
#Slide 99
'''
V = {32:[1,3,'at'], 1:"kitty", "kitty":32}
print(V.keys())
print(V.values())

if V[1] == "kitty":
    print("yes, we have cat")

if "dog" in V.values():
    print("yes, we have puppies")


#Rock Paper Sicsors Game:

import random as rn 

rules = [["r","s"],["p","r"],["s","p"]]

history = {"r":0, "p":0, "s":0}
wins = 0
ties = 0
loses = 0
moves = ["r", "s", "p"]
cnt = 0

def get_best_move():
    m = "r"
    for i in history.keys():
        if history[i] >= history[m]:
            m = i
    for i in rules:
        if i[1] == m:
            return i[0]
print("We'll play 10 games hoomun")
while cnt < 11:
    x = input("play: ")
    history[x] += 1
    if history == 1:
        m = moves[rn.randint(0,2)]
    else: 
        m = moves[rn.randint(0,2)]
        if x == m:
            ties =+ 1
            print("tie")
        elif [x,m] in rules:
            print("human wins {0} beats {1}".format(m,x))
        else:
            loses += 1
            print("robot wins {0} beats {1}".format(x,m))
        cnt += 1

print("human wins : {0}".format(wins))
print("robot wins : {0}".format(loses))
print("ties: {0}".format(ties))
'''
#Lecture 10 9/30/19
'''
for i in '0123':
    print(i,ord(i),bin(ord(i)),hex(ord(i)))

print(13//2, 13%2)
print(6//2, 6%2)
print(3//2, 3%2)
print(1//2, 1%2)

def d_to_b (n):
    y = 0
    p = 0
    while n != 0:
        y = (n%2)*(10**p)+y
        p += 1
        n = n//2
    return y

for i in range(0,16):
    print("{:<3} {:<4}".format(i, d_to_b(i)))


def d_to_b (n,b):
    y = 0
    p = 0
    while n!= 0:
        y = (n%b)*(10**p)+y
        p += 1
        n = n//b
    return y


for i in range(0,17):
    base2 = d_to_b(i,2)
    base3 = d_to_b(i,3)
    print("{:<3} {:<4} {:<3}".format(i,base2,base3))

import random
answer = random.randint(0,100)
while True:
    guess = input("Enter a number between 1 and 100: ")
    try:
        guess = int(guess)
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print("Great Guess!")
            break
    except:
        print("That wasn't a number. ")

'''

import random
colorList = ["black","brown","orange","green","blue","purple","yellow"]
while colorList:
   myColor = random.choice(colorList)
   colorList.remove(myColor)
   print(myColor)
   