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
entity_type = {
    'usual': BlockUsual,
    'bad': BadBlock
}
clock = pygame.time.Clock()
print(dir(pygame))

class Window:
    def __init__(self):
        global screen
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption('IndiGame')
        self.player = Player(screen)
        # self.main_rect = pygame.draw.rect(screen,(0,0,0),(64,64,w-128,h-128),0)
        self.level_data = []
        self.right = False
        self.left = False
        self.load_level()
        pygame.init()

        self.screen_update()

    def screen_update(self):
        self.event = True
        while self.event:
            clock.tick(67) # 67 is optimal
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.event = False
            screen.fill((0, 0, 0))

            self.player.draw_player(screen)
            for obj in self.level_data:
                obj.draw()
                self.colliding(obj, self.player)

            self.key_events()
            self.player.pos_x += self.player.speed
            font = pygame.font.Font(None, 25)
            text = font.render('X: ' + str(self.player.pos_x), 1, (255, 55, 100))
            text_x = w - text.get_width() - 10
            text_y = 10
            screen.blit(text, (text_x, text_y))

            pygame.display.flip()

    def restart(self, collusion_obj):
        if collusion_obj.get_type() == 'Bad':
            self.event = False
            return self.__init__()

    def load_level(self):
        file = open('LEVELS/lvl_0.txt', 'r')
        level = file.read().split('\n')
        for block in level:
            block = block.split()
            self.level_data.append(entity_type[block[-1]](int(block[0]), int(block[1]), int(block[2]), screen))

    def colliding(self, ob1, pl):
        side = GetSide(ob1=ob1, player=pl, l=self.left, r=self.right)
        side = side.getting_side()

        if side is not None:
            if side[2] == 1 and pl.in_air:
                self.restart(ob1)
                pl.in_air = False
                pl.speed_down = 0
                pl.player.bottom = ob1.shell.top - 1

            elif side[3] == 1 and pl.in_air:
                self.restart(ob1)
                pl.speed_down = 0
                pl.player.top = ob1.shell.bottom + 1

            elif side[0] == 1:
                self.restart(ob1)
                pl.pos_x -= pl.speed
                pl.speed = 0
                pl.player.left = ob1.shell.right + 1

            elif side[1] == 1:
                self.restart(ob1)
                pl.pos_x -= pl.speed
                pl.speed = 0
                pl.player.right = ob1.shell.left - 1

        if ob1.shell.colliderect(pl.player):
            pl.player.bottom = ob1.shell.bottom - 2*pl.player.size[1]
            # print('Произошля колизия')
            pass


    def key_events(self):
        if self.player.player.top - 120 < 0 and self.player.in_air:
            if self.level_data[0].shell.top - self.player.player.top > 150 and self.player.speed_down < 0:
                self.player.player.top = self.player.player.top - self.player.speed_down
                for entity in self.level_data:
                    # entity.shell = entity.shell.move(-self.player.speed, -self.player.speed_down)
                    entity.shell = entity.shell.move(0, -self.player.speed_down)
                    entity.now_pos[1] -= self.player.speed_down
        if self.player.player.bottom + 120 > h and self.player.speed_down > 0:
            # if self.level_data[0].shell.top - self.player.player.top > 150 and self.player.speed_down > 0:
            self.player.player.top = self.player.player.top - self.player.speed_down
            for entity in self.level_data:
                # entity.shell = entity.shell.move(-self.player.speed, -self.player.speed_down)
                entity.shell = entity.shell.move(0, -self.player.speed_down)
                entity.now_pos[1] -= self.player.speed_down

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

            if self.player.player.left - 100 < 0:
                for entity in self.level_data:
                    entity.shell = entity.shell.move(-self.player.speed, 0)
                    entity.now_pos[0] -= self.player.speed
                self.player.pos_x += self.player.speed
                self.player.speed = 0


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

            if self.player.player.right + 300 > w:
                for entity in self.level_data:
                    entity.shell = entity.shell.move(-self.player.speed, 0)
                    entity.now_pos[0] -= self.player.speed
                self.player.pos_x += self.player.speed
                self.player.speed = 0

        elif pygame.key.get_pressed()[pygame.K_SPACE] and self.player.in_air is False: # TODO
            self.player.in_air = True
            self.player.stopped = False
            self.player.speed_down = -20

        else:
            self.player.speed = 0

if __name__ == '__main__':
    win = Window()
    pygame.quit()