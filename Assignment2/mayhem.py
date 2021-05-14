#All Work Here is Solely Mine!

import math

#1
def speed(d,t):
    return d/t

print("{} miles/hour".format(speed(50,2))) 

#2
def distance(s,t):
    return s*t

print("{} miles" .format(distance(25,2)))

#3
def time(s,d):
    minute_hours = 60
    return (minute_hours*d)/s

print("{} minutes".format(time(25,50)))

#4 (
def hours_to_min(numberHours):
    hours = 60 #minutes
    return hours*numberHours

print("{} minutes" .format(hours_to_min(.5)))

#5
def min_to_sec(numberMinutes):
    minutes = 60 #seconds 
    return minutes*numberMinutes

print("{} seconds". format(min_to_sec(3)))

#6
def feet_to_mile(numberFeet):
    miles =  5280 #feet
    return numberFeet/miles

print("{} miles" .format(feet_to_mile(2640)))

#7
def miles_to_kilometers(numberMiles):
    kilometers = 1.60934 #miles
    return numberMiles*kilometers

print("{} kilometers" .format(miles_to_kilometers(5)))

#8
def kilometers_to_miles(numberKilometers):
    miles = 1/1.60934 #kilometers
    return numberKilometers*miles

print("{} miles" .format(kilometers_to_miles(5)))

#9
def miles_to_feet(numberMiles):
    miles = 1/5280 #feet
    return numberMiles/miles

print("{} feet" .format(miles_to_feet(2)))

#10
def degrees_to_radians(numberDegrees):
    degrees = math.pi/180 #radians
    return numberDegrees*degrees

print("{} radians" .format(degrees_to_radians(180)))

#11 Gamma must be in radians

def degrees_to_radians(gamma):
    deg_to_rad = math.pi/180
    return deg_to_rad*gamma

print(degrees_to_radians(37))


def side_length_triangle(a,b,gamma):
    return math.sqrt(a**2 +b**2 -2*a*b*math.cos(gamma))

print("{} length of side c". format(side_length_triangle(8,11,degrees_to_radians(37))))

#12 
def celsius_to_fahrenheit(numberDegreesC):
    degrees_Celsius = (9/5)*numberDegreesC+32 #Fahrenhiet
    return degrees_Celsius

print("{} degrees Fahrenheit".format(celsius_to_fahrenheit(100)))

#13
def fahrenheit_to_celsius(numberDegreesF):
    degrees_fahrenheit = (numberDegreesF-32)*(5/9)
    return degrees_fahrenheit

print("{} degrees Celcius".format(fahrenheit_to_celsius(32)))

#14
def kelvin_to_fahrenheit(numberKelvin):
    degrees_kelvin = ((numberKelvin-273)*(9/5) + 32)
    return degrees_kelvin

print("{} degrees Fahrenheit".format(kelvin_to_fahrenheit(1000)))

#15 STUCK
def percent_change(s,d):
    if s < 0:
        return -(1+(s+d/s))
    else:
        return (((s+d)/s) -1)

print("{} percent change".format(percent_change(223.08,-.5)))

#16
def parsecs_to_kilometers(numberParsecs):
    parsecs = 3.086e13 #Kilometers
    return parsecs*numberParsecs

print("{} kilometers".format(parsecs_to_kilometers(2)))

#17
def lightyears_to_parsecs(numberLightYears):
    light_years = 1/3.26 #parsecs
    return light_years*numberLightYears

print("{} parsecs ".format(lightyears_to_parsecs(3)))


####
#Data
####

s1 = 75         #miles/hours
t1 = 4          #hours
t2 = 2020       #min
t3 = 414241     #sec
d1 = 100        #miles
d2 = 1442412    #feet

######
#Tests
#####

print(speed(d1,t1), "miles/hour")

print(speed(miles_to_kilometers(d1),t1), "kilometers/hours")

print(speed(miles_to_kilometers(d1),min_to_sec(hours_to_min(t1))),"kilometers/hour")

print(celsius_to_fahrenheit(-30), "Fahrenheit")

print(min_to_sec(hours_to_min(1)), "seconds")

print(fahrenheit_to_celsius(-22), "Celsius")

print(celsius_to_fahrenheit(20), "Fahrenheit")

print(kelvin_to_fahrenheit(293), "Fahrenheit") 

print(fahrenheit_to_celsius(kelvin_to_fahrenheit(293)), "Celsius") 

print(side_length_triangle(8,11,degrees_to_radians(37)), "units") 

print(percent_change(170.90,3.31), "percent change")

print(percent_change(170.90,-3.31), "percent change") 

print(parsecs_to_kilometers(231), "kilometers")

print(lightyears_to_parsecs(100), "parsecs")