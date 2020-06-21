import pygame
import math

class Player:
    def __init__(self):
        self.lifes = 3
        self.initiated = False
        self.velocity = [0,0]
        self.reached_end = False

    def load_texture(self):
        self.texture = pygame.image.load("Assets/Mariusz.png").convert_alpha()
        self.texture.set_alpha(128)

    def check_for_collisions_right(self,x,y,map):
        right1 = map[math.floor(-y/32)][math.floor((-x+31)/32)]
        right2 = map[math.floor((-y+31)/32)][math.floor((-x+31)/32)]
        if right1 == '#' or right2 == '#':
            return True
        if right1 == '^' or right2 == '^':
            self.reached_end = True
            return True
        return False

    def check_for_collisions_left(self, x, y, map):
        left1 = map[math.floor(-y / 32)][math.floor(-x / 32)]
        left2 = map[math.floor((-y + 31) / 32)][math.floor(-x / 32)]
        if left1 == '#' or left2 == '#':
            return True
        if left1 == '#' or left2 == '^':
            self.reached_end = True
            return True
        return False

    def is_falling(self,x,y,map):
        return map[math.floor(-y/32)+1][math.floor((-x)/32)] != '#' and map[math.floor(-y/32)+1][math.floor((-x+31)/32)] != '#'

    def draw(self,surface,x,y):
        if not self.initiated:
            self.initiated = True
            self.load_texture()
        pygame.draw.rect(surface,(0,0,0),(x,y,32,32))
        surface.blit(self.texture,(x-8,y-16))
        return surface



