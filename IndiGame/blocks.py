import pygame

size = w, h, = 720,480
class BlockUsual:
    def __init__(self, pos_x, pos_y, size, screen, additionally = None):
        self.screen = screen
        self.size = size
        self.addit = additionally
        self.color = (255,255,255)
        self.start_pos = [pos_x, pos_y]
        self.now_pos = [pos_x, pos_y]
        self.shell = pygame.draw.rect(screen, self.color, (pos_x, pos_y, size, size), 0)

    def draw(self):
        pass
        # print(self.add)
        self.shell = pygame.draw.rect(self.screen, self.color, (
            self.now_pos[0], self.now_pos[1], self.size, self.size), 0)

    def get_type(self):
        return 'Usual'

class BadBlock(BlockUsual):
    def __init__(self, pos_x, pos_y, size, screen, additionally = None):
        super().__init__(pos_x, pos_y, size, screen, additionally)
        self.color = (235, 50, 50)

    def draw(self):
        super().draw()

    def get_type(self):
        return 'Bad'