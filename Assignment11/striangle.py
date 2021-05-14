import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,102,0)
PURPLE = (102,0,102)
ORANGE = (255,128,0)
PINK = (255,51,153)

WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width

'''
Sample Code
def s(loc,width):
    if width > 1:
        Draw a tringle at loc using width
        s(top,width/2)
        s(L, width/2)
        s(R, width/2)
    else:
        return

L,R are 1/2 distance on the original sides
'''

def triangle(loc,width):
    #loc[0] = x and loc[1] = y
    # z = math.sqrt(width**2 - (width/2)**2)
    top = (loc[0] + width/2, loc[1])
    left = (loc[0],loc[1] + (width/2 * 3 **(1/2)))
    right = (loc[0]+width, loc[1]+(width/2 * 3**(1/2))) #We are adding loc[1] + z becasue we have a set starting point and we want it to draw based on that.  
    Location = [top,left,right] 
    return Location

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    colors = [BLUE,RED,GREEN,PURPLE,ORANGE,PINK]
    pygame.draw.polygon(DISPLAYSURF, rn.choice(colors), triangle(loc,w),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    if width > 1:
        draw_triangle(loc,width)

        top = (loc[0] + width/4, loc[1])
        left = (loc[0],loc[1] + ((width/2 * 3 **(1/2)/2)))
        right = (loc[0]+width/2, loc[1]+((width/2 * 3**(1/2)/2)))
        
        s(top, width/2)
        s(left, width/2)
        s(right, width/2)
    else:
        return
    
s((0,0),440)

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()