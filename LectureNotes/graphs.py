#Qucksort

# import random as rn 
# xlst = []
# for i in range(0,20):
#     xlst.append(rn.randint(0,100))
# print("Unsorted random list...")
# print(xlst)

# def quicksort(xlst):
#     if len(xlst) == 0:
#         return []
#     elif len(xlst) == 1:
#         return [xlst[0]]
#     else:
#         pivot = xlst[0]
#         rest = xlst[1:]
#         left = []
#         right = []
#         for i in rest:
#             if i <= pivot:
#                 left.append(i)
#             else:
#                 right.append(i)
#         return quicksort(left) + quicksort(right)

# ylst = quicksort(xlst)
# print("Sorted list...")
# print(ylst)

#Finance OOD Problem

import datetime
class Account:
    def __init__(self, name, checking, savings):
        self.name = name
        self.checking = checking
        self.savings = savings

    def deposit(self,account,amount):
        if account == "checking":
            self.checking += amount
        elif account == "savings":
            self.savings += amount

    def get_name(self):
        return self.name

    def __str__(self):
        return "{0}\n{1}nChecking: ${2:.2f}\nSavings: ${3: .2f}".format(self.get_name(), datetime.datetime.now().replace(microsecond=0), self.checking, self.savings)
        
    def cut_check(self, amt):
        if amt <= self.checking:
            self.checking -= amt
            return amt
        else:
            return 0

    def withdrawal(self, amt):
        if amt <= self.savings:
            self.savings -= amt
            return amt
        else:
            return 0

    def transfer(self,act,amt):
        if act == "checking":
            if amt <= self.checking:
                self.savings += amt
                self.checking -= amt
                return True
            else:
                return False
        elif act == "savings":
            if amt <= self.savings:
                self.checking += amt
                self.savings -= amt
                return True
            else:
                return False
    

Ursala = Account("Ursala", 1000, 1000)
Kaiser = Account("Kaiser", 40, 100)
Shilah = Account("Shilah", 200, 200)

Ursala.transfer("savings", 499)
Kaiser.deposit("checking", Ursala.cut_check(123))
Shilah.deposit("savings", Kaiser.withdrawal(69))

print(Ursala)
print(Kaiser)
print(Shilah)

# I am getting memory locations only print and not the actual results.  
# I need help understanding OOD

            
#Graphs

# class Graph:
#     def __init__(self,nodes):
#         self.nodes = nodes
#         self.edges = {}
#         for i in self.nodes:
#             self.edges[i] = []
        
#     def add_edge(self, pair):
#         start,end = pair
#         self.edges[start].append(end)
#     def children(self, node):
#         return self.edges[node]
#     def nodes(self):
#         return str(self.nodes)
#     def __str__(self):
#         return str(self.edges)

# g = Graph([1,2,3,4,5])
# elst = [(1,2), (1,3), (2,4), (4,1), (3,3), (3,4), (3,2), (5,4), (5,3)]
# for i in elst:
#     g.add_edge(i)
# print(g)

#Perceptron:
#randomly assign weight values (small +/- numbers)
#for T iterations:
#     for each input vector:
#         update weights
# return weights

# f = [[[-1,0,0], 0], [[-1,0,1],1], [[-1,1,1],1]]
# weights = [-.05,-.02,.02]

# for i in range(0,10):
#     print(weights)
#     update(weights, f[i%4])
#     test(weights,f)

#Incomplete code, idk how to fix cuz im dumb

#DFS

# def dfs(g,node):
#     visited = []
#     s = Stack()
#     s.push(node)
#     while not s.emtpy():
#         nnode = s.pop()
#         if nnode not in visited:
#             #print(nnode) prints each node as it's visited
#             visited.append(nnode)
#             clist = g.childeren(nnode)
#             for n in clist:
#                 if n not in visited:
#                     s.push(n)
#     return visited

#BFS
# def bfs(g,node):
#     visited = []
#     q = Queue()
#     q.enqueue(node)
#     while not q.empty():
#         nnode = q.dequque()
#         if nnode not in visited:
#             #print(nnode) prints each node as it's visited
#             visited.append(nnode)
#             clist = g.children(nnode)
#             for n in clist:
#                 if n not in visited:
#                     q.enqueue(n)
#     return visited

# Warshall's Algorithm

# import numpy as np 
# a = np.array([[0,0,1,0],[1,0,0,1],[0,0,0,0],[0,1,0,0]])
# print(a)

# a = a.dot(a) + a
# print(a)

# a = a.dot(a) + a
# print(a)

# a = np.array([[0,0,1,0],[1,0,0,1],[0,0,0,0],[0,1,0,0]], dtype = bool)
# print(a)

# a = a.dot(a) + a
# print(a)

# a = a.dot(a) + a
# print(a)

