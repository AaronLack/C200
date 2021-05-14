def occurencesWhile(lst, var):
    """
    Using a while loop, find the number of occurences in the list
    """
    # we know we are returning a number
    # the number represenents the number of occurences
    numberOfFinds = 0
    i = 0 # List starts at 0 (first index)
    while len(lst) > i: # can also write while i < len(lst): 
        currentValue = lst[i]
        if currentValue == var:
            numberOfFinds += 1 # numberOfFinds = numberOfFinds + 1
        i += 1
    return numberOfFinds


def occurencesWhileList(lst,var):
    """
    Using a while loop, find the number of occurences in the list. 
    The exception is, you must use lst as the condition
    """
    item = 0
    while lst: # while the lst is NOT empty
        if lst[0] == var:
            item += 1
        lst = lst[1:len(lst)] # slicing
    return item


def operationList(opsList, opp):
    """
    Given a list of lists, where each inner list has a size > 0

    using the operation provide:
    - subtract: s
    - multiply: m
    - addition: a

    Apply that to a whole list
    """

    resultingList = []
    index1 = 0
    
    while index1 < len(opsList):
        currList = opsList[index1]
        if opp == "m":
            currResult = 1
        else: 
            currResult = 0
        index2 = 0
        while index2 < len(currList):
            if opp == "m":
                currResult *= currList[index2]
            elif opp == "a":
                currResult += currList[index2]
            else: # elif opp ==  "s":
                currResult -= currList[index2]
            index2 += 1
        index1 += 1
        resultingList += [currResult]
    return resultingList

def evenCount2(dictionary):
    count = 0
    for key in dictionary: # for key in dictionary.keys()
        if key % 2 == 0:
            count += 1
        return count
