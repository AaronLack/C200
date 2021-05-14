#All Work Here is Solely Mine!

def unmarriedTax(income):
    if 0 <= income <= 9700:
        return income*.1
    elif 9701 <= income <= 39475:
        return income*.12
    elif 39476 <= income <= 84200:
        return income*.22
    elif 84201 <= income <= 160275:
        return income*.24
    elif 160726 <= income <= 204100:
        return income*.32
    elif 204101 <= income <= 510300:
        return income*.35
    elif income >= 510301:
        return income*.37

income = int(input("Amount of income in USD income: "))
print("{} amount taxes owed" .format(unmarriedTax(income)))

def marriedTax(income):
    if 0 <= income <= 19400:
        return income*.1
    elif 19401 <= income <= 78950:
        return income*.12
    elif 78951 <= income <= 168400:
        return income*.22
    elif 168401 <= income <= 321450:
        return income*.24
    elif 321451 <= income <= 408200:
        return income*.32
    elif 408201 <= income <= 612350:
        return income*.35
    elif income >= 612350:
        return income*.37

income = int(input("Amount of income in USD income: "))
print("{} amount taxes owed" .format(marriedTax(income)))

def tax(income, maritalStatus):
    if(maritalStatus):
        return marriedTax(income)
    else:
        return unmarriedTax(income)

#######
#Data
#######

UrsalaIncome, UrsalaMarried = 160726, True
KaiserIncome, KaiserMarried = 501000, True
ShilahIncome, ShilahMarried = 20, True

print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))


#######
#Data
#######

UrsalaIncome, UrsalaMarried = 204099, False
KaiserIncome, KaiserMarried = 510310, False
ShilahIncome, ShilahMarried = 9400, False

print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

__name__ == "__main__"

#Is there anything unusual that you'd observe from the two different taxes-married and unmarried?

# The amount of income and the ranges of income for married people is much higher than not married 
# people. This can be slightly unfiar because for example, an unmarried person who makes $40,000 owes 
# the government 22% of his/her income however a married couple who's income is $40,000 only 
# owes the government 12% of their income.  This is kind of unusuall because both households 
# make the same amount however one's maritial status effects how much one owes to the 
# government in taxes.  