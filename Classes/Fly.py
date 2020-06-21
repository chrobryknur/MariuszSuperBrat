import pygame
import Classes.Creature as Creature


BLOCK_SIZE = 32
class Fly(Creature.Creature):
    def __init__(self, pos):
        pygame.init()
        self.speed = 1
        self.pos = pos
        self.texture_l = pygame.image.load("Assets/fly_l.png")
        self.texture_r = pygame.image.load("Assets/fly_r.png")
        self.texture = self.texture_r
