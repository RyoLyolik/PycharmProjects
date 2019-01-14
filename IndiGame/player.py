import pygame

size = w, h, = 720, 480
class Player:
    def __init__(self, screen):

        self.player_size = 64
        self.speed = 0
        self.pos_x = 128
        self.pos_y = 60


        self.double_jump = 2
        self.in_air = True
        self.stopped = False
        self.up = False

        self.gravity_force = 1
        self.speed_down = 0

        self.money = 0

        self.player = pygame.draw.rect(screen, (200, 100, 150),
                                       (self.pos_x, self.pos_y, self.player_size, self.player_size), 0)
        # self.draw_player()
        self.hand_obj_pos = [0, 0]
        self.hand_obj = None
        self.player_power = self.hand_obj.power if self.hand_obj is not None else 1
        self.max_health = 100
        self.health = self.max_health

        self.regen_cnt = 0
        self.regen = 1


    def draw_player(self, screen):
        self.player = pygame.draw.rect(screen, (150, 100, 70), (
            self.player.left, self.player.top, self.player_size, self.player_size), 0)
        self.move([self.speed, self.speed_down])
        self.gravity()
        self.actions()

    def get_hand_obj(self):
        return self.hand_obj

    def move(self, speed):
        self.player = self.player.move(speed)

    def gravity(self):
        if self.stopped is False:
            self.in_air = True
            if self.speed_down < 12:
                self.speed_down += self.gravity_force
            else:
                self.speed_down = 13
            if self.speed_down < 0:
                self.up = True
            else:
                self.up = False
        else:
            self.double_jump = 0
            self.in_air = False
            self.speed_down = 0
            self.stopped = True

    def actions(self):
        self.player_power = self.hand_obj.power if self.hand_obj is not None else 1


