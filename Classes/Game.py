import pygame

SKY = "."
BRICK = "#"
PIPE = "/"

class Game:
    def __init__(self):
        self.level = self.load_level()

    def next_state(self):
        return self.next_s

    def load_level(self):
        file = open("Levels/Level1","r")
        print(file.readline())

    def draw(self):
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
                        if 400 <= mouse_pos[1] <= 450:
                            self.next_s = 0
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
