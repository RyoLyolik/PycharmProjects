import pygame

size = w, h, = 720,480
class BlockUsual:
    def __init__(self, pos_x, pos_y, size, screen):
        self.screen = screen
        self.size = size
        self.color = (255,255,255)
        self.shell = pygame.draw.rect(screen, self.color, (pos_x, pos_y, size, size), 0)

    def draw(self):
        print(self.shell)
        if 720-self.shell.size[0]-21<self.shell.left:
            self.shell = pygame.draw.rect(self.screen, self.color, (
            self.shell.left, self.shell.top, self.size, self.size), 0)
        else:
            self.shell = pygame.draw.rect(self.screen, self.color, (self.shell.right-self.size, self.shell.bottom-self.size, self.size,self.size), 0)


    def get_type(self):
        return 'Usual'

class BadBlock(BlockUsual):
    def __init__(self, pos_x, pos_y, size, screen):
        super().__init__(pos_x, pos_y, size, screen)
        self.color = (235, 50, 50)

    def draw(self):
        super().draw()

    def get_type(self):
        return 'Bad'