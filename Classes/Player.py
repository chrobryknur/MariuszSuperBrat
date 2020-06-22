import pygame
import math

BLOCK_SIZE = 32


class Player:
    def __init__(self):
        self.lifes = 2
        self.velocity = [0, 0]
        self.reached_end = False
        self.current_texture = "right"
        self.died = False
        self.texture_left = pygame.image.load("Assets/Mariusz_left.png").convert_alpha()
        self.texture_right = pygame.image.load("Assets/Mariusz_right.png").convert_alpha()
        self.jumping = 0

    def check_for_collisions_right(self, pos, map):
        right1 = map[math.floor(-pos[1] / BLOCK_SIZE)][math.floor((-pos[0] + BLOCK_SIZE - 1) / BLOCK_SIZE)]
        right2 = map[math.floor((-pos[1] + BLOCK_SIZE - 1) / BLOCK_SIZE)][
            math.floor((-pos[0] + BLOCK_SIZE - 1) / BLOCK_SIZE)]
        if right1 == '#' or right2 == '#':
            return True
        if right1 == '^' or right2 == '^':
            self.reached_end = True
            return True
        return False

    def check_for_collisions_left(self, pos, map):
        left1 = map[math.floor(-pos[1] / BLOCK_SIZE)][math.floor(-pos[0] / BLOCK_SIZE)]
        left2 = map[math.floor((-pos[1] + BLOCK_SIZE - 1) / BLOCK_SIZE)][math.floor(-pos[0] / BLOCK_SIZE)]
        if left1 == '#' or left2 == '#':
            return True
        if left1 == '#' or left2 == '^':
            self.reached_end = True
            return True
        return False

    def is_falling(self, pos, map):
        if map[math.floor(-pos[1] / BLOCK_SIZE) + 1][math.floor((-pos[0] / BLOCK_SIZE))] == '&' or \
                map[math.floor(-pos[1] / BLOCK_SIZE) + 1][math.floor((-pos[0] + BLOCK_SIZE - 1) / BLOCK_SIZE)] == '&':
            self.died = True
            return True
        return map[math.floor(-pos[1] / BLOCK_SIZE) + 1][math.floor((-pos[0]) / BLOCK_SIZE)] != '#' and \
               map[math.floor(-pos[1] / BLOCK_SIZE) + 1][math.floor((-pos[0] + BLOCK_SIZE - 1) / BLOCK_SIZE)] != '#'

    def jump(self, pos, map):
        y = 0
        left  = map[math.floor((-pos[1] - BLOCK_SIZE/4) / BLOCK_SIZE) ][math.floor(-pos[0] / BLOCK_SIZE)]
        right = map[math.floor((-pos[1] - BLOCK_SIZE/4) / BLOCK_SIZE) ][math.floor((-pos[0] + BLOCK_SIZE - 1) / BLOCK_SIZE)]
        if not left == '#' and not right == '#':
            y += BLOCK_SIZE/4
        return y

    def collision_with_creature(self, pos, creature_rect):
        if pygame.Rect(-pos[0], -pos[1], BLOCK_SIZE, BLOCK_SIZE).colliderect(creature_rect):
            self.died = True

    def draw(self, surface, x, y):
        s = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(s, (0, 0, 0), (x, y, BLOCK_SIZE, BLOCK_SIZE), 1)
        s.set_alpha(0)
        surface.blit(s,(x,y))
        if self.current_texture == "right":
            surface.blit(self.texture_right, (x, y))
        else:
            surface.blit(self.texture_left, (x, y))
        return surface
