import pygame
from loading_image import load_image

w,h = 720,480
class UsualEntity:
    def __init__(self, pos_x, pos_y, size, screen, image=None, additionally=0):
        self.screen = screen
        self.addit = additionally
        self.color = (100, 255, 225)

        self.start_pos = [pos_x, pos_y]
        self.now_pos = [pos_x, pos_y]

        self.gravity_force = 1
        self.speed = 2
        self.standart_speed = 2
        self.in_air = True
        self.up = False
        self.left = False
        self.right = False
        self.speed_down = 0
        self.gravity_n = True

        # self.shell = pygame.draw.rect(screen, self.color, (pos_x, pos_y, size, size-0.5*size), 0)

        self.health = 20
        self.die = False
        self.cost = 25
        self.paid = False
        self.stopped = []

        self.reload = 0
        self.power = 0

        self.image = image

        self.image = ('../textures/entities/Knight/knight_1.png')
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image(self.image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.shell = self.sprite.rect
        self.sprite.rect = pygame.Rect(pos_x, pos_y, 96, 96)
        self.size = (96,96)

    def draw(self):
        if self.paid:
            self.cost = 0
            self.health = 0
            self.die = True
        if self.health > 0:
            # self.shell = pygame.draw.rect(self.screen, self.color, (
            #     self.now_pos[0], self.now_pos[1], self.size[0], self.size[1]), 0)
            self.shell = pygame.Rect(self.now_pos[0], self.now_pos[1], self.size[0], self.size[1])
            self.sprite.rect = self.shell
        else:
            self.die = True
            self.health = 0

    def gravity(self):
        if self.health > 0:
            if self.speed_down < 12:
                self.in_air = True
                self.speed_down += self.gravity_force
            else:
                self.speed_down = 13
            # print(self.speed_down)
            self.now_pos[1] += self.speed_down


    def get_type(self):
        return 'Usual_Entity'


class BadEntity(UsualEntity):
    def __init__(self, pos_x, pos_y, size, screen,image=None, additionally = 0):
        super().__init__(pos_x, pos_y, size, screen,image, additionally=0)
        self.color = (255,69,0)
        self.power = 15

        self.image = ('../textures/entities/Knight/knight_1.png')
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image(self.image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.shell = self.sprite.rect

    def draw(self):
        super().draw()

    def gravity(self):
        super().gravity()

    def get_type(self):
        return 'Bad_Entity'
