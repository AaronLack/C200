import os

path_of_execution = os.getcwd()

print("~" * 30)
print("Current location where python program is running: ")
print("\t" + path_of_execution) #"\t": represents an indent

print("\n")
print("\t\t READING \t\t")

someFile = open("CodeDemos/Lab5/blank.txt", "r")
# someFile = open("CodeDemos/Lab5/blank.txt")
# "r" is a default value for the 2nd parameter

contents = someFile.read()
print("Start of file")
print("-"*30)
print(contents, end="") #To prevent an automatic new liine at the end
print("*EOF*") #EOF is end of file
someFile.close()

print("~"*30)
print("\n")
print("\t\t READING \t\t")
someFile = open("CodeDemos/Lab5/blank.txt", "r")
contents = someFile.readlines()
print("Start of file")
print("-" * 30)
print(contents)
print("*EOF*")
someFile.close()

print("\n")
print("\t\t Writing \t\t")
stuff = ["a","b","c","d","e","f"]

fileToWrite = open("CodeDemos/Lab5/wrong.txt", "w")
for s in stuff:
    fileToWrite.write(s + "\n") # we need to tel it to have a new line
fileToWrite.close()

fileToWrite = open("CodeDemos/Lab5/wrong.txt", "a")
for s in stuff:
    fileToWrite.write("more\n")
fileToWrite.close

print("~"*30)
print("\t\t STRINGS \t\t")
v1 = "l o s t"
v2 = " carrot"
v3 = "the quick brwon fox jumped over quickly over the lazy turtle."

template = "|{0}| |{1}|"

print(template.format(v1, v1.strip()))
print(template.format(v2, v2.strip()))
print(template.format(v3, v3.strip("thaeiou.")))

print("~"*30)
print("SPLIT")
t1 = "1,2,3"
t2 = "1cat2cat3cat"
t3 = "a123,b123,3"
t4 = "1 2 3"

print(template.format(t1, t1.split(",")))
print(template.format(t2, t2.split("cat")))
print(template.format(t3, t3.split("123")))
print(template.format(t4, t4.split()))
