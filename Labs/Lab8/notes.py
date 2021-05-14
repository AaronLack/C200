# Generators: extended form of looping; iterable; uses yield instead of return
# Lazy programming
# Geerator function is another term for generator
#Ex:
def h():
    x = 0
    while True:
        yield x
        x = x+2

#List Comprehension:
#Syntax: [(select)(from)(where)]

# Ternary Operator
# value_if_true if true_conditoin else vale_if_false
#Ex:

import random
x = random.randint(1,10)
y = 1 if x >5 else 0
print(x,y)

[x for x in range(10)]
# x: is the select, 
# for x in range(10) is the from

[a + "" + for a in words if len(a)>4]
# a + "": select; this is the true value
# for a in words: from
# if len(a)>4: where

#Memoization: A way to do recursion without creating stack calls
#Fibonacci: F(n) = F(n-1) + F(n-2)

#Debugging! 