#All Work Here is Solely Mine!

Ap,Bp,Op,ABp = "A+","B+","O+","AB+"
An,Bn,On,ABn = "A-","B-","O-","AB-"

def recieveFrom(x,y):
    if x==Ap:
        if y==Ap or y==An or y==Op or y==On:
            return True
        else:
            return False

    elif x==Bp:
        if y==Bp or y==Bn or y==Op or y==On:
            return True
        else:
            return False

    elif x==ABp:
        if y==Ap or y==Bp or y==Op or y==ABp or y==An or y==An or y==On or y==ABn:
            return True
        else: 
            return False

    elif x==On:
            if y==On:
                return True
            else:
                return False

        
    elif x==Op:
        if y==Op or y==On:
            return True
        else:
            return False
            
    elif x==An:
        if y==An or y==On:
            return True
        else:
            return False

        
    elif x==Bn:
        if y==Bn or y==On:
            return True
        else: 
            return False
    

    elif x==ABn:
        if y==ABn or y==An or y==Bn or y==On:
            return True
        else:
            return False



def donateTo(x,y):
    if x==Ap:
        if y==Ap or y==Bp:
            return True
        else:
            return False

    elif x==Bp:
        if y==Bp or y==ABp:
            return True
        else:
            return False

    elif x==ABp: 
        if y==ABp:
            return True
        else:
            return False

    elif x==On:
        if y==Ap or y==Bp or y==Op or y==ABp or y==An or y==Bn or y==On or y==ABn:
            return True
        else:
            return False

    elif x==Op:
        if y==Op or y==Ap or y==Bp or y==ABp:
            return True
        else:
            return False

    elif x==An:
        if y==An or y==Ap or y==ABn or y==ABp:
            return True
        else:
            return False

    elif x==Bn:
        if y==Bn or y==Bp or y==ABn or y==ABp:
            return True
        else:
            return False

    elif x==ABn:
        if y==ABn or y==ABp:
            return True
        else: 
            return False


x = [Ap, Bp, Op, ABp, An, Bn, On, ABn]

for i in x:
    print(i," donate to ", end="")
    for j in x:
        if donateTo(i,j):
            print(j," ",end="")
    print()
print()

for i in x:
    print(i, "recieve from ", end="")
    for j in x:
        if recieveFrom(i,j):
            print(j, " ", end="")
    print()
__name__ == "main"

#Why are all the blood type values printing for donate and receive?!