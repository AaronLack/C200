import week5 as w5

dictionary1 = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five"}

names = ["Josh", "Josh", "Josh", "Kaitlynne", "Larry", "Teresa", "Sub", "Sub"]

grades = ["A", "B-", "C-", "D", "A", "F", "B+", "A"]

ex3 = [[1, 2, 3], [3, 3, 3], [4], [5, -1, -2]]

print("Testing code from {0} module".format(w5.__name__))
print("Test code being run from this module, {0}".format(__name__))
print("\n"*2)

print("Testing function occurencesWhile")
print("~"*30)
print("Input: {0}, {1}".format(names, "Josh"))
print("Result: {0}".format(w5.occurencesWhile(names, "Josh")))
print()

print("Input: {0}, {1}".format(names, "Nick"))
print("Result: {0}".format(w5.occurencesWhile(names, "Nick")))
print()

print("Input: {0}, {1}".format(grades, "Josh"))
print("Result: {0}".format(w5.occurencesWhile(grades, "Josh")))
print()

print("Input: {0}, {1}".format(grades, "A"))
print("Result: {0}".format(w5.occurencesWhile(grades, "A"))) 
print()
print()
print("Testing function occurencesWhileList")
print("~"*30)
print("Input: {0}, {1}".format(names, "Josh"))
print("Result: {0}".format(w5.occurencesWhileList(names[:], "Josh"))) # this passes a copy of the list, so we don't modify the original
print()

print("Input: {0}, {1}".format(names, "Nick"))
print("Result: {0}".format(w5.occurencesWhileList(names[:], "Nick"))) # this passes a copy of the list, so we don't modify the original
print()

print("Input: {0}, {1}".format(grades, "Josh"))
print("Result: {0}".format(w5.occurencesWhileList(grades[:], "Josh"))) # this passes a copy of the list, so we don't modify the original
print()

print("Input: {0}, {1}".format(grades, "A"))
print("Result: {0}".format(w5.occurencesWhileList(grades[:], "A"))) # this passes a copy of the list, so we don't modify the original
print()
print()

print("Testing function operationList")
print("~"*30)
print("Input: {0}, {1}".format(ex3, "m"))
print("Result: {0}".format(w5.operationList(ex3, "m")))
print()
print("Input: {0}, {1}".format(ex3, "s"))
print("Result: {0}".format(w5.operationList(ex3, "s")))
print()
print("Input: {0}, {1}".format(ex3, "a"))
print("Result: {0}".format(w5.operationList(ex3, "a")))
print()

print("Testing function evenCount2")
print("~"*30)
print("Input: {0}".format(dictionary1))
print(w5.evenCount2(dictionary1))