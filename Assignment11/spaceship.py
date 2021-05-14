import pygame
import sys

MAX_ITER = 80

#Z and C are represented by complex numbers
# def mandelbrot(c):
#     c = (2,2j) #IDK what c is or what it does
#     z = (2,2j) #IDK value of c either
#     if n == 0:
#         return 0
#     else:
#         return z**2 * mandelbrot(n-1) + c

def mandelbrot(c,max):
    iteration = 0
    z = 0
    for i in range(0, max+1):
        if abs(z) <= 2:
            z = z**2 + c
            iteration += 1
    return iteration

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BlUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mandelbrot")
screen.fill(WHITE)

#create an array of pixels
pixAr = pygame.PixelArray(screen) #Allows you to color each pixel


for a in range(-450,450):
    for b in range(-300,300):
        c = (a/450 + b/300j)      
        v = mandelbrot(c,80)
        if v > MAX_ITER:
            pixAr[a+450, b+300] = BLACK   #Make pixel black
        else:
            pixAr[a+450,b+300] = RED #Make pixel red

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() #Since there is no annimation we have to update once