import pygame
from loading_image import load_image

size = w, h, = 720, 480


class BlockUsual:
    def __init__(self, pos_x, pos_y, size, screen, image=None, additionally=None):
        self.screen = screen
        self.size = (size, size)
        self.addit = additionally
        self.color = (255, 255, 255)
        self.start_pos = [pos_x, pos_y]
        self.now_pos = [pos_x, pos_y]
        self.image = image
        if self.image is None:
            self.sprite = None
            self.shell = pygame.draw.rect(screen, self.color, (pos_x, pos_y, size, size), 0)

        else:
            self.sprite = pygame.sprite.Sprite()
            print(image)
            self.sprite.image = load_image(image)
            self.sprite.image = pygame.transform.scale(self.sprite.image, (self.size[0], self.size[1]))
            self.sprite.rect = self.sprite.image.get_rect()
            self.shell = self.sprite.rect

    def draw(self):
        self.now_pos[0] = round(self.now_pos[0], 0)
        if self.image is None:
            self.shell = pygame.draw.rect(self.screen, self.color, (
                self.now_pos[0], self.now_pos[1], self.size[0], self.size[1]), 0)
        else:
            self.sprite.rect = pygame.Rect(self.now_pos[0], self.now_pos[1], 64, 64)
            self.shell = self.sprite.rect

    def get_type(self):
        return 'Usual'


class BadBlock(BlockUsual):
    def __init__(self, pos_x, pos_y, size, screen, image=None, additionally=None):
        super().__init__(pos_x, pos_y, size, screen, image, additionally)
        self.color = (235, 50, 50)

    def draw(self):
        super().draw()

    def get_type(self):
        return 'Bad'
