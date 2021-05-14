ex_f = lambda x: x**6 - x - 1               #Equation 6; done by hand
ex_fp = lambda x: 6*(x**5) - 1              #Equation 7; an approximation

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)      #Equation 5

def newton(f,fp,x,tau,iterations):
    def n(x,i):
        while f(x) > tau and i < iterations:
            print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
            x = x - f(x)/fp(x)
            i += 1
        return x
    n(x,0)

if __name__ == "__main__":
    # newton(ex_f, ex_fp, 1.5, .0001)
    # newton(ex_f,fpa(ex_f), 1.5, .0001)
    # To Do: put input statements here
    # 'input()' statements only go here
    #  You need to be familliar with eval() to complete this problem
    Function = input("Funtion ")
    bound = float(input("tau: "))
    start = float(input("x0: "))
    iterations = int(input("iterations: "))
    newton(eval("lambda x: " + Function),ex_fp,start,bound,iterations)

    Function = input("Funtion ")
    bound = float(input("tau: "))
    start = float(input("x0: "))
    iterations = int(input("iterations: "))
    newton(eval("lambda x: " + Function),ex_fp,start,bound,iterations)
    
    Function = input("Funtion ")
    bound = float(input("tau: "))
    start = float(input("x0: "))
    iterations = int(input("iterations: "))
    newton(eval("lambda x: " + Function),ex_fp,start,bound,iterations)


"""
Output from Newton.py
0 1.50000 8.89062
1 1.30049 2.53726
2 1.18148 0.53846
3 1.13946 0.04924

4 1.13478 0.00055
0 1.50000 8.89062
1 1.30049 2.53726
2 1.18148 0.53846
3 1.13946 0.04924
4 1.13478 0.00055
"""