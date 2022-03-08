import pygame
import color

class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 80
        self.height = 80

        self.rect = (self.x, self.y, self.width, self.height)

        self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, color.white, self.rect)

        if self.active:
            pygame.draw.rect(surface, color.green, self.rect)

        if self.check_hover():
            pygame.draw.rect(surface, color.blue, self.rect)

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            if self.check_hover():
                self.active = True
            else:
                self.active = False

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                return True
            else:
                return False
        else:
            return False

# The Region class controls a 3*3 "region" of Tiles.
class Region():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.tile1 = Tile(self.x, self.y)
        self.tile2 = Tile(self.x + 83, self.y)
        self.tile3 = Tile(self.x + 166, self.y)
        self.tile4 = Tile(self.x, self.y + 83)
        self.tile5 = Tile(self.x + 83, self.y + 83)
        self.tile6 = Tile(self.x + 166, self.y + 83)
        self.tile7 = Tile(self.x, self.y + 166)
        self.tile8 = Tile(self.x + 83, self.y + 166)
        self.tile9 = Tile(self.x + 166, self.y + 166)

        self.tiles = [
            self.tile1, self.tile2, self.tile3,
            self.tile4, self.tile5, self.tile6,
            self.tile7, self.tile8, self.tile9
        ]

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)

    def update(self):
        for tile in self.tiles:
            tile.update()

class Board():
    def __init__(self):
        self.region1 = Region(5, 5)
        self.region2 = Region(256, 5)
        self.region3 = Region(507, 5)
        self.region4 = Region(5, 256)
        self.region5 = Region(256, 256)
        self.region6 = Region(507, 256)
        self.region7 = Region(5, 507)
        self.region8 = Region(256, 507)
        self.region9 = Region(507, 507)

        self.regions = [
            self.region1, self.region2, self.region3,
            self.region4, self.region5, self.region6,
            self.region7, self.region8, self.region9
        ]

    def draw(self, surface):
        for region in self.regions:
            region.draw(surface)

    def update(self):
        for region in self.regions:
            region.update()