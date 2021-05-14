ex_f = lambda x: x**6 - x -1

def sign(x):
    if x <= 0:
        return -1
    else:
        return 1

def bisect(f,a,b,tau):
    #To Do: Implement funtion
    #variable c is from the algorithmic specification of the bisextion method seen above
    while True:
        c = (a+b)/2                     #B1
        if b-c <= tau:
            break                  #B2
        else:
            if sign(f(b)) * sign(f(c)) <= 0:
                a = c
            else:                       #In this case, you need to repeat step B1
                b = c
    print("{0:5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))



bisect(ex_f, 1.0, 2.0,.001)

#More of my testing cases
bisect(ex_f, -1.0, 2.0,.001)
bisect(ex_f, 1.0, -2.0,.001) 