# x = [1,4,5,2,1,3]
# y = ["a","dog","kitty","tree","z","c"]

# for i,j in zip(x,y):
#     print(i,j)

# def insertion_sort(a,size):
#     i = 1
#     while i < size:
#         j = i
#         while j > 0:
#             if a[j] < a[j-i]:
#                 a[j],a[j-1] = a[j-1], a[j]
#             j -= 1
#         i += 1

# def selection_sort(a,size):

#     for i in range(size):
#         smallest_id = i
#         for j in range(i+1,size):
#             if a[smallest_id] > a[j]:
#                 smallest_id = j
#         a[smallest_id],a[i] = a[i], a[smallest_id]

# def bubble_sort(a,size):

#     for i in range(size):
#         for j in range(size-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j] 

# def bubble_sort(a,size):

#     for i in range(size):
#         for j in range(size-1-i):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]

# def half_adder(a,b):
#     def exor(a,b):
#         return int((not a and b) or (a and not b))
#     sum = exor(a,b)
#     carry = a and b
#     return (sum,carry)

# input = [0,1]
# for a in input:
#     for b in input:
#         x,y = half_adder(a,b)
#         print("{0} {1} | {2} {3}".format(a,b,x,y))

# def d_to_b(n,b):
#     y = 0
#     p = 0
#     while n!=0:
#         y = (n % b)*(10**p) + y
#         p += 1
#         n = n//b
#     return y

# for i in range(0,17):
#     base2 = d_to_b(i,2)
#     base3 = d_to_b(i,3)
#     print("{:<3} {:<4} {:<3}".format(i,base2,base3))

# def make(xlst):
#     x = []
#     for i in xlst:
#         x = x + [i[0]*i[1]]
#     return x

# y = make([['a',2],[2,1],['z',3]])
# print(y)

def make1(xlst):
    xtmp,tmp = xlst[:],[]
    while xtmp:
        a,b = xtmp[0][0],xtmp[0][1]
        tmp.append([a]*b)
        xtmp = xtmp[1:]
    return tmp

y = make1([['a',2],[2,1],['z',3]])
print(y)
