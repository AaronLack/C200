import math

#1
def y(d,r,t):
    return d*math.e**(r*t)

print(y(1000,.02,10))

#2

def N(n_O, m, t):
    return n_O*math.exp(m*t)

print(N(500,100,4))

#3  
def N_t(t):
    return 71.8 * math.exp(-8.96 * math.exp(-0.0685 * t))

print(math.floor(N_t(1000)))
#4
def K(t):
    return ((9/2.6)*t)/(2*t**2 +3)

print(K(1))

#5
def r(t):
    return 1.5207*t**4 - 19.166*t**3 + 62.91*t**2 + 6.0726*t +1026

print(r(4))

#6
def p(x):
    return 4*x**2 - 100*x -1000

print(p(10))

#7
def W(P_i,P_f):
    return R*T*math.log(P_i/P_f)

R = 8.314 #J/mol
T = 300 #Kelvins

print(W(10,1))

#8
def depreciate(c,s,life):
    return ((c-s)/life)

print(depreciate(20000,1000,5))

#9
def L(k,V,A,C):
    return k*(V**2)*A*C

print(L(.0033,33.8,512,0.515))

#What is this? Ask DR.D
if __name__=="main":
    pass