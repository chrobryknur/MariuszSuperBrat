import math
import pygame

class Info:
    def __init__(self, lifes,score):
        self.x = 0
        self.y = 0
        self.player_x = 368
        self.player_y = 352
        self.player_x_default = 368
        self.player_y_default = 352
        self.dx = 4
        self.dy = 4
        self.gravity = 4
        self.jump = 96
        self.pressed_w = False
        self.pressed_d = False
        self.pressed_a = False
        self.game_over = False
        self.score = score
        self.lifes_left = lifes

    def update_score(self):
        self.score = max(self.score,-math.floor(self.x/self.dx))

    def text_sufrace(self,text, font,color):
        white = (255, 255, 255)
        surf = pygame.Surface(font.size(text))
        surf.fill(white)
        textSurface = font.render(text, True, color, surf)
        return textSurface

    def player_pos_on_map(self):
        return [self.x - self.player_x, self.y - self.player_y]

    def draw(self,surface):
        self.scoreText = pygame.font.Font("Assets/pcsenior.ttf", 15)
        self.lifesText = self.scoreText
        surface.blit(self.text_sufrace("Score:" + str(self.score), self.scoreText, (0, 0, 0)), (600, 20))
        surface.blit(self.text_sufrace("Lifes left:", self.lifesText, (0, 0, 0)), (600, 50))
        surface.blit(self.text_sufrace(str(self.lifes_left), self.lifesText, (255, 0, 0)), (770, 50))
        return surface