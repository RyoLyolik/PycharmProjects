import pygame
from loading_image import load_image

class UsualSword:
    def __init__(self, place, in_hand, screen):
        self.place = place
        self.in_hand = in_hand
        self.image = '../textures/items/usual_sword.png'

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image('../textures/items/usual_sword.png')
        self.sprite.image_default = load_image('../textures/items/usual_sword.png')
        self.sprite.image_flip = load_image('../textures/items/usual_sword_flip.png')
        self.sprite.rect = self.sprite.image.get_rect()
        self.obj = self.sprite.rect
        self.changed_in_inv = False

        self.power = 5
        self.upgrade_cost = 25
        self.level = 1

    def draw(self, coord, screen):
        self.obj = pygame.Rect(*coord, 48, 48)
        self.sprite.rect = self.obj

    def get_type(self):
        return 'Usual_Sword'

class SecretSword(UsualSword):
    def __init__(self, place, in_hand, screen):
        super().__init__(place, in_hand,screen)
        self.image = '../textures/items/secret_sword.png'

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image('../textures/items/secret_sword.png')
        self.sprite.image_default = load_image('../textures/items/secret_sword.png')
        self.sprite.image_flip = load_image('../textures/items/secret_sword_flip.png')

        self.power = 1
        self.upgrade_cost = 0
        self.level = 0

    def draw(self, coord, screen):
        self.level = 0
        super().draw(coord,screen)

    def get_type(self):
        return 'Secret_Sword'

class Hand:
    def __init__(self, place, in_hand):
        self.place = place
        self.in_hand = in_hand
        self.size = 16
        # self.obj = pygame.draw.rect(screen, (255, 10, 150),
        #                                (self.place[0], self.place[1], 0, 0), 0)
        self.power = 0
        self.image = '../textures/items/hand.png'
    #
    # def draw(self, coord, screen):
    #     self.obj = pygame.draw.rect(screen, (255, 10, 150),
    #                                 (*coord, 0, 0), 0)

    def get_type(self):
        return 'Hand'