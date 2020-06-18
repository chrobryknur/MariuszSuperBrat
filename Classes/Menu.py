import pygame

class Menu:
    def __init__(self,wsize):
        self.surface = pygame.display.set_mode(wsize)
        pygame.display.set_caption('Mariusz Super Brat')
        self.initiated = False

    def text_sufrace(self,text, font,color):
        white = (255, 255, 255)
        surf = pygame.Surface(font.size(text))
        surf.fill(white)
        textSurface = font.render(text, True, color, surf)
        return textSurface

    def next_state(self):
        return self.next_s

    def init(self):
        self.background = pygame.image.load("Assets/main_menu_bg.png")
        self.titleText = pygame.font.Font("Assets/pcsenior.ttf", 35)
        self.buttonText = pygame.font.Font("Assets/pcsenior.ttf", 15)
        self.title =       [pygame.Rect(100, 100, 600, 100),(0,0,0), self.text_sufrace("Mariusz Super Brat", self.titleText, (0,96,128))]
        self.game_button = [pygame.Rect(300, 300, 200, 50), (0,0,0), self.text_sufrace("Start game", self.buttonText, (0,128,0))]
        self.quit_button = [pygame.Rect(300, 400, 200, 50), (0,0,0), self.text_sufrace("Quit game", self.buttonText, (0,128,0))]

    def draw(self,screen):
        if not self.initiated:
            self.init()
            self.initiated = True

        clock = pygame.time.Clock()

        handle=True
        while handle:
            self.surface.blit(self.background,(0,0))
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.locals.QUIT:
                    handle=False
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse_pos[0] <= 500:
                        if 300 <= mouse_pos[1] <= 350:
                            self.next_s = 1
                            handle = False
                        if 400 <= mouse_pos[1] <= 450:
                            self.next_s = -1
                            handle = False
                if 300 <= mouse_pos[0] <= 500:
                    if 300 <= mouse_pos[1] <= 350:
                        self.game_button[1] = (255, 0, 0)
                    else:
                        self.game_button[1] = (0, 0, 0)
                    if 400 <= mouse_pos[1] <= 450:
                        self.quit_button[1] = (255, 0, 0)
                    else:
                        self.quit_button[1] = (0, 0, 0)
            self.game_button[2] = self.text_sufrace("Start game", self.buttonText, self.game_button[1])
            self.quit_button[2] = self.text_sufrace("Quit game", self.buttonText, self.quit_button[1])
            pygame.draw.rect(self.surface, self.game_button[1], self.game_button[0], 5)
            pygame.draw.rect(self.surface, self.quit_button[1], self.quit_button[0], 5)
            screen.blit(self.title[2],(95,140))
            screen.blit(self.game_button[2], (332,316))
            screen.blit(self.quit_button[2], (340,416))
            screen.blit(self.surface,(0,0))

            pygame.display.update()
            clock.tick(15)

