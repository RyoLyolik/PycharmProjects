import pygame
pygame.init()
import random
import math
import sys
from player import Player
from blocks import *
from character_interaction import *
from entities import *
from inventory import *
from inventory_objects import *
from loading_image import load_image
import menu
from upgrade_item import *
import json

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

items = {
    'Usual_Sword': UsualSword,
    'Secret_Sword': SecretSword
}

def load_settings():
    player_settings = open('../settings/Player.json').read()
    data = json.loads(player_settings)
    # print(data)
    return data

clock = pygame.time.Clock()
# print(dir(pygame))
font = pygame.font.SysFont('comicsansms', 20)

walk_s = pygame.mixer.Sound('../audio/walk.ogg')
coins_s = pygame.mixer.Sound('../audio/gold.ogg')
walk_s.set_volume(0.05)

class Window:
    def __init__(self, lvl):
        global screen
        self.lvl = str(lvl)
        self.inv = Invent(8, 5)
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_icon(screen)
        pygame.display.set_caption('IndiGame')
        a = pygame.image.load('icon.png')
        pygame.display.set_icon(a)
        self.upg = Upgrade()
        self.player = Player(screen)

        # print(self.player.testing())
        print(self.player.money)
        self.inv_data = [[Hand((0, 0), True), Hand((0, 2), False),
                          Hand((0, 2), False),
                          Hand((0, 3), False), Hand((0, 4), False)],
                         [Hand((1, 0), False), Hand((1, 1), False),
                          Hand((1, 2), False),
                          Hand((1, 3), False), Hand((1, 4), False)],
                         [Hand((2, 0), False), Hand((2, 1), False),
                          Hand((2, 2), False),
                          Hand((2, 3), False), Hand((2, 4), False)],
                         [Hand((3, 0), False), Hand((3, 1), False),
                          Hand((3, 2), False),
                          Hand((3, 3), False), Hand((3, 4), False)],
                         [Hand((4, 0), False), Hand((4, 1), False),
                          Hand((4, 2), False),
                          Hand((4, 3), False), Hand((4, 4), False)],
                         [Hand((5, 0), False), Hand((5, 1), False),
                          Hand((5, 2), False),
                          Hand((5, 3), False), Hand((5, 4), False)],
                         [Hand((6, 0), False), Hand((6, 1), False),
                          Hand((6, 2), False),
                          Hand((6, 3), False), Hand((6, 4), False)],
                         [Hand((7, 0), False), Hand((7, 1), False),
                          Hand((7, 2), False),
                          Hand((7, 3), False), Hand((7, 4), False)]]

        settings = load_settings()

        self.player.money = settings['player']['money']
        self.player.power = settings['player']['power']
        self.player.upgrade_cost = settings['player']['upgrade_cost']
        self.player.max_health = settings['player']['max_health']
        self.player.health = self.player.max_health
        self.player.level = settings['player']['level']
        self.player.regen = settings['player']['regen']

        print(len(self.inv_data))
        for i in range(40):
            y = i // 8
            x = i % 8
            if settings['inventory'][str(i)]["type"] == 'Hand':
                self.inv_data[x][y] = Hand((x,y), True)
            else:
                print(self.inv_data)
                print(settings['inventory'][str(i)]['type'])
                print()
                print(settings['inventory'][str(i)])
                self.inv_data[x][y] = items[settings['inventory'][str(i)]['type']]((x,y),False,screen)
                self.inv_data[x][y].power = settings['inventory'][str(i)]['power']
                self.inv_data[x][y].upgrade_cost = settings['inventory'][str(i)]['upgrade_cost']
                self.inv_data[x][y].level = settings['inventory'][str(i)]['level']

        print(self.inv_data)

        # self.main_rect = pygame.draw.rect(screen,(0,0,0),(64,64,w-128,h-128),0)
        self.level_data = []
        self.player.right = False
        self.player.left = False
        self.invsee = False
        # self.entity_gravity = True
        self.load_level()

        self.all_sprites = pygame.sprite.Group()
        for obj in self.level_data:
            if obj.image is not None:
                self.all_sprites.add(obj.sprite)

        self.screen_update()

    def screen_update(self):
        self.event = True
        check = pygame.event.Event(2, {'unicode': 'e', 'key': 101, 'mod': 0, 'scancode': 18})
        check_2 = pygame.event.Event(2, {'unicode': '0', 'key': 256, 'mod': 0, 'scancode': 82})
        upgr_menu = pygame.event.Event(2, {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 33})

        while self.event:
            check_for_moving = self.player.pos_x
            check_for_collect = self.player.money
            self.player.pos_x = round(self.player.pos_x, 0)
            self.player.speed = round(self.player.speed, 1)
            if abs(self.player.speed) <= 0.1:
                self.player.speed = 0
            # print(self.player.pos_x, self.player.speed)
            mouse_rect = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
            if self.player.pos_x >= self.end:
                self.save_settings()
                menu.Menu()
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
                        # print(obj.health, self.player.power)
                        obj.reload += 1
                        # print(obj.speed_down)
                        if int(obj.now_pos[0] - self.player.player.left) < -32:
                            obj.sprite.image = obj.image_default
                            obj.now_pos[0] += obj.speed
                            obj.right = True
                            obj.left = False
                        elif int(obj.now_pos[0] - self.player.player.right) > 32 - obj.size[0]:
                            obj.now_pos[0] -= obj.speed
                            obj.sprite.image = obj.image_flip
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
                                0, 0, 0, 0]:
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
                        self.player.money += obj.cost
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
                    self.save_settings()
                    self.event = False
                    quit(0)
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.upg.check_for_updates(mouse_rect, self.player, screen)
                    if self.invsee:
                        self.upg.all_sprites.empty()
                        self.inv.get_cell(pygame.mouse.get_pos(), screen)
                    elif not self.invsee:
                        for obj in self.level_data:
                            if obj.now_pos[0] + obj.size[0] + 200 > 0 and obj.now_pos[
                                0] - 200 < w and not (
                                    self.upg.main_rect.colliderect(
                                        mouse_rect)) and 'Entity' in obj.get_type():
                                if obj.die is False:
                                    val = ObjIsNear(ob1=obj, player=self.player).getting_side()
                                    if val != [0, 0, 0, 0]:
                                        obj.health -= self.player.player_power
                                        obj.draw()

                                if obj.paid is False and obj.die is True:
                                    obj.health -= self.player.player_power
                                    obj.die = True
                                    obj.paid = True

                # print(e)
                if e == check or e == check_2:
                    self.invsee = not self.invsee

                if upgr_menu == e:
                    self.upg.all_sprites.empty()
                    self.upg.on_display = not self.upg.on_display

            self.all_sprites.draw(screen)

            if self.invsee:
                self.inv.render(screen)
                self.player.hand_obj_pos = list(self.inv.get_last_cell())
                self.player.hand_obj = self.inv_data[self.player.hand_obj_pos[0]][self.player.hand_obj_pos[1]]

                for i in range(len(self.inv_data)):
                    for j in range(len(self.inv_data[i])):
                        inv_obj = self.inv_data[i][j]
                        if inv_obj.get_type() != 'Hand':
                            inv_obj.draw((inv_obj.place[0] * self.inv.cell_size + self.inv.left,
                                          inv_obj.place[1] * self.inv.cell_size + self.inv.top), screen)
                        if inv_obj.get_type() != 'Hand' and not self.all_sprites.has(
                                inv_obj.sprite):
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
                if not self.all_sprites.has(self.player.hand_obj.sprite):
                    self.all_sprites.add(self.player.hand_obj.sprite)
                self.player.hand_obj.sprite.image = self.player.hand_obj.sprite.image_flip
            elif self.player.hand_obj is not None and self.player.hand_obj.get_type() != 'Hand' and self.player.right:
                self.player.hand_obj.draw(
                    (self.player.player.left + 4, self.player.player.top + 32), screen)
                self.player.hand_obj.sprite.image = self.player.hand_obj.sprite.image_default
                if not self.all_sprites.has(self.player.hand_obj.sprite):
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
            screen.blit(money, (20, 35))

            health = self.player.health = int(self.player.health)
            health_rend = font.render('Health: ' + str(health) + ' / ' + str(self.player.max_health), 1, (255, 55, 100))
            screen.blit(health_rend, (20, 60))

            power = font.render('Power: ' + str(self.player.player_power), 1, (255, 55, 100))
            screen.blit(power, (20, 85))
            self.upg.draw(screen, self.player)

            if check_for_moving != self.player.pos_x:
                walk_s.play(0)

            if check_for_collect != self.player.money:
                coins_s.play(0)

            pygame.display.flip()

    def save_settings(self):
        data = load_settings()
        data['player'] = {
            "money": self.player.money,
            "power": self.player.power,
            "upgrade_cost": self.player.upgrade_cost,
            "max_health": self.player.max_health,
            "level": self.player.level,
            "regen": self.player.regen
        }
        for i in range(40):
            y = i // 8
            x = i % 8
            if self.inv_data[x][y].get_type() != 'Hand':
                data['inventory'][str(i)] = {
                    "type": self.inv_data[x][y].get_type(),
                    "level": self.inv_data[x][y].level,
                    "power": self.inv_data[x][y].power,
                    "upgrade_cost": self.inv_data[x][y].upgrade_cost
                }

        settings = open('../settings/Player.json', mode='w')
        json.dump(data, settings)


    def restart(self):
        if self.player.health <= 0:
            self.save_settings()
            return self.__init__(self.lvl)

    def load_level(self):
        file = open('../LEVELS/lvl_' + self.lvl + '.txt', 'r')
        level = file.read().split('\n')
        self.end = int(level[0])
        for block in level[1:]:
            block = block.split()
            if 'way:' in block[-2]:
                self.level_data.append(
                    obj_type[block[-1]](int(block[0]), int(block[1]), int(block[2]), screen,
                                        additionally=block[3],
                                        image=block[-2][4:]))
            else:
                if 'entity' in block[4]:
                    self.level_data.append(
                        obj_type[block[4]](int(block[0]), int(block[1]), int(block[2]), screen,
                                            additionally=block[3], power=int(block[5]), health=int(block[6]), cost=int(block[7])))
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
                pl.player.top = ob1.now_pos[1] + ob1.size[1] + 1

            elif side[0] == 1:
                check = True
                pl.speed = 0
                pl.player.left = ob1.now_pos[0] + ob1.size[0] + 0

            elif side[1] == 1:
                check = True
                pl.speed = 0
                pl.player.right = ob1.now_pos[0] - 0

            if side[0] == 0 and side[1] == 0:
                check = False
        if ob1.shell.colliderect(pl.player):
            # pl.player.bottom = ob1.shell.bottom - 2 * pl.player.size[1]
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

    def key_events(self,e=None):

        if self.player.player.top - 120 < 0 and self.player.in_air:
            if self.level_data[0].shell.top - self.player.player.top > 150 and self.player.speed_down < 0:
                self.player.player.top = self.player.player.top - self.player.speed_down
                for entity in self.level_data:
                    entity.now_pos[1] -= self.player.speed_down
        if self.player.player.bottom + 120 > h and self.player.speed_down > 0:
            self.player.player.top = self.player.player.top - self.player.speed_down
            for entity in self.level_data:
                entity.now_pos[1] -= self.player.speed_down

        if self.player.player.right + 300 > w:
            for entity in self.level_data:
                entity.now_pos[0] = round(entity.now_pos[0]-self.player.speed,0)
            self.player.player.left -= self.player.speed

        if self.player.player.left - 100 < 0:
            for entity in self.level_data:
                entity.now_pos[0] = round(entity.now_pos[0] - self.player.speed, 0)
            self.player.player.left -= self.player.speed


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

            # if self.player.player.left - 100 < 0:
            #     for entity in self.level_data:
            #         entity.now_pos[0] -= self.player.speed
            #     self.player.player.left -= self.player.speed


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

            # if self.player.player.right + 300 > w:
            #     for entity in self.level_data:
            #         entity.now_pos[0] -= self.player.speed
            #     self.player.player.left -= self.player.speed

        elif (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] or
              pygame.key.get_pressed()[pygame.K_w]) and self.player.in_air is False:
            self.player.in_air = True
            self.player.stopped = False
            self.player.speed_down = -20

        else:
            # if self.player.player.right + 300 > w:
            #     for entity in self.level_data:
            #         entity.now_pos[0] -= self.player.speed
            #         entity.now_pos[0] -= entity.speed if 'Entity' in entity.get_type() else 0
            #     self.player.player.left -= self.player.speed
            # if self.player.player.left - 100 < 0:
            #     for entity in self.level_data:
            #         entity.now_pos[0] -= self.player.speed
            #         entity.now_pos[0] += entity.speed if 'Entity' in entity.get_type() else 0
            #     self.player.player.left -= self.player.speed
            # self.player.speed = round(self.player.speed * 0.9, 4)
            # if abs(self.player.speed) <= 10**-3:
            #     self.player.speed = 0
            if self.player.in_air:
                self.player.speed *= 0.9
            else:
                self.player.speed *= 0.5
if __name__ == '__main__':
    Window(0)