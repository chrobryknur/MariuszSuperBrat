import pygame
import math

BLOCK_SIZE = 32

class Player:
    def __init__(self):
        self.lifes = 3
        self.velocity = [0,0]
        self.reached_end = False
        self.current_texture = "right"
        self.died = False
        self.texture_left = pygame.image.load("Assets/Mariusz_left.png").convert_alpha()
        self.texture_right = pygame.image.load("Assets/Mariusz_right.png").convert_alpha()

    def check_for_collisions_right(self, pos, map):
        right1 = map[math.floor(-pos[1]/BLOCK_SIZE)][math.floor((-pos[0]+BLOCK_SIZE-1)/BLOCK_SIZE)]
        right2 = map[math.floor((-pos[1]+BLOCK_SIZE-1)/BLOCK_SIZE)][math.floor((-pos[0]+BLOCK_SIZE-1)/BLOCK_SIZE)]
        if right1 == '#' or right2 == '#':
            return True
        if right1 == '^' or right2 == '^':
            self.reached_end = True
            return True
        return False

    def check_for_collisions_left(self, pos, map):
        left1 = map[math.floor(-pos[1]/BLOCK_SIZE)][math.floor(-pos[0]/BLOCK_SIZE)]
        left2 = map[math.floor((-pos[1]+BLOCK_SIZE-1)/BLOCK_SIZE)][math.floor(-pos[0]/BLOCK_SIZE)]
        if left1 == '#' or left2 == '#':
            return True
        if left1 == '#' or left2 == '^':
            self.reached_end = True
            return True
        return False

    def is_falling(self, pos, map):
        if map[math.floor(-pos[1]/BLOCK_SIZE)+1][math.floor((-pos[0]/BLOCK_SIZE))] == '&' or map[math.floor(-pos[1]/BLOCK_SIZE)+1][math.floor((-pos[0]+BLOCK_SIZE-1)/BLOCK_SIZE)] == '&':
            self.died = True
            return True
        return map[math.floor(-pos[1]/BLOCK_SIZE)+1][math.floor((-pos[0])/BLOCK_SIZE)] != '#' and map[math.floor(-pos[1]/BLOCK_SIZE)+1][math.floor((-pos[0]+BLOCK_SIZE-1)/BLOCK_SIZE)] != '#'

    def jump(self,pos,map):
        y = 0
        for i in range (1,4):
            left = map[math.floor(-pos[1]/BLOCK_SIZE)-i][math.floor(-pos[0]/BLOCK_SIZE)]
            right = map[math.floor(-pos[1]/BLOCK_SIZE)-i][math.floor((-pos[0]+BLOCK_SIZE-1)/BLOCK_SIZE)]
            if not left == '#' and not right == '#':
                y += BLOCK_SIZE
            else:
                return y
        return y

    def draw(self,surface,x,y):
        pygame.draw.rect(surface,(0,0,0),(x,y,BLOCK_SIZE,BLOCK_SIZE))
        if self.current_texture == "right":
            surface.blit(self.texture_right,(x-8,y-16))
        else:
            surface.blit(self.texture_left,(x-8,y-16))
        return surface



