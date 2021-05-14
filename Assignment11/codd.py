import sqlite3

# I have to use the absolute path here because Mac File I/O is not in line with PC's.  Sorry for the inconvienence, and please for the love of god don't take points off for it
dog = sqlite3.connect("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment11/example1.db")

c = dog.cursor()
r = [('c','a'),('a','b'), ('a','e'),('c','d'),
          ('c','f'),('f','g'), ('f','h'),('h','j'),
          ('h','i')]

c.execute('DROP TABLE IF EXISTS G')
c.execute('''CREATE TABLE G (Parent text, Child)''')

c.executemany('INSERT INTO G VALUES (?,?)', r)

dog.commit()


q = lambda x,y: "Select distinct(G.Parent) FROM G WHERE (Parent, '{}') in G and (Parent, '{}') in G".format(x,y)

# start = 'c'
# xlst = []
# qlst = [q(start)]
# while qlst:
#     for i in list(c.execute(qlst[0])):
#         child = i[0]
#         xlst.append(child)
#         qlst.append(q(child))
#     qlst = qlst [1:]


print(c.execute(q('b','e')).fetchone())
print(c.execute(q('h','g')).fetchone())
print(c.execute(q('e','a')).fetchone())

dog.close()