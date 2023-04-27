import pygame
import numpy as np
from .constants import BLACK,GREY,RADIUS,OUTLINE,WHITE

class Stone:
    def __init__(self,x,y,id,group):
        self.x = x
        self.y = y
        self.id = id
        self.group = group
        self.isSelected = False
        self.visiable = True
        
    def draw(self,win):
        if not self.visiable:
            pygame.draw.circle(win,WHITE,(self.x,self.y),RADIUS)
            return
        if self.isSelected:
            pygame.draw.circle(win,GREY,(self.x,self.y),RADIUS + OUTLINE)
        pygame.draw.circle(win,BLACK,(self.x,self.y),RADIUS)

STONES=[[],[],[],[]]
STONES[0].append(Stone(100,20,0,0))

STONES[1].append(Stone(250,20,0,1))
STONES[1].append(Stone(250,120,1,1))
STONES[1].append(Stone(250,220,2,1))

STONES[2].append(Stone(400,20,0,2))
STONES[2].append(Stone(400,120,1,2))
STONES[2].append(Stone(400,220,2,2))
STONES[2].append(Stone(400,320,3,2))
STONES[2].append(Stone(400,420,4,2))

STONES[3].append(Stone(550,20,0,3))
STONES[3].append(Stone(550,120,1,3))
STONES[3].append(Stone(550,220,2,3))
STONES[3].append(Stone(550,320,3,3))
STONES[3].append(Stone(550,420,4,3))
STONES[3].append(Stone(550,520,5,3))
STONES[3].append(Stone(550,620,6,3))

def stone_from_pos(pos):
    x,y = pos
    for group in STONES:
        for point in group:
            if dist(x,y,point.x,point.y)<=RADIUS:
                return point
    return 

def dist(x1,y1,x2,y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)