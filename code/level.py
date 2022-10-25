from tokenize import group
import pygame
from settings import *
from tile import Tile
from player import Player
#from code.settings import WORLD_MAP

class Level:
    def __init__(self):
        
        #get display surface
        self.display_surface = pygame.display.get_surface()
        
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #sprtie setup
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate (WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites])
                    
        
    def run(self):
        #update and draw the game
        pass