#For loop factorial
def g(n):
    if n == 0:
        return 1
    else:
        prod = 1
        for i in range(2,n+1):
            prod *= i
        return prod

#While loop factorial
def h(n):
    prod = 1
    while n:
        prod *=n
        n -= 1
    return prod

def hp(n):
    prod = 1
    cnt = 1
    while cnt < n + 1:
        prod *= cnt
        cnt += 1
    return prod

#Recursion
def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

#Tail Recursion
def ftail(n,x=1):
    if n == 0:
        return x
    else:
        return ftail(n-1,n*x)

#Generators
def a():
    prod = 1
    n = 1
    while True:
        yield prod
        prod *= n
        n += 1

x=a()
# for i in range(0,6):
#     print(next(x))

#Approximations/Convergence to e:
def approx_e():
    n = 1
    prod = 1
    sum = 0
    while True:
        sum += 1/prod
        yield sum
        prod *= n
        n += 1

x = approx_e()
# for i in range(0,10):
#     print(next(x))

def approxE():
    def f(n):
        prod = 1
        while n:
            prod *= n
            n -= 1
        return prod
    sum = 0
    n = 0
    for i in range(0,7):
        sum += 1/f(n)
        print(sum)
        n += 1
# approxE()

#IMPORTANT
"""
You’ve gone to a fortune teller and discovered the numbers 1,5,9,8 are unlucky for you.  
Write a function that removes these numbers from a string.
Write Python code to take a sentence and purge of any bad mojo numbers.
For example, “You are the 1, I have $1865. Cats have 9 lives.”
Then you’d get “You are the , I have $6. Cats have  lives.”
"""

s = "You are the 1, I have $1865. Cats have 9 lives."
bad_mojo = ["1", "5", "8", "9"]
good = ""
for i in s:
    if i not in bad_mojo:
        good += i
# print(good)


# *args & **kwargs

def foo(required, *args, **kwargs): #aka key word: args
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

#foo('hello', 1,2,3) 
'''
Output:
hello
(1,2,3)
'''
#foo('hello',1,2,3, key1='value', key2= 999)
'''
Output:
hello
(1,2,3)
{'key1': 'value', 'key2': 999}
'''

#####################################################
#Final Practice Exam:
#2
def g1(*x, **options):
    if options.get("operation") == "per":
        return x[0]*(x[1]/100)
    elif options.get("operation") == "div":
        return x[0]/x[1]
    elif options.get("operation") == "min":
        return min(x[0],x[1])
    else:
        return "No opeation specified"

# print(g1,(10,20))
# print(g1(10,20, operation = "per"))
# print(g1(10,20, operation = "div"))
# print(g1(10,20, operation = "min"))

#3 I don't understand this problem
x = "1ABC"
print(len(x))
for i in range(0,len(x)-2):
    print(int(x[i]+x[i+1]+x[i+2],16))


# print(int(x[i],16))             #10
# print(int(x[i+1],16))           #11
# print(int(x[i+2],16))           #12
# print(int(x[i]+x[i+1],16))      #171
# print(int(x[i+1]+x[i+2],16))    #188
# print(int("A0",16))             #160

#7
# f_1 = 2
# f_n = 2a_n-1 + 3

#recursion
def f(n):
    if n == 1:
        return 2
    else:
        return 2*f(n-1) + 3

#memoization
d = {1:2}
def fm(n):
    if n in d.keys():
        return d[n]
    else:
        d[n] = 2*d[n-1] + 3
        return d[n]

#tail recursion
def ftr(n,x=2):
    if n == 1:
        return x
    else:
        return ftr(n-1, 2*x+3)

# for i in range(1,6):
#     print(f(i),fm(i),ftr(i))


x = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
y = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C"]


def roman(number):
    return y[number//10] + x[number%10]

# for i in range(1,100):
#     print(roman(i))

pprint(scientists)