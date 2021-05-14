#TIMER FUNCTION -- deprecated in 3.8 FYI
#so you might get messages -- you can ignore them for now
import time

def ftimer(f,args):
    time_start = time.clock()
    f(args)
    time_elapsed2 = (time.clock()-time_start)
    return time_elapsed2

#1
def even(x):
    if x == 1 or x== 2:
        return 0
    else:
        return x-1 + even(x-1)
    

#2
def odd(x):
    if x == 1 or x == 2:
        return 0
    else:
        return x**2 + 1 + odd(x-1)

#3
#Recursive
#input parameter: n
#OUTPUT RE value
def b(n):
    if n == 1 or n == 2:
        return 0
    else:
        if n%2 == 0:
            return n-1 + b(n-1)
        else:
            return n**2 + 1 + b(n-1)

#4
#TAIL RECURSIVE for function B
# S is like a counter; and you do the math inside the paramater for tail recursion
def btr(n,s):
    if n == 1 or n == 2:
        return s
    else:
        if n % 2 == 0:
            return btr(n-1,s+n-1)
        else:
            return btr(n-1,s + (n**2 + 1))
            

#5 
#MEMOIZATION 
#USE THIS DICTIONARY for function B
d = {2:0,1:0}
def bm(n):
    if n in d.keys():
        return d[n]
    else:
        if n % 2 == 0:
            d[n] = n-1 + bm(n-1)
            return d[n]
        else:
            d[n] = n**2 + 1 + bm(n-1)
            return d[n]


###################################################

#7
def gg(n):
    if n == 0:
        return 1
    else:
        return 1 + 2*gg(n-1)
    

#8 #This is wrong
#TAIL RECURSIVE version of gg
def gtr(n,s=1):
    if n == 0:
        return s
    else:
        return gtr(n-1,1+2*s)

#9
D = {0:1}
def gm(n):
    if n in D.keys():
        return D[n]
    else:
        D[n] = 1 + 2*gm(n-1)
        return D[n]

if __name__ == "__main__":

    # Function numbers 1 - 6

    for i in range(1,10): 
        print("f({0}) = {1}, {2}, {3}".format(i, b(i),btr(i,0),bm(i)))

    fblist = [b, lambda i: btr(i,0), bm ]
    tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
    print(tlist)
    print()

    fglist = [gg, lambda i: gtr(i,0),gm]

    # Function numbers 7 - 9 

    for i in range(0,10):
        print("f({0}) = {1}, {2}, {3}".format(i,gg(i),gtr(i),gm(i)))

    tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
    print(tlist)
