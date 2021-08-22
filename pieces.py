# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:48:36 2021

@author: ajher
"""
import pygame
from .constants import SPACE_SIZE, GRAY


class Piece:
    
    Padding = 10
    Outline = 2   
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SPACE_SIZE * self.col + SPACE_SIZE // 2
        self.y = SPACE_SIZE * self.row + SPACE_SIZE // 2
        
    def draw(self, win):
        
        radius = SPACE_SIZE // 2 - self.Padding
        outline_rad = radius + self.Outline
        
        pygame.draw.circle(win, GRAY, (self.x, self.y), outline_rad)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
        
    def __repr__(self):
        return str(self.color)