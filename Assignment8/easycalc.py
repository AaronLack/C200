import math

# Input function fn, start is a, end is b,
# n is an even number of intervals
# Retun approximate area under the curve

def simpson(fn,a,b,n):
    delta_x = (b-a)/n
    interval = lambda i: a + i*delta_x
    x0 = a
    xn = b
    sum = fn(x0) + fn(xn)
    for i in range(1,n):
        if i % 2 != 0:
            sum += 4*fn(interval(i))
        elif i % 2 == 0:
            sum += 2*fn(interval(i))
    intergral = ((b-a)/(3*n)) * sum
    return intergral

# convert string to either number or expression
def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)

if __name__ == "__main__":
    with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment8/intergralfile.txt", "r") as xfile: 
        xlines = [d.split(",") for d in xfile.read().split("\n")]

    for i in xlines:
        body = i[0]
        fn = eval("lambda x : " + body)
        a = convert(i[1])
        b = convert(i[2])
        n = convert(i[3])
        answer = convert(i[4])
        integration = simpson(fn,a,b,n)
        error = abs((answer - integration)/answer)
        print("f(x) = {0} over [{1},{2}] is {3:.3f}".format(body,a,b,integration))
        print("Actual answer is {0:.3f}".format(answer))
        print("Error is {0:.3f}".format(error))