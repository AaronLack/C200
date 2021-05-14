def magic(x):
    x= (((15+x)*3)-(9))/(3)-12
    return x


if __name__=="__main__":

    x = input("Pick any positive whole number: ")

    x = int(x)

    print("Your number was", magic(x))


if __name__=="main":
    pass 