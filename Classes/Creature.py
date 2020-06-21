import pygame
import math


BLOCK_SIZE = 32
class Creature:

    def __init__(self, pos):
        pass

    def toggle_speed(self):
        self.speed *= -1
        if self.speed < 0:
            self.texture = self.texture_l
        else:
            self.texture = self.texture_r

    def check_for_collisions_right(self, map):
        right1 = map[math.floor(self.pos[1] / BLOCK_SIZE)][math.floor(self.pos[0] / BLOCK_SIZE) + 1]
        right2 = map[math.floor((self.pos[1] + BLOCK_SIZE - 1) / BLOCK_SIZE)][math.floor(self.pos[0] / BLOCK_SIZE) + 1]
        return right1 == '#' or right2 == '#'

    def check_for_collisions_left(self, map):
        left1 = map[math.floor(self.pos[1] / BLOCK_SIZE)][math.floor(self.pos[0] / BLOCK_SIZE)]
        left2 = map[math.floor((self.pos[1] + BLOCK_SIZE - 1) / BLOCK_SIZE)][math.floor(self.pos[0] / BLOCK_SIZE)]
        return left1 == '#' or left2 == '#'

    def creature_rect(self):
        return (self.pos[0], self.pos[1], BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, surface, x, y, map):
        if not self.check_for_collisions_right(map):
            self.pos[0] += self.speed
        else:
            self.toggle_speed()
            self.pos[0] += self.speed

        if not self.check_for_collisions_left(map):
            self.pos[0] += self.speed
        else:
            self.toggle_speed()
            self.pos[0] += self.speed
        pygame.draw.rect(surface, (0, 0, 0), (self.pos[0], self.pos[1], BLOCK_SIZE, BLOCK_SIZE))
        surface.blit(self.texture, (self.pos[0] + x, self.pos[1]))
        return surface
