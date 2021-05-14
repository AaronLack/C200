#All Work Here Is Solely Mine

import math

APR = float(input("What is your APR?"))
C = float(input("What is the amount owed on the credit card"))
p = float(input("What is the monthly payment made: $ "))
i = (APR/100)/12

n = -(math.log(1-((i*C)/p)))/(math.log(i+1))


print("You'll make", math.ceil(n),"payments.")