def div_9(n):
    y = 0
    z = 0
    for i in range(0,len(str(n))):
        y += int(str(n)[i])
        
    for j in range(0,len(str(y))):
        z += int(str(y)[j])
        
    return y == 0 or z == 9

x = [99,0,18273645,22]


for i in x:
    print(div_9(i))

if __name__=="main":
    pass 