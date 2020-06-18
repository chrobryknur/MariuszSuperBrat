import pygame

class Menu:
    def __init__(self,wsize):
        self.surface = pygame.display.set_mode((wsize[0], wsize[1]))
        pygame.display.set_caption('Mariusz Super Brat')

    def text_sufrace(self,text, font,color):
        white = (255, 255, 255)
        surf = pygame.Surface(font.size(text))
        surf.fill(white)
        textSurface = font.render(text, True, color, surf)
        return textSurface

    def next_state(self):
        return self.next_s

    def draw(self,screen):
        clock = pygame.time.Clock()

        background = pygame.image.load("Assets/main_menu_bg.png")
        titleText = pygame.font.Font("Assets/pcsenior.ttf", 35)
        buttonText = pygame.font.Font("Assets/pcsenior.ttf", 15)
        title =       [pygame.Rect(100, 100, 600, 100),(0,0,0), self.text_sufrace("Mariusz Super Brat", titleText, (0,96,128))]
        game_button = [pygame.Rect(300, 300, 200, 50), (0,0,0), self.text_sufrace("Start game", buttonText, (0,128,0))]
        quit_button = [pygame.Rect(300, 400, 200, 50), (0,0,0), self.text_sufrace("Quit game", buttonText, (0,128,0))]

        handle=True
        while handle:
            self.surface.blit(background,(0,0))
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.locals.QUIT:
                    handle=False
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse_pos[0] <= 500:
                        if 300 <= mouse_pos[1] <= 350:
                            self.next_s = 1
                        if 400 <= mouse_pos[1] <= 450:
                            self.next_s = 0
                if 300 <= mouse_pos[0] <= 500:
                    if 300 <= mouse_pos[1] <= 350:
                        game_button[1] = (255, 0, 0)
                    else:
                        game_button[1] = (0, 0, 0)
                    if 400 <= mouse_pos[1] <= 450:
                        quit_button[1] = (255, 0, 0)
                    else:
                        quit_button[1] = (0, 0, 0)
            game_button[2] = self.text_sufrace("Start game", buttonText, game_button[1])
            quit_button[2] = self.text_sufrace("Quit game", buttonText, quit_button[1])
            pygame.draw.rect(self.surface, game_button[1], game_button[0], 5)
            pygame.draw.rect(self.surface, quit_button[1], quit_button[0], 5)
            screen.blit(title[2],(95,140))
            screen.blit(game_button[2], (332,316))
            screen.blit(quit_button[2], (340,416))
            screen.blit(self.surface,(0,0))

            pygame.display.update()
            clock.tick(15)

