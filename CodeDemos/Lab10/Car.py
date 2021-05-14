'''
HELP
## Lab Assignments
For the lab assignment, they will update the code they have already been given in the **Code Demo**. 
They don't have to create a new file; they can just add to the one they already made. 

1. Add an instance function, `getName(self)`. To return the make and model of your car as a string.
2. add more instance variables: `blueToothOn`, default to `False`; `mileage`, default to 0.
3. Add an instance function to turn on/off blue tooth: `setBlueToothOn(boolean)`
4. Add an instance function: `accelerate(self, speed)`. to increase speed; 
5. Add an instance function: `brake(self)`. To decrease the speed to 0.
6. Add an instance function: `runFor(self, time)`. To increase the mileage based on time run and speed.
7. Add an instance function: `isStopped(self)`. To tell if a car is stopped.
8. Show two different ways to get the mileage value of a car, one with function, one without.
9. Challenging task: learn about generator class: 
last lab we had a generator function (the random function), can you convert it to a generator class

'''

class Car:

    recall = False  #Static Variable

    def __init__(self,make,model,year): #Constructor
        self.make = make
        self.model = model
        self.year = year
        

    @staticmethod

    def setRecall(b):   #Static Function
        Car.recall = b

    def showCar(self):
        print("Do you like my car ~")
        print(self.make + " " + self.model + " " + str(self.year))

    def startCar(self):
        self.speed = 0

    def __str__(self):
        myStr = self.make + " " + self.model + " " + str(self.year)
        return myStr

    def getName(self): 
        return str(make,model)

    
    milege = 0
    def setBlueToothOn(boolean):
        blueToothOn = False
        return blueToothOn

    def accelerate(self,speed):
        print(self.speed)
    
    def brake(self):
        print(self.speed)
        
    def runFor(self,time):
        print("I dont know")
    
    def isStopped(self):




# myCar = Car()      # This will create an instance of 'Car', which calls the constructor    
# myCar = Car("Honda", "Accord", 1998) # This will create an instance of 'Car', which calls the constructor
# myCar.showCar() # Calling an instance function on an instance of 'Car' class
# secondCar = Car("Honda", "Accord", 1998) 
# print(myCar) # Print a representation of the instance of 'Car' # Prints memory location
# print(secondCar) # Print a representation of the instance of 'Car' # Prints memory location
# print(myCar == secondCar)   # Checking if the classes are the exact same # Output: False
# # Two different memory locations will return false for above line

# print(myCar.recall)     #False
# print(secondCar.recall) #False
# print(id(myCar.recall) == id(secondCar.recall)) #True

# #myCar.recall = True #Outputs below was when this statement was true
# print(myCar.recall)  #True
# print(secondCar.recall) #False

# Car.recall = False  # Outputs below was when this was set to True
# print(myCar.recall) #True
# print(secondCar.recall) #True

# Car.setRecall(True)
# print(myCar.recall)