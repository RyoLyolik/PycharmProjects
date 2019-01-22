import pygame
import random
import math
import sys
from player import Player
from blocks import *
from character_interaction import *
from entities import *
from inventory import *
from inventory_objcets import *
from loading_image import load_image


def round_to(num, rounded_to=3):
    if int(num) == num:
        return str(int(num)) + '.' + '0' * rounded_to
    elif int(num) != num:
        return str(round(num, rounded_to))
    else:
        raise ValueError


screen = None
size = w, h, = 720, 480
obj_type = {
    'usual': BlockUsual,
    'bad': BadBlock,
    'usual_entity': UsualEntity,
    'bad_entity': BadEntity
}
clock = pygame.time.Clock()
print(dir(pygame))
pygame.init()
font = pygame.font.SysFont('comicsansms', 25)

class Window:
    def __init__(self, lvl):
        global screen
        self.lvl = str(lvl)
        self.inv = Invent(8, 5)
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption('IndiGame')
        self.player = Player(screen)
        self.inv_data = [[Hand((0, 0), True, screen), UsualSword((0, 1), False, screen),
                          Hand((0, 2), False, screen),
                          Hand((0, 3), False, screen), Hand((0, 4), False, screen)],
                         [Hand((1, 0), False, screen), Hand((1, 1), False, screen),
                          Hand((1, 2), False, screen),
                          Hand((1, 3), False, screen), Hand((1, 4), False, screen)],
                         [Hand((2, 0), False, screen), Hand((2, 1), False, screen),
                          Hand((2, 2), False, screen),
                          Hand((2, 3), False, screen), Hand((2, 4), False, screen)],
                         [Hand((3, 0), False, screen), Hand((3, 1), False, screen),
                          Hand((3, 2), False, screen),
                          Hand((3, 3), False, screen), Hand((3, 4), False, screen)],
                         [Hand((4, 0), False, screen), Hand((4, 1), False, screen),
                          Hand((4, 2), False, screen),
                          Hand((4, 3), False, screen), Hand((4, 4), False, screen)],
                         [Hand((5, 0), False, screen), Hand((5, 1), False, screen),
                          Hand((5, 2), False, screen),
                          Hand((5, 3), False, screen), Hand((5, 4), False, screen)],
                         [Hand((6, 0), False, screen), Hand((6, 1), False, screen),
                          Hand((6, 2), False, screen),
                          Hand((6, 3), False, screen), Hand((6, 4), False, screen)],
                         [Hand((7, 0), False, screen), Hand((7, 1), False, screen),
                          Hand((7, 2), False, screen),
                          Hand((7, 3), False, screen), Hand((7, 4), False, screen)]]
        # self.main_rect = pygame.draw.rect(screen,(0,0,0),(64,64,w-128,h-128),0)
        self.level_data = []
        self.player.right = False
        self.player.left = False
        self.invsee = False
        # self.entity_gravity = True
        self.load_level()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player.sprite)
        for obj in self.level_data:
            if obj.image is not None:
                self.all_sprites.add(obj.sprite)

        self.screen_update()

    def screen_update(self):
        self.event = True
        check = pygame.event.Event(2, {'unicode': 'e', 'key': 101, 'mod': 0, 'scancode': 18})
        check_2 = pygame.event.Event(2, {'unicode': '0', 'key': 256, 'mod': 0, 'scancode': 82})

        while self.event:
            self.restart()
            self.player.regen_cnt += 1
            if self.player.regen_cnt > 25:
                if self.player.health < self.player.max_health:
                    self.player.health += self.player.regen
                else:
                    self.player.health = self.player.max_health
                self.player.regen_cnt = 0
            screen.fill((0, 0, 0))
            self.player.draw_player(screen)
            blocks_near = []
            for obj in self.level_data:
                if obj.now_pos[0] + obj.size[0] + 200 > 0 and obj.now_pos[0] - 200 < w:
                    if obj.sprite not in self.all_sprites and obj.sprite is not None:
                        self.all_sprites.add(obj.sprite)
                    if 'Entity' in obj.get_type() and obj.die is False:
                        obj.reload += 1
                        # print(obj.speed_down)
                        if obj.now_pos[0] - self.player.player.left <= -10:
                            obj.sprite.image = load_image('../textures\entities\Knight/knight_-1.png')
                            obj.now_pos[0] += obj.speed
                            obj.right = True
                            obj.left = False
                        elif obj.now_pos[0] + obj.size[0] - self.player.player.right >= 10:
                            obj.now_pos[0] -= obj.speed
                            obj.sprite.image = load_image(
                                '../textures\entities\Knight/knight_1.png')
                            obj.left = True
                            obj.right = False

                        for obj_ in self.level_data:
                            if 'Entity' not in obj_.get_type() and GetSide(ob1=obj_, ob2=obj,
                                                                           l=obj.left,
                                                                           r=obj.right).getting_side() != [
                                0, 0, 0, 0]:
                                val = self.entity_colliding(obj_, obj)
                                obj.stopped.append(val[2] == 1)

                        for obj_ in self.level_data:
                            if 'Entity' not in obj_.get_type() and ObjIsNear(ob1=obj_,
                                                                             ob2=obj).getting_side() != [
                                0, 0,
                                0,
                                0]:
                                val = self.entity_colliding(obj_, obj)
                                near_ch = ObjIsNear(ob1=obj_, ob2=obj).getting_side()
                                if True in obj.stopped and (near_ch[0] == 1 or near_ch[1] == 1):
                                    obj.speed_down = -16
                                    obj.stopped = []

                        if obj.gravity_n is True:
                            obj.gravity()

                        if obj.shell.colliderect(
                                self.player.player) and 'bad' in obj.get_type().lower() and obj.reload > 100:
                            self.player.health -= obj.power
                            obj.reload = 0
                    elif 'Entity' in obj.get_type() and obj.die:
                        self.all_sprites.remove(obj.sprite)
                    if not 'Entity' in obj.get_type():
                        val = self.colliding(obj, self.player)
                        blocks_near.append(val)
                elif not (obj.now_pos[0] + obj.size[0] + 200 > 0 and obj.now_pos[0] - 200 < w):
                    if obj.sprite in self.all_sprites and obj.sprite is not None:
                        self.all_sprites.remove(obj.sprite)
                obj.draw()
            if True in blocks_near:
                self.player.block_is_near = True
            else:
                self.player.block_is_near = False
            self.key_events()
            self.player.pos_x = self.player.player.left - self.level_data[-1].now_pos[0]
            self.player.pos_y = self.level_data[-1].now_pos[1] - self.player.player.top + 448

            clock.tick(67)  # 67 is optimal
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.event = False
                    quit(0)

                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.invsee:
                        self.inv.get_cell(pygame.mouse.get_pos(), screen)
                    elif not self.invsee:
                        for obj in self.level_data:
                            if obj.now_pos[0] + obj.size[0] + 200 > 0 and obj.now_pos[0] - 200 < w:
                                if 'Entity' in obj.get_type() and obj.die is False:
                                    val = ObjIsNear(ob1=obj, player=self.player).getting_side()
                                    if val != [0, 0, 0, 0]:
                                        obj.health -= self.player.player_power
                                        obj.draw()

                                if 'Entity' in obj.get_type() and obj.paid is False and obj.die is True:
                                    obj.health -= self.player.player_power
                                    obj.die = True
                                    obj.paid = True

                # print(e)
                if e == check or e == check_2:
                    self.invsee = not self.invsee

            self.all_sprites.draw(screen)

            if self.invsee:
                self.inv.render(screen)
                self.player.hand_obj_pos = list(self.inv.get_last_cell())
                self.player.hand_obj = self.inv_data[self.player.hand_obj_pos[0]][self.player.hand_obj_pos[1]]

                for i in range(len(self.inv_data)):
                    for j in range(len(self.inv_data[i])):
                        inv_obj = self.inv_data[i][j]
                        inv_obj.draw((inv_obj.place[0] * self.inv.cell_size + self.inv.left,
                                      inv_obj.place[1] * self.inv.cell_size + self.inv.top), screen)
                        if inv_obj.get_type() != 'Hand':
                            self.all_sprites.add(inv_obj.sprite)

            else:
                for i in range(len(self.inv_data)):
                    for j in range(len(self.inv_data[i])):
                        inv_obj = self.inv_data[i][j]
                        if inv_obj.get_type() != 'Hand':
                            self.all_sprites.remove(inv_obj.sprite)

            if self.player.pos_y < -1000:
                self.player.health -= 1

            # print(self.player.hand_obj)
            if self.player.hand_obj is not None and self.player.hand_obj.get_type() != 'Hand' and self.player.left:
                self.player.hand_obj.draw(
                    (self.player.player.left + 12, self.player.player.top + 32), screen)
                self.all_sprites.add(self.player.hand_obj.sprite)
                self.player.hand_obj.sprite.image = load_image(
                    '../textures/items/usual_sword_flip.png')
            elif self.player.hand_obj is not None and self.player.hand_obj.get_type() != 'Hand' and self.player.right:
                self.player.hand_obj.draw(
                    (self.player.player.left + 4, self.player.player.top + 32), screen)
                self.player.hand_obj.sprite.image = load_image('../textures/items/usual_sword.png')
                self.all_sprites.add(self.player.hand_obj.sprite)

            # Text rendering

            text_fps = font.render('FPS: ' + str(int(clock.get_fps())), 1, (255, 55, 100))
            text_fps_x = w - text_fps.get_width() - 10
            text_fps_y = 10
            screen.blit(text_fps, (text_fps_x, text_fps_y))

            text_xy = font.render(
                'X: ' + round_to(self.player.pos_x / 64, 3) + '   Y: ' +
                round_to(self.player.pos_y / 64, 3), 1,
                (255, 55, 100))
            text_xy_x = 10
            text_xy_y = 10
            screen.blit(text_xy, (text_xy_x, text_xy_y))

            text_money = self.player.money
            money = font.render('Money: ' + str(text_money), 1, (255, 55, 100))
            screen.blit(money, (360, 10))

            health = self.player.health = int(self.player.health)

            health_rend = font.render('Health: ' + str(health), 1, (255, 55, 100))
            screen.blit(health_rend, (360, 30))
            # print(self.player.block_is_near)
            pygame.display.flip()

    def restart(self):
        if self.player.health <= 0:
            return self.__init__()

    def load_level(self):
        file = open('../LEVELS/lvl_' + self.lvl + '.txt', 'r')
        level = file.read().split('\n')
        for block in level:
            block = block.split()
            if 'way:' in block[-2]:
                self.level_data.append(
                    obj_type[block[-1]](int(block[0]), int(block[1]), int(block[2]), screen,
                                        additionally=block[3],
                                        image=block[-2][4:]))
            else:
                self.level_data.append(
                    obj_type[block[-1]](int(block[0]), int(block[1]), int(block[2]), screen,
                                        additionally=block[3]))

    def colliding(self, ob1, pl):
        side = GetSide(ob1=ob1, player=pl, l=self.player.left, r=self.player.right)
        side = side.getting_side()
        check = None
        if side is not None:
            if side[2] == 1 and pl.in_air:
                pl.in_air = False
                pl.speed_down = 0
                pl.player.bottom = ob1.now_pos[1] - 0

            elif side[3] == 1 and pl.in_air:
                pl.speed_down = 0
                pl.player.top = ob1.now_pos[1] + ob1.size[1] + 0

            elif side[0] == 1:
                check = True
                pl.speed = 0
                pl.player.left = ob1.now_pos[0] + ob1.size[0] + 5

            elif side[1] == 1:
                check = True
                pl.speed = 0
                pl.player.right = ob1.now_pos[0] - 5

            if side[0] == 0 and side[1] == 0:
                check = False

        if ob1.shell.colliderect(pl.player):
            pl.player.bottom = ob1.shell.bottom - 2 * pl.player.size[1]
            # print('Произошля колизия')
            pass

        return check

    def entity_colliding(self, ob1, ob2):
        side = GetSide(ob1=ob1, ob2=ob2, l=ob2.left, r=ob2.right)
        side = side.getting_side()
        if side != [0, 0, 0, 0]:
            pass
            # print(side, ob1)
        if side is not None:
            if side[2] == 1:
                ob2.in_air = False
                ob2.gravity_n = False
                ob2.speed_down = 0
                ob2.now_pos[1] = ob1.now_pos[1] - ob2.size[1] - 1

            elif side[3] == 1:
                ob2.in_air = False
                ob2.speed_down = 0
                ob2.now_pos[1] = ob1.now_pos[1] + ob1.size[1] + 1

            elif side[0] == 1:
                ob2.now_pos[0] += ob2.speed
                ob2.speed = 0

            elif side[1] == 1:
                ob2.now_pos[0] -= ob2.speed
                ob2.speed = 0

            if side == [0, 0, 0, 0]:
                # ob2.stopped = False
                ob2.in_air = True
                ob2.gravity_n = True

            if side[0] == 0 or side[1] == 0:
                ob2.speed = ob2.standart_speed
        if side is None or side[2] == 0 or side[3] == 0:
            ob2.in_air = True
        if ob1.shell.colliderect(ob2.shell):
            # ob2.shell.bottom = ob1.shell.bottom + 50
            # print('Произошля колизия')
            pass
        return side

    def key_events(self):
        if self.player.player.top - 120 < 0 and self.player.in_air:
            if self.level_data[0].shell.top - self.player.player.top > 150 and self.player.speed_down < 0:
                self.player.player.top = self.player.player.top - self.player.speed_down
                for entity in self.level_data:
                    # entity.shell = entity.shell.move(-self.player.speed, -self.player.speed_down)
                    entity.now_pos[1] -= self.player.speed_down
        if self.player.player.bottom + 120 > h and self.player.speed_down > 0:
            # if self.level_data[0].shell.top - self.player.player.top > 150 and self.player.speed_down > 0:
            self.player.player.top = self.player.player.top - self.player.speed_down
            for entity in self.level_data:
                # entity.shell = entity.shell.move(-self.player.speed, -self.player.speed_down)
                entity.now_pos[1] -= self.player.speed_down

        if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            self.player.speed = -5
            self.player.left = True
            self.player.right = False
            if (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] or
                pygame.key.get_pressed()[pygame.K_w]) and self.player.in_air is False:
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20

            if pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[
                pygame.K_LCTRL] and self.player.block_is_near is False:
                self.player.speed = -20

            if self.player.player.left - 100 < 0:
                for entity in self.level_data:
                    entity.now_pos[0] -= self.player.speed
                self.player.speed = 0


        elif pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            self.player.speed = 5
            self.player.right = True
            self.player.left = False
            if (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] or
                pygame.key.get_pressed()[pygame.K_w]) and self.player.in_air is False:
                self.player.in_air = True
                self.player.stopped = False
                self.player.speed_down = -20

            if pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[
                pygame.K_LCTRL] and self.player.block_is_near is False:
                self.player.speed = 20

            if self.player.player.right + 300 > w:
                for entity in self.level_data:
                    entity.now_pos[0] -= self.player.speed
                self.player.speed = 0

        elif (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] or
              pygame.key.get_pressed()[pygame.K_w]) and self.player.in_air is False:
            self.player.in_air = True
            self.player.stopped = False
            self.player.speed_down = -20

        else:
            self.player.speed = 0