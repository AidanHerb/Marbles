# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:18:03 2021

@author: ajher
"""
import pygame
from .constants import BLACK, WHITE, RED, ROWS, COLS, SPACE_SIZE, GREEN
from .pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        
    def draw_board(self, win):
        win.fill(BLACK)
        for row in range(7):
            for col in range(7):
                if((row > 1) and (row < 5)):
                    pygame.draw.rect(win, WHITE, (row*SPACE_SIZE, col*SPACE_SIZE, 
                                                  SPACE_SIZE, SPACE_SIZE), border_radius = 30)
                if((col > 1) and (col < 5)):
                    pygame.draw.rect(win, WHITE, (row*SPACE_SIZE, col*SPACE_SIZE, 
                                                  SPACE_SIZE, SPACE_SIZE), border_radius = 30)
    def move(self, piece, row, col):
        #swaps place of piece with the air at the location we want to move it to
        #this removes the need for a temp variable
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if ((col > 1) and (col < 5)):
                    self.board[row].append(Piece(row, col, GREEN))
                elif ((row > 1) and (row <5)):
                    self.board[row].append(Piece(row, col, GREEN))
                else:
                    self.board[row].append(0)
                    
                    
                    
    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                    
                    
                
                
                    
                            
        
