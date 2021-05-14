#Lecture4 Notes Problems
"""
def E(F):
    return (1/4)*F + 1.7*(F**2)

print(E(10))


def days(year):
    return year * 365

age = int(input("How old are you in years? "))

print("You are", days(age), "days old more or less")


import time
from datetime import date

def days(m,d,y):
    my_birthday = date (y,m,d)
    today = date.today()
    return (today - my_birthday).days

month = int(input("Birthday Month: "))
day = int(input("Birthday Day: "))
year = int(input("Birthday Year: "))

print("You are exactly", days(month,day,year), "days old.")


def FtoK(deg_f):
    def FtoC (deg_f):
        return (deg_f - 32)*(5/9)
    def CtoK(deg_c):
        return deg_c + 273.15
    return CtoK(FtoC(deg_f))

temp_F = -50
temp_K = round(FtoK(temp_F),2)
print(temp_F, "deg Fahrenheit is", temp_K, "eg Kelvin")

"""
#Lecture5 Notes Problems
'''
x = 1

def a(i):
    x = 10
    print(a.__name__ + "(" + str(i) + ")" + " x = " + str(x))

    def b(i):
        x = 100
        print(b.__name__ + "(" + str(i) + ")" + " x = " + str(x))

        def c(i):
            x = 1000
            print(c.__name__ + "(" + str(i) + ")" + " x = " + str(x))

        c(i+1)

    b(i+1)

print(x)
a(1)
print(x)

import math

def OxygenSupply(Hemocrit,a,b):
    # Hemocrit is 0..100
    # H is percentage
    H = Hemocrit/100

    return a*H*math.exp(-b*H)

print(OxygenSupply(30,2,1))

def f(a,b,x):
    if a:
        x = x + 1
    elif b:
        x = x - 1
    return x

x = 5
a = True
b = True
print(x)
print(f(a,b,x))
print(x)
'''

#9/17/19
'''
def X(A,B):
    def M(A,B): 
        return not A and B
    def N(A,B):
        return A and not B
    return int(M(A,B) or N(A,B))

def Y(A,B):
    return A and B

def date_fashion(you,date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def isEven(x):
    return x % 2 == 0

def isOdd(x):
    return not isEven(x)

print(2, isEven(2), isOdd(2))
print(3, isEven(3), isOdd(3))

grade = input("Grade: ")
GPA = 0

if grade == 'A':
    GPA = 4.0
elif grade == 'A-':
    GPA = 3.7
elif grade == 'B+':
    GPA = 3.0
else:
    GPA = -1

print(GPA)


def f(a,b,x):
    if a:
        x = x + 1
    if not a and b:
        x = x - 1
    return x

x = 5
a = True
b = True
print(x)
print(f(a,b,x))
print(x)
'''


#9/18/19
'''
x,y,z = 1,2,10
print(x,y,z)

x,y,z = y+z, z, 100
print(x,y,z)

(x,y) = (1,2)
(x,y) = 1,2
x,y = (1,2)

a,b,c,d,e = "Hello"
print(a,b,c,d,e)
print(a+b+c+d+e)

x = "C200 is a super class!"
print(len(x))
print(x[len(x)-1])
print(x[21])

print(x[0:])
print(x[9:])
print(x[21:])
print(x[22:])

w = [10,9]
x = [1,["dog", [w,3.1415],"dog"],4]
print(x)
print(len(x))
print(x[0])
print(x[1:])
print(x[0::2])

w = [10,9]
x = [1,["dog", [w,3.1415],"dog"],4]
y = [x[1][0],x[1][2]]
w = [x[0],x[1][1],x[2]]

print(y)
print(w)

x = ["cat", [1,2,3], "dog", 100]
for i in x:
    print(i)
'''


for j in range(4):
    for k in range (0,j):
        for m in range(0,k):
            print("{0} {1} {2} {3}".format(j,k,m,k+k+m))

A = {1,2,3,4,5,6,7,8,9,10}
B = {5,4,10,124,23,6,9}
for i in A:
    if not i in B:
        print("*", end="")