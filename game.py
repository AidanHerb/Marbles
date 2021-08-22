# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:23:51 2021

@author: ajher
"""

import pygame
from marbles.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.valid_moves = {}
    
    def reset(self):
        self._init()
        
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row,col)
        if piece != 0:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
        

    