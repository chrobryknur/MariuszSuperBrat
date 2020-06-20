import pygame
import Classes.Map as Map
import Classes.Info as Info
import Classes.Player as Player

class Game:
    def __init__(self,wsize):
        self.initiated = False
        self.surface = pygame.display.set_mode(wsize)
        self.map = Map.Map()
        self.info = Info.Info()
        self.player = Player.Player()
        self.clock = pygame.time.Clock()

    def next_state(self):
        return self.next_s

    def init(self):
        self.background = pygame.image.load("Assets/main_menu_bg.png").convert()
        self.level = self.map.load_level()
        self.handle = True
        self.next_s = 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.handle = False
                self.next_s = -1
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.info.player_y -= 32
                if event.key == pygame.K_s:
                    self.info.player_y += 32
                if event.key == pygame.K_a:
                    self.info.pressed_a = True
                if event.key == pygame.K_d:
                    self.info.pressed_d = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.info.pressed_w = False
                if event.key == pygame.K_s:
                    self.info.pressed_s = False
                if event.key == pygame.K_a:
                    self.info.pressed_a = False
                if event.key == pygame.K_d:
                    self.info.pressed_d = False

        if self.info.pressed_a:
            if not self.player.check_for_collisions(self.info.x - 368,self.info.y - self.info.player_y,self.map.level_repr):
                self.info.x += self.info.dx
        if self.info.pressed_d:
            if not self.player.check_for_collisions(self.info.x - 400,self.info.y - self.info.player_y,self.map.level_repr):
                self.info.x -= self.info.dx

    def draw(self, screen):
        if not self.initiated:
            self.init()
            self.initiated = True
        while self.handle:
            self.handle_events()
            self.surface.blit(self.background, (0, 0))
            screen.blit(self.map.draw_map(self.level, self.surface, self.info.x, self.info.y), (0, 0))
            screen.blit(self.player.draw(self.surface,self.info.player_x,self.info.player_y), (0,0))
            pygame.display.update()
            self.clock.tick(50)
