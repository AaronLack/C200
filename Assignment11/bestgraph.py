import numpy as np 
class Graph:

    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = [] #This sets up an adjacency list

    def add_edge(self,pair):
        start,end = pair        #Start is the key, end is the value in the dictionary
        if start not in self.edges.keys():
            self.edges[start] = [end]
            return 1
        elif end not in self.edges[start]:
            self.edges[start].append(end)
            return 1
        else:
            return -1
    
    def add_node(self,n):
        if n not in self.nodes:
            self.nodes += [n]
            return 1
        else:
            return -1

    def del_node(self,n):
        if n in self.nodes:
            self.nodes.remove(n)
            self.edges.pop(n)       #Pop removes a specific item from a dict
            return 1
        else:
            return -1

    def del_edge(self,x,y):
        if x in self.edges.keys():
            self.edges[x].pop(y)
            return 1
        else:
            return -1
    
    def reachable(self,x,y):
        a = np.zeros ((len(self.nodes),len(self.nodes)), dtype = int)
        for i in self.edges[x]:
            if y in self.edges[i]:
                return True
            else: 
                return False

        print(a)
        a = np.dot(a,a) + a
        print(a)
        a = np.dot(a,a) + a
        print(a)
        a = np.dot(a,a) + a
        print(a)


    def children(self,node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.edges)



#this is just an example
# import numpy as np 
# a = np.zeros ((4,4), dtype = int)
# a[0][1] = 1
# a[1][2] = 1
# a[2][3] = 1
# print(a)
# a = np.dot (a,a) + a
# print(a)
# a = np.dot(a,a) + a
# print(a)
# a = np.dot(a,a) + a
# print(a)

# for i in range(0,4):
#     for j in range(0,4):
#         if not i == j:
#             print("{0} reaches {1}: {2}".format(i+1,j+1,bool(a[i][j])))
