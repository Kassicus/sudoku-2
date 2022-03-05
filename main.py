import pygame
import color

pygame.init()

class Game():
    def __init__(self):
        self.width = 1000
        self.height = 800

        self.title = "Sudoku 2"

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.white)

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()