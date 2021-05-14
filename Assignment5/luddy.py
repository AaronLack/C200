import numpy as np 
def area(x,y):
    return x*y==75

def f(x,y):
    return (2*(10*y))+ (10*x) + (5*x) 

#Place some arbitray paramaters
ax = 15
by = 5
minCost = f(ax,by)

# Only 2 for loops, 2 dimensions
for i in range(0,400,1):       # x dimension
    for j in range(0,400,1):   # y dimension
        if f(i/4,j/4) < minCost and area(i/4,j/4):
            minCost = f(i/4,j/4)
            ax,by = i/4,j/4


print(ax,by,f(ax,by))


if __name__=="main":
    pass 
