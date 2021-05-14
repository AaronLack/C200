def f(x,y):
    def g(x,z):
        if x + z < 2:
            return x+z+10
        else:
            return x+z/10
        
        if x+y>5:
            return g(y,x-10)
        else:
            return g(2*x,y+1)

def g(x,y,z):
    return f(x,3)

def h(a,b,c,d):
    return f(a,b+d) - g(c-d,a,a+c)

x=1
y=2
x=h(x,y,0,3)
y=g(x+h(-10,2,0,30),x+y,h(0,1,2,3))
print(x,y)