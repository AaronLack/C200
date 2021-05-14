#Hex must be a string since it has letters 
#Examples: 
# C1 = 193; (12*(16**1))+ (1*(16**0)) = 193
# 7DE = 2014; (7(16**2))+ (13*(16**1)) + (14*(16**0)) 
# (Sn * B**n) is the formal conversion equation; where S = number digit; b = base, n = power


def hex_dec(hex):
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
            'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
   
    base = 16
    power = (len(hex))
    Sum = 0
    for i in list(hex):
        value = d[i]
        power = power -1
        Sum += value*(base**power)
    return Sum

if __name__=="__main__":
    hex = input("Hex: ")
    print(hex_dec(hex))