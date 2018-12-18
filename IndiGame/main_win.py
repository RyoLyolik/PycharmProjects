# TRAINING


import pygame
import random
import math
screen = None
class Window:
    def __init__(self):
        global screen

        size = w, h = 720, 480
        screen = pygame.display.set_mode(size)
        self.player = Player()
        pygame.init()

        self.screen_update()

    def screen_update(self):
        while pygame.event.wait().type != pygame.QUIT:
            self.key_events()
            self.player.draw_player()
            pygame.display.flip()
            screen.fill((0,0,0))

    def key_events(self):
        # print(pygame.key.get_pressed())
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move(self.player.player, [-self.player.speed,0])

        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move(self.player.player, [self.player.speed,0])

        elif pygame.key.get_pressed()[pygame.K_UP]:
            self.move(self.player.player, [0,-self.player.speed])

        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.move(self.player.player, [0,self.player.speed])

    def move(self, ob, speed):
        # ob = ob.move(speed) # DONT WORK, WHY ??
        self.player.player = self.player.player.move(speed)
        print(self.player.player.left)
class Player:
    def __init__(self):
        global screen

        self.player_size = 64
        self.speed = 2
        self.pos_x = 190
        self.pos_y = 60
        self.player = pygame.draw.rect(screen, (200, 100, 150), (190, 60, self.player_size, self.player_size), 0)
        self.draw_player()


    def draw_player(self):
        self.player = pygame.draw.rect(screen, (200, 100, 150), (self.player.left, self.player.top, self.player_size, self.player_size), 0)





if __name__ == '__main__':
    win = Window()