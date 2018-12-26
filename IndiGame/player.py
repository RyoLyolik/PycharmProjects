import pygame
size = w, h, = 720,480
class Player:
    def __init__(self, screen):

        self.player_size = 64
        self.speed = 0
        self.pos_x = 190
        self.pos_y = 60


        self.double_jump = 2
        self.in_air = True
        self.stopped = False
        self.up = False

        self.gravity_force = 1
        self.speed_down = 0

        self.player = pygame.draw.rect(screen, (200, 100, 150),
                                       (self.pos_x, self.pos_y, self.player_size, self.player_size), 0)
        # self.draw_player()


    def draw_player(self, screen):
        self.player = pygame.draw.rect(screen, (150,100,70), (self.player.left, self.player.top, self.player_size, self.player_size), 0)

        self.move([self.speed,self.speed_down])
        self.gravity()

    def move(self, speed):
        self.player = self.player.move(speed)

    def gravity(self):
        if self.player.bottom < h - 40 and self.stopped is False:
            self.in_air = True
            self.speed_down += self.gravity_force
            if self.speed_down < 0:
                self.up = True
            else:
                self.up = False
        else:
            self.double_jump = 0
            self.in_air = False
            self.speed_down = 0
            self.stopped = True
            self.player.bottom = h - 41


    def limit_reached(self):
        pass