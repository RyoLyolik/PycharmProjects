import pygame
import random
import math
import sys
screen = None
size = w, h, = 720,480
player_sprites = ['player_sprite__stay_0.png']
class Window:
    def __init__(self):
        global screen
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('IndiGame')
        self.player = Player()
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
            self.level_data.append(BlockUsual(int(block[0]),int(block[1]), int(block[2])))


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
            self.player.draw_player(0)
            self.key_events()
            for obj in self.level_data:
                obj.draw()
                self.colliding(obj,self.player)

            # screen.blit(self.player.player_image, self.player.player)

            pygame.display.flip()

    def colliding(self, ob1, pl):
        # print(pl.player.bottom - ob1.shell.top)
        if (pl.player.bottom - ob1.shell.top > 0 and pl.player.bottom - ob1.shell.top < ob1.size) or (pl.player.top - ob1.shell.bottom > 0 and pl.player.top - ob1.shell.bottom < ob1.size): # and (pl.player.top < ob1.shell.bottom):
            # print(pl.player.left - ob1.shell.right)
            if pl.player.right - ob1.shell.left <= 0 and pl.player.right - ob1.shell.left > -5:
                if self.left is False:
                    self.player.speed = 0
                    self.player.player.right = ob1.shell.left-1

            elif pl.player.left - ob1.shell.right <= 0 and pl.player.left - ob1.shell.right > -5:
                # print(1)
                if self.right is False:
                    self.player.speed = 0
                    self.player.player.left = ob1.shell.right+1

        elif (pl.player.left <= ob1.shell.right and abs(pl.player.left - ob1.shell.right) <= ob1.size) or (pl.player.right >= ob1.shell.left and pl.player.right - ob1.shell.left <= ob1.size):
            if pl.player.bottom - ob1.shell.top <= 0 and pl.player.bottom - ob1.shell.top > -12:
                self.player.speed_down = 0
                # self.player.stopped = True
                self.player.in_air = False
                self.player.player.bottom = ob1.shell.top

            elif pl.player.top - ob1.shell.bottom < 0 and pl.player.top - ob1.shell.bottom < 12:
                # self.player.speed_down = 0
                if self.player.up:
                    self.player.speed_down = 0
                    self.player.player.top = ob1.shell.bottom+1


        # if (pl.player.left - ob1.shell.right <= 0 and pl.player.left - ob1.shell.right > -5) or (pl.player.right - ob1.shell.left <= 0 and pl.player.right - ob1.shell.left > -5):
        #     if pl.player.bottom - ob1.shell.top <= 0 and pl.player.bottom - ob1.shell.top > -32:
        #         self.player.speed_down = 0
        #
        #     elif pl.player.top - ob1.shell.bottom <= 0 and pl.player.top - ob1.shell.bottom > -32:
        #         print(1)
        #         self.player.speed_down = 0


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




class Player:
    def __init__(self):
        global screen, player_sprites

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


    def draw_player(self, i):
        # self.player_image = pygame.image.load(player_sprites[i])
        # self.player = self.player_image.get_rect()
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


class BlockUsual:
    def __init__(self, pos_x, pos_y, size):
        self.size = size
        self.shell = pygame.draw.rect(screen, (255,255,255), (pos_x, pos_y, size, size), 0)

    def draw(self):
        self.shell = pygame.draw.rect(screen, (255,255,255), (self.shell.left, self.shell.top, self.size,self.size), 0)




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