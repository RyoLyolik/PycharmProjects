import pygame
import random
import math
import sys
from player import Player
from blocks import  *
from get_collide_side import GetSide
screen = None
size = w, h, = 720,480
player_sprites = ['player_sprite__stay_0.png']
class Window:
    def __init__(self):
        global screen
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('IndiGame')
        self.player = Player(screen)
        self.main_rect = pygame.draw.rect(screen,(0,0,0),(64,64,w-128,h-128),0)
        # self.enemy_list = [Enemy(), Enemy(), Enemy(), Enemy()]
        self.level_data = []
        self.right = False
        self.left = False
        self.load_level()
        pygame.init()

        self.screen_update()

    def load_level(self):
        file = open('LEVELS/lvl_0.txt', 'r')
        level = file.read().split('\n')
        for block in level:
            block = block.split()
            self.level_data.append(BlockUsual(int(block[0]),int(block[1]), int(block[2]), screen))


    def screen_update(self):
        event = True
        while event:
            pygame.time.delay(15)
            for e in pygame.event.get():
                # print(e)
                if e.type == pygame.QUIT:
                    event = False
            # for enemy in self.enemy_list:
            #     enemy.draw_enemy()
            #     enemy.enemy_moving()
            #     self.check_go_out(enemy)
            #     self.colliding(self.player, enemy)
            screen.fill((0, 0, 0))
            self.player.draw_player(screen)
            self.key_events()
            for obj in self.level_data:
                obj.draw()
                self.colliding(obj,self.player)

            # screen.blit(self.player.player_image, self.player.player)

            pygame.display.flip()

    def colliding(self, ob1, pl):
        # print(pl.player.bottom - ob1.shell.top)
        side = GetSide(ob1=ob1, player=pl, l=self.left, r=self.right)
        side = side.getting_side()
        if side[1] == 1:
            self.player.speed = 0
            self.player.player.right = ob1.shell.left - 6
        # if (pl.player.bottom - ob1.shell.top > 0 and pl.player.bottom - ob1.shell.top < ob1.size) or (pl.player.top - ob1.shell.bottom > 0 and pl.player.top - ob1.shell.bottom < ob1.size): # and (pl.player.top < ob1.shell.bottom):
        #     # print(pl.player.left - ob1.shell.right)
        #     if pl.player.right - ob1.shell.left <= 0 and pl.player.right - ob1.shell.left > -5:
        #         if self.left is False:
        #             self.player.speed = 0
        #             self.player.player.right = ob1.shell.left-1
        #
        #     elif pl.player.left - ob1.shell.right <= 0 and pl.player.left - ob1.shell.right > -5:
        #         # print(1)
        #         if self.right is False:
        #             self.player.speed = 0
        #             self.player.player.left = ob1.shell.right+1
        #
        # elif (pl.player.left <= ob1.shell.right and abs(pl.player.left - ob1.shell.right) <= ob1.size) or (pl.player.right >= ob1.shell.left and pl.player.right - ob1.shell.left <= ob1.size):
        #     if pl.player.bottom - ob1.shell.top <= 0 and pl.player.bottom - ob1.shell.top > -12:
        #         self.player.speed_down = 0
        #         # self.player.stopped = True
        #         self.player.in_air = False
        #         self.player.player.bottom = ob1.shell.top
        #
        #     elif pl.player.top - ob1.shell.bottom < 0 and pl.player.top - ob1.shell.bottom < 12:
        #         # self.player.speed_down = 0
        #         if self.player.up:
        #             self.player.speed_down = 0
        #             self.player.player.top = ob1.shell.bottom+1


        if ob1.shell.colliderect(pl.player):
            # print('Произошля колизия')
            pass

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
            self.left = True
            self.right = False
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air is False:  # TODO
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20

            if pygame.key.get_pressed()[pygame.K_LALT]:
                self.player.speed = -20
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.speed = 5
            self.right = True
            self.left = False
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air is False:  # TODO
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20

            if pygame.key.get_pressed()[pygame.K_LALT]:
                self.player.speed = 20

        elif pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air is False: # TODO
            self.player.in_air = True
            self.player.stopped = False
            self.player.speed_down = -20

        else:
            self.player.speed = 0

if __name__ == '__main__':
    win = Window()
    pygame.quit()