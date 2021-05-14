# If the word length characters are =, return True else, False

# def remove(xlist, y):
#     xtemp = []
#     while xlist:
#         if xlist[0] != y:
#             xtemp += [xlist[0]]
#         else:
#             return xtemp + xlist[1:]
#         xlist = xlist[1:]
#     return xtemp

# def is_anagram(xstring,ystring):
#     xlist, ylist = list(xstring), list(ystring)
#     if len(xlist) != len(ylist):
#         return False
#     else:
#         for i in xlist:
#             ylist = remove(ylist, i)
#         return bool(not ylist)

# words = [["bat","tab"],["butt", "tub"],["evilrats","livestar"],["123","112233"]]

# for w in words:
#     print(is_anagram(w[0],w[1]))

#Sorts the numbers in xlist to ascending order

# def g(xlist):
#     h = xlist[0]
#     for i in range(1,len(xlist)):
#         if h > xlist[i]:
#             h = xlist[i]
#     return h

# def v(xlist,y):
#     xtemp = []
#     cnt = 0
#     while xlist:
#         if xlist[0] != y:
#             xtemp += [xlist[0]]
#         else:
#             cnt += 1
#         xlist = xlist[1:]
#     return [xtemp,[y,cnt]]

# def z(xlist):
#     newlist = []
#     while xlist:
#         m = g(xlist)
#         n = v(xlist,m)
#         xlist = n[0]
#         newlist += [n[1][0]]*n[1][1]
#     return newlist

# xlist = [[1,2,3,1,3,1], [52,42,1], [1,400,1]]

# for x in xlist:
#     print(z(x))

# import random as rn 

# rolls = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

# for i in range(100):
#     d1,d2 = rn.randint(1,6),rn.randint(1,6)
#     rolls[d1+d2] += 1

# print(rolls)
# max = 1

# for i in rolls.keys():
#     if rolls[i] > rolls[max]:
#         max = i

# print("The max roll is {0}={1}".format(max,rolls[max]))

#Dice rolling for certain values

# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         p = 1
#         for i in range(x,0,-1):
#             p = p*i
#         return p

# def choose(x,y):
#     return fact(x)/(fact(y)*(fact(x-y)))

# print(int(choose(5,3)))
# print(int(choose(5,0)))
# print(int(choose(16,4)))

# A function for combinations

# def occurs(xlist,y):
#     found = False
#     while not found and xlist:
#         if xlist[0] == y:
#             found = True
#         xlist = xlist[1:]
#     return found

# print(occurs([1,2,1,2],1))
# print(occurs([1,2,1,2],2))
# print(occurs([1,2,1,2],3))

#Program that uses a while loop to see if something reoccurs in a list

# inputs = [0,1]

# for A in inputs:
#     for B in inputs:
#         print(A,B, int(not (A or B)) == int(not A and not B))

# for A in inputs:
#     for B in inputs:
#         print(A,B, int(not (A and B)) == int(not A or not B))

#Demorgans Law

#Midterm Practice Check

# five = "*"
# four = 4*len(five)
# four = list ('[' + four*five + ']')
# four = four[1:] + [four[0]]
# print(four)

# d = {0:1, 1:2, 2:3, 3:3}
# x = 0
# while d[x] < d[d[x]]:
#     print("hello")
#     x = (x+1) % 4

# input()

# d = {0:1, 1:2, 2:3, 3:3}
# x = 0
# while d[x] <= d[d[x]]:
#     print("bye")
#     x = (x+1) % 4

# x = list(range(2,22,7))
# y = list(range(101,0))
# z = list(range(5,3,-1))

# print(z+2*y+x)

# for i in range(10,21,3):
#     print(i)

# i = 10
# while i < 21:
#     print(i)
#     i = i + 3

# def implication(A,B):
#     if A and B == True:
#         return 1
#     if A == True and B == False:
#         return 0
#     if A == False:
#         return 1

# x = [0,1]
# print("{0:<4} {1:<4} {2:<0}".format('A','B','A -> B'))
# for A in x:
#     for B in x:
#         print("{0:<4} {1:<4} {2:<0}".format(A,B,implication(A,B)))


# x = 1
# y = 2*x
# def f1(x,y):
#     x = x + y
#     print(x,y)
#     def f11(y,x):
#         y,x = x,y
#         print(x,y)
#         def f3(y):
#             y = 2*x
#             print(x,y)
#         f3(3)
#     print(x,y)
#     f11(x+1,y)
# f1(x,y)
# print(x,y)


# xlst = ["44",44,3]
# def sum(weirdList):
#     sum = int(xlst[0]) + xlst[1] + xlst[2]
#     return sum

# print(sum(xlst))

# d = {1:"good",2:"bad",3:"ugly"}
# i = 0
# # while d.keys():
# #     print(d[i])
# d = d[1:]


def insertion_sort(a,size):
    i = 1
    while i < size:
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1], a[j]
            j -= 1
        i += 1

a = [42,2,1,13,1]

print(insertion_sort(a,len(a)))


# def removeLetters(str1,str2):
#     tmp = []
#     for i in str2:
#         if i not in str1:
#             tmp += [i]
#     return "".join(tmp)


# s = "The lazy brown cow as jumped over by the dog"
# t = "ezcowy"

# print(removeLetters(t,s))

# primes = []
# for possiblePrime in range (2,100):
#     isPrime = True
#     for num in range(2, possiblePrime):
#         if possiblePrime % num == 0:
#             isPrime = False

#     if isPrime:
#         primes.append(possiblePrime)

# print(primes)