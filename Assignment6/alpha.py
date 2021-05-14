def alphaFunction():
    # Need to read file, and return output of how many times letters (a-z) appear in happy.txt. 
    # Use read function to import file in here, then use a for loop with a dictionary
    
    #This filing path works when I tested it on my MAC desktop
    #The path directory will be different when testing on a different computer
    #I ran into several errors with file I/O reading with just "Assignment6/happy.txt",
    #Stating the file wasn't found unless if I included the full source path for my desktop.  
    
    with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment6/happy.txt","r") as poem:
        x = poem.read()
    
        d = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
            'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}        
        lst = list(x)

        for i in lst:
            if 97 <= ord(i) and ord(i) <= 122:
                d[i] += 1
        return d


for i in alphaFunction().keys():
    print(i + " " + str(alphaFunction()[i]))


# if __name__ = "__main__":
#     pass

