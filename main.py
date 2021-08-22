# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:31:40 2021

@author: ajher
"""

import pygame
from marbles.constants import WIDTH, HEIGHT, SPACE_SIZE
from marbles.game import Game

FPS = 60    

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Marble Solitaire')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SPACE_SIZE
    col = x // SPACE_SIZE
    return row, col


def main():
    
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
       
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
               
            game.update()
                
    pygame.quit()


main()