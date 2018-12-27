import pygame

size = w, h, = 720,480
class BlockUsual:
    def __init__(self, pos_x, pos_y, size, screen):
        self.screen = screen
        self.size = size
        self.shell = pygame.draw.rect(screen, (255,255,255), (pos_x, pos_y, size, size), 0)

    def draw(self):
        self.shell = pygame.draw.rect(self.screen, (255,255,255), (self.shell.left, self.shell.top, self.size,self.size), 0)