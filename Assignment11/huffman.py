from Stack import Stack
from bestgraph import Graph

'''
while there are at least two nodes:
find the two smallest counts x,y
create a new node with the count x + y
and annotate x with 0, y with 1

This will produce graph(tree) T. 
Using T, create a dictionary of each letter (make code)
'''

#INPUT huffman tree, current code taken from edges
#OUTPUT build dictionary of words and code

#NOTHING is explicitly returned, it should fill in the dictionary d
#RECURSIVE FUNCTION
#code is a string
# 1 means right, 0 means left for the binary tree

def make_code(xlst,code):
    print("Make code xlst -> " + str(xlst)) #This is how it gets broken up
    if len(xlst) == 3:
        x,y,z = xlst #Breaking up the list into 3 parts
        c1,a1 = y #C1 is character (0 or 1) and a1 is the rest of the list
        make_code(a1, code + c1) #A recursive call with xlst, and the number 0 or 1 added to old code
        c2,a2 = z   #The exact thing as the top but in the case of 2 children
        make_code(a2, code + c2) #A recursive call with xlst, and the number 0 or 1 added to old code    
    else:       #Else case is 1 child or 0 children
        x,y = xlst
        d[x] = code #all you have to do is a final dictionary code

    '''
    pseudocode
    if left:
        reutun 0
    elif right:
        return 1
    slice list
    somehow track all 0's and 1 (code parameter)
    and append that to dicitonary
    '''

#INPUT list of word, count pairs
#OUTPUT huffman tree with a single node
#[node [0 or 1 [node]]]
def make_tree(xlst):
    f = lambda x: x[1] if type (x[0]) == str else x[0] #you need type so the strings don't concatenate
    xlst.sort(key=f)
    while len(xlst) >= 2:
        x = xlst.pop(0) #Removes the items in the list
        y = xlst.pop(0)

        xlst.append([f(x)+f(y),  ['0', x], ['1', y]]) #adds x+y factoring in data types
    return xlst


###DATA
xlst = [['w',7],['u',12],['x',15],['v',18],['y',20]]
d = {}
f = lambda x: x[1] if type(x[0]) == str else x[0]
xlst.sort(key=f) #sorts either original or new nodes 
print('xlst:', xlst) 

xlst = make_tree(xlst)
print('Huffman Tree:', xlst)

make_code(xlst[0],"")

print('d:', d)