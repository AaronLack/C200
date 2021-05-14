def is_magic(ms):
    row1 = (ms[0][0])+(ms[0][1])+(ms[0][2])
    
    row2 = (ms[1][0])+(ms[1][1])+(ms[1][2])
    
    row3 = (ms[2][0])+(ms[2][1])+(ms[2][2])
    
    column1 = (ms[0][0])+(ms[1][0])+(ms[2][0])
    
    column2 = (ms[0][1])+(ms[1][1])+(ms[2][1])
   
    column3 = (ms[0][2])+(ms[1][2])+(ms[2][2])
    
    if row1 == row2 and row2 == row3 and row1 == row3 and column1 == column2 and column2 == column3 and column1 == column3:
        print("This is a magic Square")
    else:
        print("This is not a magic Squre...hide")

ms = [[4,9,2],[3,5,7],[8,1,6]]

is_magic(ms)

ms = [[4,9,2],[3,5,7],[8,2,6]]

is_magic(ms)

if __name__=="main":
    pass 