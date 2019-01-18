import pygame
from loading_image import load_image

class UsualSword:
    def __init__(self, place, in_hand, screen):
        self.place = place
        self.in_hand = in_hand
        self.size = 16
        self.power = 5

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image('../textures/items/usual_sword.png')
        self.sprite.rect = self.sprite.image.get_rect()
        self.obj = self.sprite.rect
        self.changed_in_inv = False

    def draw(self, coord, screen):
        self.obj = pygame.Rect(*coord, 16, 16)
        self.sprite.rect = self.obj

    def get_type(self):
        return 'Usual Sword'

class Hand:
    def __init__(self, place, in_hand, screen):
        self.place = place
        self.in_hand = in_hand
        self.size = 16
        self.obj = pygame.draw.rect(screen, (255, 10, 150),
                                       (self.place[0], self.place[1], 0, 0), 0)
        self.power = 1

    def draw(self, coord, screen):
        self.obj = pygame.draw.rect(screen, (255, 10, 150),
                                    (*coord, 0, 0), 0)

    def get_type(self):
        return 'Hand'
