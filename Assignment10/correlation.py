import matplotlib.pyplot as plt
import numpy as np
import math

def mean(lst):
    average = sum(lst)/len(lst)
    return average

def sd(xlst):
    r = 0
    for i in xlst:
        r += (i - mean(xlst))**2
    return math.sqrt(r/(len(x) -1))

def r(x, y):
    r = 0
    for i in range(len(x)):
        a = (x[i] - mean(x)) / sd(x)
        b = (y[i] - mean(y)) / sd(y)
        r += a * b
    return r/(len(x) -1)


def theGraph():
    with open('/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment10/acme_zyx.txt') as myfile:
        xlines = [a.split(" ") for a in myfile.read().split("\n")]
   
    xlst = []
    ylst = []

    for i in xlines:
        xlst += [float(i[0])]
        ylst += [float(i[1])]
     
    rValue = r(xlst, ylst)
    print(rValue)

    

    
if __name__ == "__main__":
    x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]
    xlst = []
    ylst = []

    for i in x:
        xlst += [float(i[0])]
        ylst += [float(i[1])]
     
    rValue = r(xlst, ylst)
    print(rValue)
    
    plt.plot([i[0] for i in x],[i[1] for i in x], 'ro')
    t = np.arange(0,6,.1)
    plt.plot(t,t*.65 + .5,'g--')
    plt.axis([0,6,0,6])
    plt.xlabel("A values")
    plt.ylabel("B value")
    plt.title("r = {0:.3}".format(rValue))
    plt.savefig('/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment10/stock.png', dpi = 500) #Saves as a png

    plt.show()
    theGraph()