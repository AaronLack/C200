import matplotlib.pyplot as plt

### TODO: Answer question in the comments here
# It is very difficult to notice a pattern here, however I made many test cases and here is what I found:
# I am noticing when a number is odd, there are more recursive calls and more numbers that are outputed
# When a number is even, not as many values print or are displayed on the graph
# For example, 92 had less recursive calls then 92 then 91
# On the other hand, 1000 has more calls than 1003.  
# So in conclusion I am not noticing any specific pattern.  


xlst, ylst = [],[]

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

def g(n,i):
    xlst.append(i)
    ylst.append(n)
    if n == 1:
        print(str(n) + " ", end = "")
        return 1
    else:
        print(str(n) + " ", end = "")
        return g(f(n), i+1)
        

if __name__ == "__main__":
    # g(26,0)
    g(27,0)
    # g(91,0)
    # g(92,0)
    # g(1000,0)
    # g(1003,0)
    # g(10000,0)
    # g(10,0)
    xmax = max(tuple(xlst))
    ymax = max(tuple(ylst))
    print("\nNumber of recursive calls: {0}\nMaximum number: {1}".format(xmax,ymax))
    plt.plot(xlst,ylst,'r--')
    plt.axis([0,xmax,0,ymax])
    plt.show()