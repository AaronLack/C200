import pygame
import sys
import random as rn

pygame.init()
 
#RGB Colors; look online for what they are
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)
DARK_GREEN = (0,100,0)

class Rectangle:
    """
    Refer to the instructions if you need to modify this.
    """

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
  
       
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("C200 CHANGE")


r = Rectangle(RED, [0, 0, 20, 20])


if __name__ == "__main__":
    while True:
        
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
        screen.fill(WHITE)
    
        r.my_draw(screen)
        
        if r.loc[0] > 280:
            r = Rectangle(DARK_GREEN, [r.loc[0], r.loc[1], 20, 20])            #Right
            xd = -rn.randint(1,3)

        if r.loc[1] > 280:  
            r = Rectangle(BLUE, [r.loc[0], r.loc[1], 20, 20])                 #Bottom
            yd = -rn.randint(1,3)
            
        if r.loc[0] < 10: 
            r = Rectangle(RED, [r.loc[0], r.loc[1], 20, 20])                    #Left
            xd = rn.randint(1,3)
            
        if r.loc[1] < 10:  
            r = Rectangle(YELLOW, [r.loc[0], r.loc[1], 20, 20])                 #Top
            yd = rn.randint(1,3)
            

        r.my_move(xd,yd)

        pygame.display.flip()

#Coordinates start at upper left corner