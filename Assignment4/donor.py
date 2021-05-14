import os

#blood bank type: units
bank = {"A+":5, "A-":6, "O+":4, "O-":2, "B+":5, "B-":6, "AB+":7,"AB-":8} #"A+" is the key, 5 the value
donorReceiver = {
    "O-": ("O-","O+","A+","A-","B+","B-","AB+","AB-"),
    "O+":("O+","A+","B+","AB+"), 
    "A-":("O-","O+","A+","A-",), 
    "A+":("A+","AB+"),
    "B+":("B-","B+","AB+","AB-"),
    "B-":("B-","B+","AB+","AB-"),
    "AB-":("AB+","AB-"),
    "AB+":("AB+")   }

#Input donor's blood type donorBloodType
#Return a tuple of the types that can accept the blood

#Lets use a for loop to look for stuff in the dictionaries make, how to do?
# How do I know if this is correct?
def red_blood_compability(donorBloodType):
    if donorBloodType == "O- ":
        return ("O-","O+","A+","A-","B+","B-","AB+","AB-")
    elif donorBloodType == "O+ ":
        return ("O+","A+","B+","AB+")
    elif donorBloodType == "A- ":
        return ("O-","O+","A+","A-")
    elif donorBloodType == "A+ ":
        return ("A+","AB+")
    elif donorBloodType == "B+ ":
        return ("B-","B+","AB+","AB-")
    elif donorBloodType == "B- ":
        return ("B-","B+","AB+","AB-")
    elif donorBloodType == "AB- ":
        return ("AB+","AB-")
    elif donorBloodType == "AB+":
        return ("AB+")

# Show the current bank stock
def showBank():
    print("Current Blood Bank")
    print("{0:4} {1:>5}".format("Type","Units"))
    for k,v in bank.items():
        print("{0:>4} {1:>4}".format(k,v)) #k = Type, v = Units

#Show number of units of particular type in the bank
def showTypeInBank(bloodType):
    units = bank[bloodType]
    print("{0:>1} units of {1:>2} in bank".format(units, bloodType))


def transfusion(donor,recipient,pints):
    if ((pints<=bank[donor]) and (recipient in donorReceiver[donor])):
       bank[donor] = bank[donor] - pints
       return 1
    else:
        return 0

###############################
#TESTING 
#Shows current Bank
showBank()
os.system("pause")

#Enough A+==5 units, and 4 can be given to AB+
#Result is A+==1
if (transfusion("A+","AB+",4)):
    print("Transfusion successful")
else:
    print("Transfusion failed")
showTypeInBank("A+")
input("pause")

#Fail because O+ cannot donate to B-
if (transfusion("O+", "B-",1)):
    print("Transfusion successful")
else:
    print("Transfusion failed")

#Fail because insufficient units of blood
if (transfusion("A-","O-",7)):
    print("Transfusion successful")
else:
    print("Transfusion failed")

#Succeed and AB-==0 at end
if (transfusion("AB-","AB+",8)):
    print("Transfusion successful")
else:
    print("Transfusion failed")
showTypeInBank("AB-")
input("pause")

showBank()

if __name__ == "main":
    pass