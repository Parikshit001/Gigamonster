import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, gropus):
        super().__init__(gropus)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)