#Consult At Office Hours, I am Cofused.  
import math
def f(x):
    return 3*(x**2) + 4*x + 2

x = -2/3 + math.sqrt(2)/3j
y = -2/3 - math.sqrt(2)/3j

print(f(x))
print(f(y))

###

import numpy as np 
import math
import numpy as np 
import matplotlib.pyplot as plt 

def q(a,b,c): #figure out how to define x
    discrimanent = (b**2-4*a*c)
    if discrimanent < 0:
        d = (math.sqrt((b**2-4*a*c)*-1))/(2*a)
        print(d)
        e = -b/(2*a)
        print(e)
        x = complex(e,d)
        y = complex(-e,d)
        print("Complex")
        return(x,y)
    else: 
        x = (-b - (math.sqrt(b**2-4*a*c)))/(2*a)
        y = (-b + (math.sqrt(b**2-4*a*c)))/(2*a)
        print("Not Complex")
        return (x,y)
        


print(q(1,3,-4))
print(q(2,-4,-3))
print(q(9,12,4))
print(q(3,4,2))

    
x1,y1 = (q(1,-2,-4)) #x**2 -2*x -4
print(x1,y1)

f = lambda x: x**2 -2*x -4
print(f(x1), f(y1))

#Ploting 
x = np.arange(-4.0, 5.0, 0.2)
plt.plot(x, x**2 - 2*x - 4, 'g--')
plt.plot(x, 3*x**2 + 4*x + 2, 'b--')
plt.plot([-4,4],[0,0], color='k', linestyle='-', linewidth=2)
plt.plot([x1,y1],[0,0], 'ro')
if __name__=="__main__":
    plt.show()
    