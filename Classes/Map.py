import pygame

SKY = "."
BRICK = "#"
PIPE = "/"

class Map:
    def __init__(self):
        self.tile_x, self.tile_y = 32, 32

    def load_tile(self, type, x, y):
        image = 0
        if type == SKY:
            image = 0
        elif type == BRICK:
            image = pygame.image.load("Assets/brick.png").convert()
        image_width, image_height = 32,32
        rect = (x * image_width, y * image_height, image_width, image_height)
        return [image, rect]

    def load_level(self):
        file = open("Levels/Level1", "r")
        level = []
        self.level_repr = []
        for i in range(0, 19):
            l = []
            level.append(l)
            line = file.readline()
            self.level_repr.append(line)
            for j in range(0, 79):
                l.append(self.load_tile(line[j], j, i))
        return level

    def draw_map(self,level,surface,dx,dy):
        for x, row in enumerate(level):
            for y, tile in enumerate(row):
                if tile[0]:
                    pygame.draw.rect(surface, (0, 0, 0, 0), tile[1])
                    surface.blit(tile[0], (tile[1][0] + dx, tile[1][1] + dy))
        return surface