# Comment out the for loops and first build all the recusrion functions, uncomment later

#Questions:
#  When plugging in a range of 0,999 for s, the maximum recursion depth error I got was 995 times.

# P(30) has a value of 1811.3615841033534, 
# it took 9 minutes and 57 seconds to calculate (via stopwatch on my phone)

# Function b(n) outputs a fibonnaci sequence of numbers.  


# Problem 1
def s(n):
    if n == 0:
        return 0
    else:
        return s(n-1) + n

# for n in range(0,10):
#     print(s(n))

# for n in range(0,999):
#     print(s(n))

# Problem 2
def s1(n):
    if n == 0:
        return 0
    else:
        return (n*(n+1))//2

# for n in range(0,10):
#     print(s1(n))

# Problem 3
def p(n):
    if n == 0:
        return 1000
    else:
        return ((p(n-1)) + (0.02*p(n-1)))


# for n in range(0,10):
#     print(p(n))
# print("This is P " + str(p(30)))

# Problem 4
def p1(n):
    if n == 0:
        return 1000
    else:
        return (((1.02)**n) * 1000)

# for n in range(0,10):
#     print(p1(n))

# Problem 5
def b(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return b(n-1) + b(n-2) #n = 3,4,5,...

# for n in range(1,11):
#     print(b(n))


# Problem 6
def c(n):
    if n == 1:
        return 9
    else:
        return (9*c(n-1) + 10**(n-1) - c(n-1))

# for n in range(1,11):
#     print(c(n))

# Problem 7
def d(n):
    if n == 0:
        return 1
    else:
        return (3*d(n-1) + 1)

# for n in range(0,10):
#     print(d(n))

# Problem 8
def d1(n):
    if n == 0:
        return 1
    else:
        return (((3**(n-1)) -1)//2)

# for n in range(0,10):
#     print(d1(n))

# Problem 9
def c18(n,k):
    if k == 0:
        return 1
    elif n == k:
        return 1
    else:
        return (c18(n-1,k) + c18(n-1,k-1))

# print(c18(4,3))

# for k in range(0,10):
#     for n in range(k,10):
#         print("{0},{1},{2}".format(n,k,c18(n,k)))

# Problem 10 
# Factorial backwards
def B(n):
    if n == 0:
        return 1
    else:
        Sum = 0
        for k in range(0,n):            #k is the range;
            Sum += -1 * c18(n+1,k) * B(k) /(n+1) #combinatin
            return Sum


# for n in range(0,10):
#     print(B(n)) 
        

if __name__ =="__main__":
    for n in range(0,10):
        print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}"
            .format(s(n), s1(n), p(n), p1(n), b(n+1), c(n+1), d(n), d1(n), c18(n+1,n), B(n)))
        

       

