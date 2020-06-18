import pygame, sys
import pygame.locals
import Classes.Menu as M

import pygame

SKY = "."
BRICK = "#"
PIPE = "/"


class Game:
    def __init__(self,wsize):
        self.initiated = False
        self.tile_x, self.tile_y = 32, 32
        self.level = self.load_level()
        self.surface = pygame.display.set_mode(wsize)
        self.x = 0
        self.y = 0
        self.dx = 5
        self.dy = 5
        self.gravity = 10
        self.jump = 10
        self.pressed_w = False
        self.pressed_d = False
        self.pressed_a = False
        self.pressed_s = False
        self.clock = pygame.time.Clock()

    def next_state(self):
        return self.next_s

    def load_tile(self, type, x, y):
        image = 0
        if type == SKY:
            image = 0
        elif type == BRICK:
            image = pygame.image.load("Assets/brick.png").convert()
        image_width, image_height = 32,32
        rect = (x * image_width, y * image_height, image_width, image_height)
        return [image, rect]

    def load_level(self):
        file = open("Levels/Level1", "r")
        level = []
        for i in range(0, 19):
            l = []
            level.append(l)
            line = file.readline()
            for j in range(0, 79):
                l.append(self.load_tile(line[j], j, i))
        return level

    def init(self):
        self.background = pygame.image.load("Assets/main_menu_bg.png")

    def draw(self, screen):
        if not self.initiated:
            self.init()
            self.initiated = True
        self.handle = True
        self.surface.blit(self.background, (0, 0))
        while self.handle:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.handle = False
                    self.next_s = -1
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.pressed_w = True
                    if event.key == pygame.K_s:
                        self.pressed_s = True
                    if event.key == pygame.K_a:
                        self.pressed_a = True
                    if event.key == pygame.K_d:
                        self.pressed_d = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.pressed_w = False
                    if event.key == pygame.K_s:
                        self.pressed_s = False
                    if event.key == pygame.K_a:
                        self.pressed_a = False
                    if event.key == pygame.K_d:
                        self.pressed_d = False

            if self.pressed_w:
                self.y += self.dy
            if self.pressed_s:
                self.y -= self.dy
            if self.pressed_a:
                self.x += self.dx
            if self.pressed_d:
                self.x -= self.dx


            for x, row in enumerate(self.level):
                for y, tile in enumerate(row):
                    pygame.draw.rect(self.surface,(0,0,0,0),tile[1])
                    if tile[0]:
                        self.surface.blit(tile[0],(tile[1][0] + self.x,tile[1][1]+self.y))
            screen.blit(self.surface,(0,0))
            pygame.display.update()
            self.clock.tick(50)



class GameOver:
    def __init__(self):
        print("elo")


class WindowConfiguration:
    def __init__(self, w, h):
        self.windowSize = (w, h)

    def size(self):
        return self.windowSize


class Main:
    def __init__(self):
        self.WindowConfig = WindowConfiguration(800, 600)
        self.GameStates = (M.Menu(self.WindowConfig.size()),
                           Game(self.WindowConfig.size()),
                           GameOver())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return True

    def run(self):
        self.currentGameState = self.GameStates[0]
        pygame.init()
        window = pygame.display.set_mode(self.WindowConfig.windowSize)
        while not self.handle_events():
            self.currentGameState.draw(window)
            next_state = self.currentGameState.next_state()
            if next_state == 1:
                self.currentGameState = self.GameStates[1]
            if next_state == -1:
                break
