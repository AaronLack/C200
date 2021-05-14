def f(x,y,z):
    equation = 11*x*y + 14*y*z +15*x*z
    return equation

def vol(x,y,z):
    return x*y*z == 147840

a,b,c = 2,2,36960

#Everything works, now focus on making loops
#LOOP SEARCH THROUGH POSSIBLE VALUES

heatLoss= f(a,b,c)

for i in range (0,100):
    for j in range (0,100):
        for k in range (0,100):
            if vol(i,j,k):
                if f(i,j,k) < heatLoss:
                    heatLoss = f(i,j,k)
                    print(i,j,k)
                    a,b,c = i,j,k

print("H W L Value")
print(a,b,c,f(a,b,c))

if __name__ == "main":
    pass