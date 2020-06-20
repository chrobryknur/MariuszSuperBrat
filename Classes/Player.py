import pygame
import math

class Player:
    def __init__(self):
        self.lifes = 3
        self.initiated = False
    def load_texture(self):
        self.texture = pygame.image.load("Assets/Mariusz.png").convert_alpha()
        self.texture.set_alpha(128)

    def check_for_collisions(self,x,y,map):
        return(map[math.floor(-y/32)][math.floor(-x/32)]) == '#'

    def draw(self,surface,x,y):
        if not self.initiated:
            self.initiated = True
            self.load_texture()
        pygame.draw.rect(surface,(0,0,0),(x,y,32,32))
        surface.blit(self.texture,(x,y))
        return surface


