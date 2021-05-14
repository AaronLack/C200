#Create a function that converts dollars to coins
def dollars(x):  
    #Values of coins, using upercase variables
    Q= .25    
    D= .1
    N= .05
    P= .01
    #If/elif statements: using quarters first, then dimes, nickles, pennies
    #I want the program to use the new x value after it goes through the if and elif statements q,d,n,m, but its not
    if x >= Q:
        q = x//Q
        x_1 = x%Q
    else:
        x_1 = x
        q = 0

    if x_1 >= D:
        d = x_1//D
        x_2 = x_1%D
    else: 
        x_2 = x_1
        d = 0

    if x_2 >= N:
        n = x_2//N
        x_3 = x_2%N
    else: 
        x_3 = x_2
        n = 0

    if x_3 >= P:
        p = x_3//P
        x_4 = x_3%P
    else: 
        x_4 = x_3
        p = 0

    xlst = [q,d,n,p] #Lowercase variables to determine the amount of each coin
    return xlst


#Testing paramaters
print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))

if __name__=="main": 
    pass