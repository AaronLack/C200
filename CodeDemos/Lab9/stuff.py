import random, string

### Generator

def randomValues(maxInt, length):
    """
    Iterator that produces random values
    """
    i = 0
    while i < length:
        yield random.randint(0,maxInt)
        i += 1


### Comprehensions (Dictionary Comprehensions too!)

def dictionary1(letters):
    """
    Given a string of letters, set up a blank counter
    """
    return {L:0 for L in letters}

def dictionary2(flip):
    """
    Assuming unique values, flip the dictionary keys and values
    """
    return {flip[k]: k for k in flip}

def onlyStrings(listOfKeys):
    """
    Provides a counting dictionary that only has keys of strings
    """
    return {k:0 for k in listOfKeys if type(k) == str}

def matrix(rows, columns, defaultValues):
    """
    Create a matrix with a number of rows and colums
    Default value is value for each spot
    """

    return [[defaultValues for c in range(columns)]for r in range(rows)]


def evens(maxNum):
    """
    Create a list of evens from 0 to maximum  number (exclusive)
    """
    return [i for i in range(maxNum) if i % 2 == 0]

#In this example, we are not storing base cases in dictionary
memo = {}
def combinations(n,k):
    if n == k:          #       Base case 1
        return 1
    elif k == 0:                #Base case 2
        return 1        
    else:                       #Inductive Step 
        if (n,k) in memo:       #If the problem has been solved already, stored in a tuple
            print("MEMORY: n = {}, k = {}".format(n,k)) 
            return memo[(n,k)]
        else:
            p1 =combinations(n-1, k)
            p2 = combinations(n-1, k-1)
            memo[(n,k)] = p1 + p2
            return memo[(n,k)]



if __name__ == "__main__":
    ### Generators
    print("Generator")
    g = randomValues(10,10)
    print([x for x in g])
    
    #An Equivelant
    temp= []
    for x in g:
        temp.append(x)
    print(temp)

    ### Dictionary Comprehension
    print() #A blank line easier to read
    print("Dictionary Comprehension")
    print(dictionary1(string.ascii_lowercase))
    print(dictionary1("SICE"))
    temp = {s:i for s,i in zip(string.hexdigits, range(0,16))}
    print(dictionary2(temp))
    values = ["1",1,"2",2,3,"3"]
    print(onlyStrings(values))

    ### List Comprehension
    print()
    print("List Comprehension")
    print(matrix(4,5,'a'))
    print(matrix(5,1,0))
    print(evens(10))

    ### Memoization
    print()
    print("Memoization")
    print(combinations(100,50))
