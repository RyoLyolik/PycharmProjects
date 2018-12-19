import pygame
import random
import math
import sys
screen = None
size = w, h, = 720,480
class Window:
    def __init__(self):
        global screen
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('IndiGame')
        self.player = Player()
        self.main_rect = pygame.draw.rect(screen,(0,0,0),(64,64,w-128,h-128),0)
        # self.enemy_list = [Enemy(), Enemy(), Enemy(), Enemy()]
        pygame.init()

        self.screen_update()

    def screen_update(self):
        event = True
        while event:
            pygame.time.delay(15)
            for e in pygame.event.get():
                print(e)
                if e.type == pygame.QUIT:
                    event = False
            # for enemy in self.enemy_list:
            #     enemy.draw_enemy()
            #     enemy.enemy_moving()
            #     self.check_go_out(enemy)
            #     self.colliding(self.player, enemy)
            screen.fill((0, 0, 0))
            self.key_events()
            self.player.draw_player()
            pygame.display.flip()

    def colliding(self, ob1, ob2):
        if ob1.player.colliderect(ob2.player):
            screen.fill(pygame.Color('#ffcc00'), ob1.player.clip(ob2.player))

        if ob1.player.colliderect(ob2.player):
            if ob1.player.clip(ob2.player).size[0] < ob1.player.clip(ob2.player).size[1]:
                ob2.speed = -ob2.speed
                ob1.speed = 0
            if ob1.player.clip(ob2.player).size[1] < ob1.player.clip(ob2.player).size[0]:
                ob2.speed2 = -ob2.speed2
                ob1.speed2 = 0
            if ob1.player.clip(ob2.player).size[0] == ob1.player.clip(ob2.player).size[1]:
                ob2.speed = -ob2.speed
                ob2.speed2 = -ob2.speed2
                ob1.speed = 0
                ob1.speed2 = 0
        else:
            ob1.speed = 2
            ob1.speed2 = 2
        # print(ob1.clip(ob2))

    def check_go_out(self, ob):
        # print(self.main_rect.colliderect(ob.player))
        if self.main_rect.colliderect(ob.player) == 0:
            if ob.player.left < self.main_rect.left or ob.player.right > self.main_rect.right:
                ob.speed = -ob.speed
            if ob.player.top < self.main_rect.top or ob.player.bottom > self.main_rect.bottom:
                ob.speed2 = -ob.speed2

    def key_events(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.speed = -5
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air == False:  # TODO
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.speed = 5
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air == False:  # TODO
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20

        elif pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air == False: # TODO
            self.player.in_air = True
            self.player.stopped = False
            self.player.speed_down = -20
        else:
            self.player.speed = 0




class Player:
    def __init__(self):
        global screen

        self.player_size = 64
        self.speed = 0
        self.pos_x = 190
        self.pos_y = 60

        self.in_air = True
        self.stopped = False

        self.gravity_force = 1
        self.speed_down = 0

        self.player = pygame.draw.rect(screen, (200, 100, 150),
                                       (self.pos_x, self.pos_y, self.player_size, self.player_size), 0)
        # self.draw_player()


    def draw_player(self):
        self.player = pygame.draw.rect(screen, (200, 100, 150), (self.player.left, self.player.top, self.player_size, self.player_size), 0)

        self.move([self.speed,self.speed_down])
        self.gravity()

    def move(self, speed):
        self.player = self.player.move(speed)

    def gravity(self):
        if self.player.bottom < h - 40 and self.stopped is False:
            self.in_air = True
            self.speed_down += self.gravity_force
        else:
            self.in_air = False
            self.speed_down = 0
            self.stopped = True
            self.player.bottom = h - 41


    def limit_reached(self):
        pass




# class Enemy(Player):
#     def __init__(self):
#         super().__init__()
#         self.speed = random.choice(range(-5,5))
#         self.speed2 = random.choice(range(-5, 5))
#         self.pos_x = random.choice(range(64,656))
#         self.pos_y = random.choice(range(64,416))
#         self.player = pygame.draw.rect(screen, (200, 100, 150),
#                                        (self.pos_x, self.pos_y, self.player_size, self.player_size), 0)
#         self.enemy_moving()
#
#     def draw_enemy(self):
#         super().draw_player()
#
#     def enemy_moving(self):
#         self.player = self.player.move([self.speed, self.speed2])



if __name__ == '__main__':
    win = Window()
    pygame.quit()