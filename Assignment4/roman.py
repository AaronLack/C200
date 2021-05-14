#Define a funtion that converts integers to roman numerals
#Input a decimal value n
#Return a string cointaining Roman Numerals
#Work in groups of 10 (0-9),(10,19)...etc. 

# def roman(number):

#     one = "I"
#     five = "V"
#     romanNumber = (number <= 3)*number*one + (number == 4) *(one+five) + (number == 5)*five 
#     print("{0:<4} {1:<4}".format(number, romanNumber))

# for number in range(1,6):
#     roman(number)


#Make Lists


def roman(n):
    one = "I" 
    four = "IV"
    five = "V"
    nine = "IX"
    ten = "X"
    fourty = "XL"
    fifty = "L"
    ninty = "XC"

    
    xlst = [0,"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX","XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVII","XXVIII","XXIX","XXX","XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL","XLI","XLII","XLIII","XLIV","XLV","XLVI","XLVII","XLVIII","XLIX","L","LI","LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX","LX", "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX","LXX","LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX","LXXXX","LXXXI", "LXXXII", "LXXXIII", "LXXXIV", "LXXXV", "LXXXVI", "LXXXVII", "LXXVIII", "LXXXIX","XC","XCI", "XCII", "XCIII", "XCIV", "XCV", "XCVI", "XCVII", "XCVIII", "XCIX"]
    return xlst[n]
    
        
for i in range(1,100):
    print(roman(i))
         


#Output
for i in range(1,100):
    if i%5 == 0:
        print()
    print(i, roman(i), ", ", end="")

if __name__=="main":
    pass