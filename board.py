import pygame
import color

class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 80
        self.height = 80

        self.is_hovered = False
        self.is_selected = False

    def draw(self, surface):
        pygame.draw.rect(surface, color.white, (self.x, self.y, self.width, self.height))

        if self.is_hovered:
            pygame.draw.rect(surface, color.blue, (self.x + 3, self.y + 3, self.width - 6, self.height - 6), 3)
        else:
            pass

        if self.is_selected:
            pygame.draw.rect(surface, color.green, (self.x + 3, self.y + 3, self.width - 6, self.height - 6), 3)
        else:
            pass

    def update(self):
        # Check for mouse hover and change color
        mouse_pos = pygame.mouse.get_pos()

        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                self.is_hovered = True
            else:
                self.is_hovered = False
        else:
            self.is_hovered = False

        if pygame.mouse.get_pressed()[0]:
            if self.is_hovered:
                self.is_selected = True
            else:
                self.is_selected = False

class Board():
    def __init__(self):
        # BOX 1 TILES
        self.tile11 = Tile(5, 5)
        self.tile12 = Tile(88, 5)
        self.tile13 = Tile(171, 5)
        self.tile14 = Tile(5, 88)
        self.tile15 = Tile(88, 88)
        self.tile16 = Tile(171, 88)
        self.tile17 = Tile(5, 171)
        self.tile18 = Tile(88, 171)
        self.tile19 = Tile(171, 171)

        # BOX 2 TILES
        self.tile21 = Tile(256, 5)
        self.tile22 = Tile(339, 5)
        self.tile23 = Tile(422, 5)
        self.tile24 = Tile(256, 88)
        self.tile25 = Tile(339, 88)
        self.tile26 = Tile(422, 88)
        self.tile27 = Tile(256, 171)
        self.tile28 = Tile(339, 171)
        self.tile29 = Tile(422, 171)

        # BOX 3 TILES
        self.tile31 = Tile(507, 5)
        self.tile32 = Tile(590, 5)
        self.tile33 = Tile(673, 5)
        self.tile34 = Tile(507, 88)
        self.tile35 = Tile(590, 88)
        self.tile36 = Tile(673, 88)
        self.tile37 = Tile(507, 171)
        self.tile38 = Tile(590, 171)
        self.tile39 = Tile(673, 171)

        # BOX 4 TILES
        self.tile41 = Tile(5, 256)
        self.tile42 = Tile(88, 256)
        self.tile43 = Tile(171, 256)
        self.tile44 = Tile(5, 339)
        self.tile45 = Tile(88, 339)
        self.tile46 = Tile(171, 339)
        self.tile47 = Tile(5, 422)
        self.tile48 = Tile(88, 422)
        self.tile49 = Tile(171, 422)

        # BOX 5 TILES
        self.tile51 = Tile(256, 256)
        self.tile52 = Tile(339, 256)
        self.tile53 = Tile(422, 256)
        self.tile54 = Tile(256, 339)
        self.tile55 = Tile(339, 339)
        self.tile56 = Tile(422, 339)
        self.tile57 = Tile(256, 422)
        self.tile58 = Tile(339, 422)
        self.tile59 = Tile(422, 422)

        # BOX 6 TILES
        self.tile61 = Tile(507, 256)
        self.tile62 = Tile(590, 256)
        self.tile63 = Tile(673, 256)
        self.tile64 = Tile(507, 339)
        self.tile65 = Tile(590, 339)
        self.tile66 = Tile(673, 339)
        self.tile67 = Tile(507, 422)
        self.tile68 = Tile(590, 422)
        self.tile69 = Tile(673, 422)

        # BOX 7 TILES
        self.tile71 = Tile(5, 507)
        self.tile72 = Tile(88, 507)
        self.tile73 = Tile(171, 507)
        self.tile74 = Tile(5, 590)
        self.tile75 = Tile(88, 590)
        self.tile76 = Tile(171, 590)
        self.tile77 = Tile(5, 673)
        self.tile78 = Tile(88, 673)
        self.tile79 = Tile(171, 673)

        # BOX 8 TILES
        self.tile81 = Tile(256, 507)
        self.tile82 = Tile(339, 507)
        self.tile83 = Tile(422, 507)
        self.tile84 = Tile(256, 590)
        self.tile85 = Tile(339, 590)
        self.tile86 = Tile(422, 590)
        self.tile87 = Tile(256, 673)
        self.tile88 = Tile(339, 673)
        self.tile89 = Tile(422, 673)

        # BOX 9 TILES
        self.tile91 = Tile(507, 507)
        self.tile92 = Tile(590, 507)
        self.tile93 = Tile(673, 507)
        self.tile94 = Tile(507, 590)
        self.tile95 = Tile(590, 590)
        self.tile96 = Tile(673, 590)
        self.tile97 = Tile(507, 673)
        self.tile98 = Tile(590, 673)
        self.tile99 = Tile(673, 673)

        self.tiles = [
            self.tile11, self.tile12, self.tile13, self.tile14, self.tile15, self.tile16, self.tile17, self.tile18, self.tile19,
            self.tile21, self.tile22, self.tile23, self.tile24, self.tile25, self.tile26, self.tile27, self.tile28, self.tile29,
            self.tile31, self.tile32, self.tile33, self.tile34, self.tile35, self.tile36, self.tile37, self.tile38, self.tile39,
            self.tile41, self.tile42, self.tile43, self.tile44, self.tile45, self.tile46, self.tile47, self.tile48, self.tile49,
            self.tile51, self.tile52, self.tile53, self.tile54, self.tile55, self.tile56, self.tile57, self.tile58, self.tile59,
            self.tile61, self.tile62, self.tile63, self.tile64, self.tile65, self.tile66, self.tile67, self.tile68, self.tile69,
            self.tile71, self.tile72, self.tile73, self.tile74, self.tile75, self.tile76, self.tile77, self.tile78, self.tile79,
            self.tile81, self.tile82, self.tile83, self.tile84, self.tile85, self.tile86, self.tile87, self.tile88, self.tile89,
            self.tile91, self.tile92, self.tile93, self.tile94, self.tile95, self.tile96, self.tile97, self.tile98, self.tile99
        ]

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)

    def update(self):
        for tile in self.tiles:
            tile.update()