lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

def magic(x):
    s = 0
    for y in x:
        z = y[0]
        s += z
    return s

if __name__ == '__main__':
    print(magic(lst))