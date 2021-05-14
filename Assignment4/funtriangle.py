#Triangle 1: 

#This is what the structure should look like, now replace with *, Triangle 1 works
for i in range(1,11,1):
    print("*" * i)
    print()
for j in range (9,0,-1):
    print("*" * j)
    print()

#Triangle 2:
#Pattern: a_n = n*(n+1)/2 and -(n*(n+1)/2) respectively

for n in range (1,9,1):
    a_n = (n*(n+1)/2)
    print("*" * int(a_n))
    print()

for n in range(7,0,-1):
    a_n = (n*(n+1)/2)
    print("*" * int(a_n))
    print()

#Triangle 3 

nstar = 21
nspace = 0
for i in range(11):
    print(" " * (nspace+i) + "*" *(nstar-2*i))
    print()
    
if __name__=="main":
    pass
    

