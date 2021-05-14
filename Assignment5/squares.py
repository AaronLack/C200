def sq(n):
    star = "*"
    space = " "
    # quad = length * width 
    if n > 1:
        print(n*star)
        print(space)
        for i in range(0,n-2):
            print(star + (space*(n-2)) + star)
            print(space)
        print(n*star)
    else:
        print(star)

sq(1)
print()
sq(2)
print()
sq(5)
print()
sq(6)

if __name__=="main":
    pass 