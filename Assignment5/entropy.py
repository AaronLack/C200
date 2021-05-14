import math

def makeProbability(xlst):
    dictionary = {} 

    for i in xlst:
        if i in dictionary:
            dictionary[i] += 1/len(xlst)
        else:
            dictionary[i] = 1/len(xlst)
    return dictionary
    

def entropy(xlst):
    entropy = 0
    for i in xlst:
        entropy = -(xlst[i]*math.log2(xlst[i])) + entropy 
    return entropy

#Test Values:
s1 = ['a','b','a','b','a','b','b','b']
s2 = [(1),(2),(3),(4)]
s3 = [1]
s4 = [1,2]
xlst = [s1,s2,s3,s4]
for i in xlst:
    print(entropy(makeProbability(i)))


if __name__=="main":
    pass 
