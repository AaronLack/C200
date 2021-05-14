x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True

#Problem 1
#Original
if b:
    print("Happy")
if not b and x:
    print("Valentines")
if not b and not x and not y:
    print("day!")

#new
if b:
    print("Happy")
elif not b and not x and not y:
    print("day")
else:
    print("Valentines")


#Problem 2
#Original
if (z > a) or (2*a > z):
    print("C200")
else:
    print("is bliss")

#new (Rewrite as an equivelant two if statements...?)

if (a<z) or (z<2*a):
    print("C200")
else:
    print("is bliss")

#Problem 3
#Original
if not (not (x and y) or not x):
    print(a)

#New (Use Demorgans Law)
if (x or y) and not x:
    print(a)

#Problem 4
#Original
if (2 > z) or x:
    print("1")
elif 2 == 1:
    print("2")
elif y and not x:
    print("3")
else:
    print("4")

#New 
if (2 > z) or x:
    print("1")
if 2==1:
    print("2")
if y and not x:
    print("3")
if a==z:
    print("4")

#Problem 5
#Origional
def f(x):
    return (x==4)*100 + (x==3)*10 + (x==2)*1000 + (x!=4)*(x!=3)*(x!=2) *100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))

#New:
def f(x):
    if (x==4)*100:
        return 100
    elif (x==3)*10:
        return 10
    elif (x==2)*1000:
        return 1000
    else:
        return 100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))

if __name__=="main":
    pass