#executes can only be run once so I commented them out for the sake of this example
import sqlite3

dog = sqlite3.connect("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/LectureNotes/example1.db")

c = dog.cursor()

# c.execute('''CREATE TABLE Account (Name text, Checking real, Savings real)''')
# c.execute("INSERT INTO Account Values ('Ursala', 1000, 400)")
# c.execute("INSERT INTO Account Values ('Kaiser', 200, 100)")
# c.execute("INSERT INTO Account Values ('Shilha', 500, 200)")

# dog.commit()


# c.execute('SELECT * FROM Account WHERE checking > 200')
# print(c)
# print(list(c))

# c.execute('SELECT Account.Name FROM Account WHERE Checking != 1000')
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())

#Fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.  

#This method is the same as the one above execpt using a while loop to retireve data in python

# c.execute('SELECT Account.Name FROM Account WHERE Checking != 1000')

# i = 1
# x = c.fetchone()
# while x:
#     print("{0} {1}".format(i,x))
#     i +=1
#     x = c.fetchone()

#This method uses a for loop

# for i in c.execute('SELECT Account.Name FROM Account WHERE Name != "Hours"'):
#     print(i)


# houses = [('123 Mockingird Lane', 100, 2.5), ('5040 RR2 Canine', 400, 1), ('1 Paw Manor', 400, .25), ('1600 Pen Ave', 750, 3), ('107 S Indiana', 850, 2)]

# c.execute('''CREATE TABLE MLS (Address text, Price real, Acres real)''')

# c.executemany('INSERT INTO MLS VALUES (?,?,?)', houses)

# dog.commit()

# for i in c.execute('SELECT * FROM MLS'):
#     print(i)

# x = c.execute("SELECT Account.Name, MLS.Address FROM Account, MLS WHERE Savings + Checking > MLS.Price * .5")

# for i in x:
#     print(i)

#Graphs

# r = [('c', 'a'), ('a','b'), ('a', 'e'), ('c','d'), ('c','f'), ('f','g'), ('f','h'), ('h','j'), ('h','i')]

# # c.execute('''CREATE TABLE G (Parent text, Child)''')

# c.executemany('INSERT INTO G VALUES (?,?)', r)

# dog.commit()

# for i in c.execute('SELECT * FROM G'):
#     print(i)

# for j in c.execute('SELECT G.Child FROM G WHERE G.Parent = "f"'):
#     print(j)

#Prints GrandChildren
# for i in c.execute('SELECT H.Child FROM G, G AS H WHERE G.Parent = "f" and G.Child == H.Parent'):
#     print(i)

#Decendents

q = lambda x: 'Select G.Child FROM G WHERE G.Parent = "{0}"'.format(x)

start = 'c'
xlst = []
qlst = [q(start)]
while qlst:
    for i in list(c.execute(qlst[0])):
        child = i[0]
        xlst.append(child)
        qlst.append(q(child))
    qlst = qlst[1:]

print(xlst)

dog.close()

#For only parents (internal nodes)
# for i in c.execute("SELECT distinct(Parent) FROM G WHERE EXISTS (SELECT child from G)"):
#     print(i)

#For only children (leaves)
# for i in c.execute("SELECT distinct(child) FROM G WHERE child not in (SELECT parent from G)"):
#     print(i)


#Display the graph on a webpage problem:

# import networkx as nx 
# import matplotlib.pyplot as plt 
# import webbrowser

# edge_list = []
# for i in c.execute("SELECT * FROM G"):
#     edge_list.append(i)
# dog.close()

# G = nx.DiGraph()
# G.add_edges_from(edge_list)
# nx.draw(G, with_labels = True)
# plt.savefig("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/LectureNotes/simple_path.png")

# with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/LectureNotes/ursie123.html", "w") as file:
#     file.write("<!DOCTYPE html> \
#         <html> \
#         <body> \
#         <h1> Graph </h1> \
#         <img src = 'simple_path.png' alt = 'graph'> \
#         </body> \
#         <html>")

# webbrowser.open_new_tab("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/LectureNotes/ursie123.html")

