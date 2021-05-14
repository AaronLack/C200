import math

class MyComplexNumber:
    def __init__(self, rpart, ipart):
        self.rpart = rpart
        self.ipart = ipart
        self.cn = [self.rpart, self.ipart]
    
    def get_real(self):
        return self.rpart
    
    def get_imag(self):
        return self.ipart
    
    def __str__(self):
        return str(self.cn)

    #adds two complex numbers
    def add(self, ix):
        real_part = self.get_real() + ix.get_real()
        imag_part = self.get_imag() + ix.get_imag()
        iy = MyComplexNumber(real_part, imag_part)
        return iy
    
    #extends the '+' operator to add two complex numbers
    #what's the different between __add__(self,ix) and add(self,ix)?
    
    # __add__(self,ix) calls the object self + ix; it is more natural to do
    # all yo have do if you have a1 = MyCN(3,-1) and b1 = MyCN(0,6)
    # Is to set a variable d1 = a1+b1
    #  Still adds al and b1, but not as natural, you would have to do
    # c1 = a1.add(b1)
    #Both work and both add complex numbers a1 and b1.  

    def __add__(self,ix):
        real_part = self.get_real() + ix.get_real()
        imag_part = self.get_imag() + ix.get_imag()
        iy = MyComplexNumber(real_part, imag_part)
        return iy
        
    #extends the '-' operator to subtract two complex numbers
    #parameters: MyComplexNumber self, MyComplexNumber ix to subtract from the MyComplexNumber self
    #return: a new MyComplexNumber containing the result
    def __sub__(self,ix):
        real_part = self.get_real() - ix.get_real()
        imag_part = self.get_imag() - ix.get_imag()
        iy = MyComplexNumber(real_part, imag_part)
        return iy

    #extends the '/' operator to divide two complex numbers
    #parameters: MyComplexNumber self, MyComplexNumber ix to divide into the MyComplexNumber self
    #return: a new MyComplexNumber containing the result

    # a = self.get_real()
    # b = self.get_imag()
    # c = other.get_real()
    # d = other.get_imag()
    def __truediv__(self,other):
        real_part = ((self.get_real()*other.get_real()) + (self.get_imag()*other.get_imag()) ) / ((other.get_real()**2) + (other.get_imag()**2))
        imag_part = ((self.get_imag()*other.get_real()) - (self.get_real()*other.get_imag())) / ((other.get_real()**2) + (other.get_imag()**2))
        iy = MyComplexNumber(real_part, imag_part)
        return iy

    def __mul__(self,other):
        real_part = self.get_real()*other.get_real() - self.get_imag()*other.get_imag()
        imag_part = self.get_real()*other.get_imag() + self.get_imag()*other.get_real()
        iy = MyComplexNumber(real_part, imag_part)
        return iy

    #calculates the modulus of the self MyComplexNumber
    #parameters: MyComplexNumber self
    #return: the value of the modulus
    def modulus(self):
        return math.sqrt(self.get_real()**2 + self.get_imag()**2)
    

    #converts the self MyComplexNumber to polar representation
    #parameters: MyComplexNumber self
    #return: a tuple (rho, theta) as defined in the text, but where theta is in degrees not radians
    def polar(self):
        rho = math.sqrt(self.get_real()**2 + self.get_imag()**2)
        theta = math.atan(self.get_imag()/self.get_real()) * (180/math.pi) #This converts it
        return (rho,theta)
        


#TEST CASES
if __name__ == "__main__":
    x1 = MyComplexNumber(3,-1) #3-i
    x2 = MyComplexNumber(1,4)  #1+4i
    x3 = MyComplexNumber(-3,1) #-3+i
    x4 = MyComplexNumber(2,-4) #2-4i
    x5 = MyComplexNumber(-2,1)
    x6 = MyComplexNumber(1,2)
    x7 = MyComplexNumber(0,3) 
    x8 = MyComplexNumber(-1,-1)
    x9 = MyComplexNumber(1,-1)
    x10 = MyComplexNumber(4,-3)
    x11 = MyComplexNumber(3,2)
    x12 = MyComplexNumber(1,1)


    print(x1 + x2)
    print(x1 * x2)
    print(x3 + x4)
    print(x3 * x4)
    print()
    print(x5/x6)
    print(x7/x8)
    print(x9.modulus())
    print(x10.modulus())
    print()
    print(x12.polar())

    # I think I got subtraction right, and I'm not sure how to do polar or mod or div