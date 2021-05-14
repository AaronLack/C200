import math

#all values $/ounce abbreviated $/0z
Gold = 1503.35      #up 11.00
Silver = 17.91      #up .47
Platinum = 950.60   #down 2.50
Palladium = 1468.82 #down 10.48

Au, Ag, Pl, Pa = "Au", "Ag", "Pl", "Pa" #Makes symbols easier

account = 100000 # $100,000
Au_amt, Ag_amt, Pl_amt, Pa_amt = 0,0,0,0

def holdings():
    print("Your current holdings")
    print("Accoutnt = {0:.2f}".format(account))
    print("Gold         =", Au_amt) 
    print("Silver       =", Ag_amt)
    print("Platinum     =", Pl_amt)
    print("Palladium    =", Pa_amt)
    print()


def preciousMetalToDollars(metal,amt):
    if metal == Au:
        return Gold*amt
    elif metal == Ag:
        return Silver*amt
    elif metal == Pl:
        return Platinum*amt
    elif metal == Pa:
        return Palladium*amt
    
def purchase(metal, amt):
    global account
    global Au_amt
    global Ag_amt
    global Pl_amt
    global Pa_amt
    if metal == Au:
            if Gold*amt <= account:
                Au_amt = amt
                account = account - (preciousMetalToDollars(metal,amt))
                print("You have purchased ", amt, "oz. of ", Gold, "for ", Gold*amt)
            if Gold*amt > account:
                print("You have insufficient funds")
                 
    elif metal == Ag:
        if Silver*amt <= account:
            Ag_amt = amt
            account = account - (preciousMetalToDollars(metal,amt))
            print("You have purchased ", amt, "oz. of ", Silver, "for ", Silver*amt)
        if Silver*amt > account:
            print("You have insufficient funds")
        
    elif metal == Pl:
        if Platinum*amt <= account:
            Pl_amt = amt
            account = account - (preciousMetalToDollars(metal,amt))
            print("You have purchased ", amt, "oz. of ", Platinum, "for ", Platinum*amt)
        if Platinum*amt > account:
            print("You have insufficient funds")
        
    elif metal == Pa:
        if Palladium*amt <= account:
            Pa_amt = amt
            account = account - (preciousMetalToDollars(metal,amt))
            print("You have purchased ", amt, "oz. of ", Palladium, "for ", Palladium*amt)
        if Palladium*amt >= account:
            print("You have insufficient funds")


holdings()

print("{:0.2f}".format(preciousMetalToDollars(Au,4)))
print("{:0.2f}".format(preciousMetalToDollars(Ag,100)))
print("{:0.2f}".format(preciousMetalToDollars(Pa,23)))
print("{:0.2f}".format(preciousMetalToDollars(Pl,17)))

print()
purchase(Au,4)
purchase(Ag,100)
purchase(Pa,23)
purchase(Pl,17)
print()

holdings()

purchase(Pl,100000)

if __name__=="main":
    pass