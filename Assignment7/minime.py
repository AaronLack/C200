# # The following is examples of what Dr. D Coded

# import random as rn 
# testlst = rn.randint(0,10)
# lst = []
# while testlst:
#     lst.append(rn.randint(0,20))
#     testlst -= 1

# print("The list of numbers is:")
# print(lst)

# # Recursive sum
# def rsum(xlst):
#     if xlst:
#         return xlst[0] + rsum(xlst[1:])
#     else:
#         return 0

# # for-loop index
# def fisum(xlst):
#     sum = 0
#     for i in range(0,len(xlst)):
#         sum += xlst[i]
#     return sum

# # while-loop container
# def wcsum(xlst):
#     sum = 0
#     tmp = xlst[:]
#     while tmp:
#         sum += tmp[0]
#         tmp = tmp[1:]
#     return sum

# fns = [rsum,fisum,wcsum]
# for f in fns:
#     print(f.__name__,f(lst))

 # ___________________________________________________________________________________ #
 # My solution/homework

# 1
def min(x,y):
    if x<y:
        return x
    else:
        return y


# print(min(3,4))
# print(min(4,-2))

# 2
def MIN(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], MIN(lst[1:]))

# for -loop and index in list
# 3
def min1(x):
    tmp = x[0]
    for i in x:
        if i < tmp:
            tmp = i
    return tmp 

# for-loop and container
# 4
def min2(x):
    tmp = x[0]
    for i in range(0,len(x)):
        if x[i] < tmp:
            tmp = x[i]
    return tmp

# while-loop and index into list
# 5
def min3(x):
    i = 1
    Min = x[0]
    while i < len(x):
        if x[i] < Min:
            Min = x[i]
        i += 1
    return Min
# while-loop and container
# 6
def min4(x):
    Min = x[0]
    tmp = x[:]
    while tmp:
        if tmp[0] < Min:
            Min = tmp[0]
        tmp = tmp[1:]
    return Min

# 7 (Given)
def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

if __name__ == "__main__":

    x = [1,42,-1,22,0,12]

    mf = [MIN, min1, min2, min3, min4, min5]

    for f in mf:
        print("{0}({1}) = {2}".format(f.__name__,x,f(x)))