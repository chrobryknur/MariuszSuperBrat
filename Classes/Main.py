import pygame.locals
import Classes.Menu as Menu
import Classes.Game as Game

import pygame

class GameOver:
    def __init__(self):
        print("siema")


class WindowConfiguration:
    def __init__(self, w, h):
        self.windowSize = (w, h)

    def size(self):
        return self.windowSize


class Main:
    def __init__(self):
        self.WindowConfig = WindowConfiguration(800, 600)
        self.GameStates = (Menu.Menu(self.WindowConfig.size()),
                           Game.Game(self.WindowConfig.size()),
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
