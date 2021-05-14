ex_f = lambda x: x**6 - x -1

def secant(f,x0,x1,tau):
    if abs(x1-x0) < tau:
       return
    else:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
        x2 = (x1 - f(x1) * ((x1 -x0)/(f(x1) - f(x0))))
        x0 = x1
        x1 = x2
        secant(f, x0, x1, tau)
    

    
def secantEC(f,x0,x1,tau):
    while abs(x1-x0) > tau:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
        x2 = (x1 - f(x1) * ((x1 -x0)/(f(x1) - f(x0))))
        x0 = x1
        x1 = x2


if __name__ == "__main__":
    secant(ex_f,2.0,1.0,.0001)
    print()
    secantEC(ex_f,2.0,1.0,.0001)


        