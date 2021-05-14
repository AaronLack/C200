from Queue import Queue
from bestgraph import Graph

def bfsfull(g,node):
    unvisited = g.nodes
    visited = []
    q = Queue()
    q.enqueue(node)
    while not q.isEmpty():
        nnode = q.dequeue()
        if nnode not in visited:
            #print(nnode) prints each node as it's visited
            visited.append(nnode)
            unvisited.remove(nnode)
            print(nnode)
            clist = g.edges[nnode]
            # print(clist)
            for n in clist:
                if n not in visited:
                    q.enqueue(n)

            if len(unvisited) > 0 and q.isEmpty(): #The list has to have items and it must be empty so that it does not default go to the index of the first item in the list (in our case 1).  
                q.enqueue(unvisited[0])
                
                
    # print(visited + unvisited)     
    return visited

if __name__ == "__main__":
    my_graph = Graph([1,2,3,4,5,6,7,8])
    elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
    for i in elst:
        my_graph.add_edge(i)
    print(my_graph.edges)
    bfsfull(my_graph,5)
    