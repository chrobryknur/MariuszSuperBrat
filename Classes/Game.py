import pygame
import Classes.Map as Map
import Classes.Info as Info
import Classes.Player as Player

class Game:
    def __init__(self,wsize):
        self.initiated = False
        self.surface = pygame.display.set_mode(wsize)
        self.map = Map.Map()
        self.player = Player.Player()
        self.info = Info.Info(self.player.lifes,0)
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
                    if not self.player.is_falling(self.info.player_pos_on_map(), self.map.level_repr):
                        self.info.player_y -= self.player.jump(self.info.player_pos_on_map(), self.map.level_repr)
                if event.key == pygame.K_a:
                    self.info.pressed_a = True
                if event.key == pygame.K_d:
                    self.info.pressed_d = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.info.pressed_w = False
                if event.key == pygame.K_a:
                    self.info.pressed_a = False
                if event.key == pygame.K_d:
                    self.info.pressed_d = False

        if self.player.is_falling(self.info.player_pos_on_map(), self.map.level_repr):
            self.info.player_y += self.info.gravity
            if self.info.player_y >= 568:
                self.info.game_over = True

        if self.info.pressed_a:
            pos = self.info.player_pos_on_map()
            pos[0] += self.info.dx
            if not self.player.check_for_collisions_left(pos, self.map.level_repr):
                if not (self.info.x + self.info.dx >= 0):
                    self.info.x += self.info.dx
                else:
                    self.info.player_x -= self.info.dx
        if self.info.pressed_d:
            pos = self.info.player_pos_on_map()
            pos[0] -= self.info.dx
            if not self.player.check_for_collisions_right(pos, self.map.level_repr):
                if self.info.player_x_default > self.info.player_x:
                    self.info.player_x += self.info.dx
                else:
                    self.info.x -= self.info.dx

    def draw(self, screen):
        if not self.initiated:
            self.init()
            self.initiated = True
        while self.handle and not self.info.game_over and not self.player.reached_end:
            self.handle_events()
            self.info.update_score()
            screen.blit(self.background, (0, 0))
            screen.blit(self.map.draw_map(self.level, self.surface, self.info.x, self.info.y), (0, 0))
            screen.blit(self.player.draw(self.surface, self.info.player_x, self.info.player_y), (0, 0))
            screen.blit(self.info.draw(self.surface),(0,0))
            pygame.display.update()
            self.clock.tick(50)

        if self.info.game_over:
            if self.info.lifes_left == 0:
                self.next_s = -1
            else:
                self.info = Info.Info(self.info.lifes_left-1, self.info.score)

        if self.player.reached_end:
            self.player.reached_end = False
            self.info = Info.Info(self.player.lifes,0)
