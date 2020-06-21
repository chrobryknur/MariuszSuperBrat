import pygame.locals
import Classes.Menu as Menu
import Classes.Game as Game
import Classes.GameOver as GameOver

import pygame

EXIT = -1
MAIN_MENU = 0
GAME = 1
GAME_OVER = 2


class WindowConfiguration:
    def __init__(self, w, h):
        self.windowSize = (w, h)

    def size(self):
        return self.windowSize


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mariusz Super Brat')
        self.WindowConfig = WindowConfiguration(800, 600)
        self.window = pygame.display.set_mode(self.WindowConfig.windowSize)
        self.GameStates = [Menu.Menu(self.WindowConfig.size())]
        self.prev_state = -2
        self.handle = True
        self.currentGameState = self.GameStates[MAIN_MENU]

    def update_game_state(self):
        self.currentGameState.draw(self.window)
        self.next_state = self.currentGameState.next_state()
        if self.next_state != self.prev_state:
            if self.next_state == GAME:
                if len(self.GameStates) < 3:
                    self.GameStates.append(Game.Game(self.WindowConfig.size()))
                else:
                    self.GameStates[1] = Game.Game(self.WindowConfig.size())
                self.currentGameState = self.GameStates[GAME]

            if self.next_state == GAME_OVER:
                game_over_screen = GameOver.GameOver(self.WindowConfig.size(),
                                                     self.GameStates[GAME].info.result,
                                                     self.GameStates[GAME].info.score)
                if len(self.GameStates) < 3:
                    self.GameStates.append(game_over_screen)
                else:
                    self.GameStates[GAME_OVER] = game_over_screen
                self.currentGameState = self.GameStates[GAME_OVER]

            if self.next_state == EXIT:
                self.handle = False
            self.prev_state = self.next_state

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.handle = False

    def run(self):
        while self.handle:
            self.handle_events()
            self.update_game_state()
