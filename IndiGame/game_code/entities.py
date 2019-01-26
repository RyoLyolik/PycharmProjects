import pygame
from loading_image import load_image


font = pygame.font.SysFont('comicsansms', 20)

w,h = 720,480
class UsualEntity:
    def __init__(self, pos_x, pos_y, size, screen, image=None, additionally=0, power=0, health=25, cost=25):
        print(health)
        self.screen = screen
        self.addit = additionally
        self.color = (100, 255, 225)
        self.screen = screen

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

        self.health = health
        self.die = False
        self.cost = cost
        self.paid = False
        self.stopped = []

        self.reload = 0
        self.power = 0

        self.image = image

        self.image = ('../textures/entities/Knight/knight_1.png')
        self.image_flip = load_image(self.image)
        self.image_default = load_image('../textures/entities/Knight/knight_-1.png')
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image(self.image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.shell = self.sprite.rect
        self.sprite.rect = pygame.Rect(pos_x, pos_y, 96, 96)
        self.size = (96,96)

    def draw(self):
        self.now_pos[0] = round(self.now_pos[0],0)
        if self.paid:
            self.cost = 0
            self.health = 0
            self.die = True
        if self.health > 0:
            health_text = font.render(str(self.health), 1,(255, 55, 100))
            self.screen.blit(health_text, (self.now_pos[0]+self.size[0]//2, self.now_pos[1]-40))
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
    def __init__(self, pos_x, pos_y, size, screen,image=None, additionally = 0, power=5, health=25, cost=25):
        super().__init__(pos_x, pos_y, size, screen,image, additionally=0, health=health,power=power, cost=cost)
        self.color = (255,69,0)
        self.power = power

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