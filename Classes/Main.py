import pygame,sys
import pygame.locals
import Classes.Menu as M

class Game:
    def __init__(self):
        print("siema")

    def draw(self, window):
        print("siema")



class GameOver:
    def __init__(self):
        print("elo")

class WindowConfiguration:
    def __init__(self,w,h):
        self.windowSize = (w,h)

    def size(self):
        return  self.windowSize



class Main:
    def __init__(self):
        self.WindowConfig = WindowConfiguration(800,600)
        self.GameStates = (M.Menu(self.WindowConfig.size()),
                           Game(),
                           GameOver())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return True

    def run(self):
        self.currentGameState=self.GameStates[0]
        pygame.init()
        window = pygame.display.set_mode(self.WindowConfig.windowSize)
        while not self.handle_events():
            next_state = self.currentGameState.draw(window)
            if next_state == 0:
                return
            if next_state == 1:
                self.currentGameState=self.GameStates[1]

