# Finding the max using a for loop

def maxFor(xlst):
    if len(xlst) == 0:
        return xlst
    tmp = xlst[0]  
    for i in xlst:
        if i > tmp:
            tmp = i
    return tmp


#Finding the max using a while loop
def maxWhile(xlst):
    if len(xlst) == 0:
        return xlst
    tmp = 0
    i = 0  
    while i < len(xlst):
        if xlst[i] > tmp:
            tmp = xlst[i]
        i += 1
    return tmp


#Finding the min using a for loop
def minFor(xlst):
    if len(xlst) == 0:
        return xlst
    tmp = xlst[0]  
    for i in xlst:
        if i < tmp:
            tmp = i
    return tmp


# Removing even numbers from a list using a for loop
# GOOD JOB!
def RemoveEvens(xlst):
    tmp = []
    for i in xlst:
        if i%2 != 0:
            tmp = tmp + [i]
    return tmp

# Replacing an old list with a new list using a for loop
# GOOD JOB!
def myReplace(oldX,num,newX,xlst):
    tmp = []
    for i in xlst:
        if i == oldX:
            tmp = tmp + [newX]
        else:
            tmp = tmp + [i]

    return tmp

# Sum of odd numbers using a for loop
def sumOdd(xlst):
    tmp = 0
    if len(xlst) == 0:
        return xlst
    for i in xlst:
        if i%2 == 1:
            tmp = i+tmp
    return tmp

# Getting string items from a list to join together
def StringConcat(xlst):
    tmp = ""
    for i in xlst:
        i = (str(i))
        tmp = tmp + i
    return tmp


#Data
w = []
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [w,x,y,z] #was called nlst
c = [0,1,1,0,2,1,4]
a = ["a","b","b","a","c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]
d = ["a",1,"row",0,3,"d","ef",453]


print("maxFor_____")
for i in nlst:
    print(maxFor(i))
print("\nmaxWhile_____")
for i in nlst:
    print(maxWhile(i))
print("\nminFor_____")
for i in nlst:
    print(minFor(i))
print("\nRemoveEvens_____")
print(RemoveEvens(b))
print(RemoveEvens(c))
print("\nmyReplace_____")
print(myReplace(1,2,"dog",c))
print(myReplace(1,2,1,b))
print("\nsumOdd_____")
for i in nlst:
    print(sumOdd(i))
print("\nStringConcat_____")
print(StringConcat(a))
print(StringConcat(d))

if __name__=="main":
    pass