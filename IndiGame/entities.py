import pygame

w,h = 720,480
class UsualEntity:
    def __init__(self, pos_x, pos_y, size, screen, additionally = 0):
        self.screen = screen
        self.size = (size, size//2)
        self.addit = additionally
        self.color = (100, 255, 75)
        self.start_pos = [pos_x, pos_y]
        self.now_pos = [pos_x, pos_y]
        self.gravity_force = 1
        self.speed = 1
        self.stopped = False
        self.in_air = True
        self.up = False
        self.left = False
        self.right = False
        self.speed_down = 0
        self.gravity_n = True
        self.shell = pygame.draw.rect(screen, self.color, (pos_x, pos_y, size, size-0.5*size), 0)

    def draw(self):
        self.shell = pygame.draw.rect(self.screen, self.color, (
            self.now_pos[0], self.now_pos[1], self.size[0], self.size[1]), 0)

    def gravity(self):
        if self.speed_down < 12:
            self.speed_down += self.gravity_force
        else:
            self.speed_down = 13
        self.now_pos[1] += self.speed_down


    def get_type(self):
        return 'Usual_Entity'


class BadEntity(UsualEntity):
    def __init__(self, pos_x, pos_y, size, screen, additionally = 0):
        super().__init__(pos_x, pos_y, size, screen, additionally=0)
        self.color = (255,69,0)

    def draw(self):
        super().draw()

    def gravity(self):
        super().gravity()

    def get_type(self):
        return 'Bad_Entity'
