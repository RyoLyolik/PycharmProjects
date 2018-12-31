import pygame

class UsualSword:
    def __init__(self, place, in_hand, screen):
        self.place = place
        self.in_hand = in_hand
        self.size = 16
        self.obj = pygame.draw.rect(screen, (255, 10, 150),
                                       (self.place[0], self.place[1], 16, 16), 0)

    def draw(self, coord, screen):
        print('ok')
        self.obj = pygame.draw.rect(screen, (255, 10, 150),
                                    (*coord, 16, 16), 0)