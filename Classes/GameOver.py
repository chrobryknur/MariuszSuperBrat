import pygame


class GameOver:
    def __init__(self, wsize, result, score):
        self.surface = pygame.display.set_mode(wsize)
        self.initiated = False
        self.handle = True
        self.result = result
        self.score = score
        self.background = pygame.image.load("../Assets/main_menu_bg.png")
        self.titleText = pygame.font.Font("../Assets/pcsenior.ttf", 40)
        self.scoreText = pygame.font.Font("../Assets/pcsenior.ttf", 25)
        self.buttonText = pygame.font.Font("../Assets/pcsenior.ttf", 15)
        if self.result == "won":
            self.title = [pygame.Rect(100, 100, 600, 100), (0, 0, 0),
                          self.text_surface("You won!", self.titleText, (0, 200, 64))]
        else:
            self.title = [pygame.Rect(100, 100, 600, 100), (0, 0, 0),
                          self.text_surface("You lost!", self.titleText, (255, 0 , 0))]
        self.score = [pygame.Rect(300, 200, 400, 100), (0, 0, 0),
                      self.text_surface("Score: " + str(self.score), self.scoreText, (0, 96, 128))]
        self.restart_button = [pygame.Rect(300, 300, 200, 50), (0, 0, 0),
                               self.text_surface("Play again", self.buttonText, (0, 128, 0))]
        self.quit_button = [pygame.Rect(300, 400, 200, 50), (0, 0, 0),
                            self.text_surface("Quit game", self.buttonText, (0, 128, 0))]

    def text_surface(self, text, font, color):
        white = (255, 255, 255)
        surf = pygame.Surface(font.size(text))
        surf.fill(white)
        textSurface = font.render(text, True, color, surf)
        return textSurface

    def next_state(self):
        return self.next_s

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.handle = False
                self.next_s = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.restart_button[0].collidepoint(event.pos):
                        self.next_s = 1
                        self.handle = False
                    if self.quit_button[0].collidepoint(event.pos):
                        self.next_s = -1
                        self.handle = False
            if self.restart_button[0].collidepoint(pygame.mouse.get_pos()):
                self.restart_button[1] = (255, 0, 0)
            else:
                self.restart_button[1] = (0, 0, 0)
            if self.quit_button[0].collidepoint(pygame.mouse.get_pos()):
                self.quit_button[1] = (255, 0, 0)
            else:
                self.quit_button[1] = (0, 0, 0)

    def update_surface(self):
        self.surface.blit(self.background, (0, 0))
        self.restart_button[2] = self.text_surface("Restart game", self.buttonText, self.restart_button[1])
        self.quit_button[2] = self.text_surface("Quit game", self.buttonText, self.quit_button[1])
        pygame.draw.rect(self.surface, self.restart_button[1], self.restart_button[0], 5)
        pygame.draw.rect(self.surface, self.quit_button[1], self.quit_button[0], 5)

    def update_screen(self,screen):
        if self.result == "won":
            screen.blit(self.title[2], (260, 140))
        else:
            screen.blit(self.title[2], (250,140))
        screen.blit(self.score[2], (302, 250))
        screen.blit(self.restart_button[2], (312, 316))
        screen.blit(self.quit_button[2], (340, 416))
        screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def draw(self, screen):
        while self.handle:
            self.handle_events()
            self.update_surface()
            self.update_screen(screen)

