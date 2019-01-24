import pygame
from loading_image import load_image

class Upgrade:
    def __init__(self):
        self.on_display = False
        self.all_sprites = pygame.sprite.Group()

    def draw(self, screen, obj=None):
        if self.on_display:
            pygame.draw.rect(screen, (75,50,26), (20,50, 200,100), 0)
            pygame.draw.rect(screen, (140, 75, 39), (30, 60, 50, 50), 0)

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = load_image(obj.image)
            self.sprite.rect = self.sprite.image.get_rect()
            self.sprite.rect = (31, 61, 48, 48)
            self.all_sprites.add(self.sprite)
            self.all_sprites.draw(screen)