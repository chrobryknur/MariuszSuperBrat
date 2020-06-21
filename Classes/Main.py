import pygame.locals
import Classes.Menu as Menu
import Classes.Game as Game
import Classes.GameOver as GameOver

import pygame

class WindowConfiguration:
    def __init__(self, w, h):
        self.windowSize = (w, h)

    def size(self):
        return self.windowSize


class Main:
    def __init__(self):
        self.WindowConfig = WindowConfiguration(800, 600)
        self.GameStates = [Menu.Menu(self.WindowConfig.size())]
        self.prev_state = -2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return True

    def run(self):
        self.currentGameState = self.GameStates[0]
        pygame.init()
        window = pygame.display.set_mode(self.WindowConfig.windowSize)
        pygame.display.set_caption('Mariusz Super Brat')
        while not self.handle_events():
            self.currentGameState.draw(window)
            self.next_state = self.currentGameState.next_state()
            if self.next_state != self.prev_state:
                if self.next_state == 1:
                    if len(self.GameStates) < 3:
                        self.GameStates.append(Game.Game(self.WindowConfig.size()))
                    else:
                        self.GameStates[1] = Game.Game(self.WindowConfig.size())
                    self.currentGameState = self.GameStates[1]
                if self.next_state == 2:
                    game_over_screen = GameOver.GameOver(self.WindowConfig.size(),
                                       self.GameStates[1].info.result,
                                       self.GameStates[1].info.score)
                    if len(self.GameStates) < 3:
                        self.GameStates.append(game_over_screen)
                    else:
                        self.GameStates[2] = game_over_screen
                    self.currentGameState = self.GameStates[2]
                if self.next_state == -1:
                    break
                self.prev_state = self.next_state
