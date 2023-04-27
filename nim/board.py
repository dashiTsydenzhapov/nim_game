from re import S
import pygame
from .stone import STONES
from .constants import WHITE
class Game:
    def __init__(self,win):
        self._init()
        self.win = win
    
    def _init(self):
        self.board = STONES
        self.selected_stones = []
    
    def get_selected_stones(self):
        return self.selected_stones
    
    def remove(self):
        for point in self.selected_stones:
            self.board[point.group][point.id].visiable = False
            self.board[point.group][point.id].isSelected = False
        self.selected_stones.clear()
    
    def move_enemy(self,move):
        l=[]
        for i in range(len(self.board[int(move[0])-1])):
            if self.board[int(move[0])-1][i].visiable==True:
                l.append(i)
        for i in range(int(move[1])):
            self.board[int(move[0])-1][l[i]].visiable = False
        

    def add_selected(self,stone):
        if stone==None:
            return
        if stone.isSelected==True:
            self.board[stone.group][stone.id].isSelected = False
            self.selected_stones.remove(stone)
            return
        if not self.selected_stones or stone.group!=self.selected_stones[-1].group:
            self.selected_stones.clear()
            for group in self.board:
                for point in group:
                    point.isSelected=False
            self.selected_stones.append(stone)
            self.board[stone.group][stone.id].isSelected=True    
        else:
            self.selected_stones.append(stone)
            self.board[stone.group][stone.id].isSelected = True
            
    def isOver(self):
        isover = 0
        for group in self.board:
            for point in group:
                if point.visiable==True:
                    isover+=1
        if isover==0:
            return True
    
    def getState(self):
        s=''
        for group in self.board:
            c = 0
            for point in group:
                if point.visiable==True:
                    c+=1
            s=s+str(c)
        return s
    
    def draw(self, win):
        for group in self.board:
            for point in group:
                point.draw(win)
    
    def reset(self):
        for group in self.board:
            for point in group:
                self.board[point.group][point.id].visiable = True
                self.board[point.group][point.id].isSelected = False
        self.selected_stones = []


