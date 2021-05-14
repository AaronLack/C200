# Linearization

# n = 10
# a = [0,1]
# for i in range(2,n):
#     a.append(a[i-1] + a[i-2])
# print(a)

#Sorting
# x = [5,2,13,4]
# print(x)
# x.sort()
# print(x)

# y = ["cat", "dog", "ant", "gnat"]
# y.sort(reverse=True)
# print(y)

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z.sort
# print(z)
#Output: [[1, 'cat'], [4, 'dog'], [3, 'ant'], [2, 'gnat']]

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z.sort(key = lambda x: x[1], reverse = True)
# print(z)
# Output: [[2, 'gnat'], [4, 'dog'], [1, 'cat'], [3, 'ant']]

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z.sort(key = lambda x: (x[1],x[0]))
# print(z)
# OUtput: [[3, 'ant'], [1, 'cat'], [4, 'dog'], [2, 'gnat']]

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z = sorted(z)
# print(z)
# Output [[1, 'cat'], [2, 'gnat'], [3, 'ant'], [4, 'dog']]

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z = sorted(z, key = lambda x: x[1], reverse=True)
# print(z)
#Output: [[2, 'gnat'], [4, 'dog'], [1, 'cat'], [3, 'ant']]

# z = [[1,"cat"],[4,"dog"],[3,"ant"],[2,"gnat"]]
# z = sorted(sorted(z, key = lambda x: x[0]), key = lambda x: x[1],reverse = True)
# print(z)
#Output: [[2, 'gnat'], [4, 'dog'], [1, 'cat'], [3, 'ant']]

#Stacks

class Stack:
    def __init__(self, ):
        self.stack = []
    def pop(self):
        if not self.empty():
            top = self.stack[0]
            self.stack = self.stack[1:]
            return top
        else:
            pass
        
    def push(self,item):
        self.stack.insert(0,item)
    def empty(self):
        return self.stack==[]
    def get_stack(self):
        return self.stack

s = Stack()