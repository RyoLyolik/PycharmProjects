import pygame
from loading_image import load_image
from inventory_objects import Hand
import gc

size = w, h, = 720, 480

walk_s = pygame.mixer.Sound('../audio/walk.ogg')
coins_s = pygame.mixer.Sound('../audio/gold.ogg')
walk_s.set_volume(0.1)
# speed_particles = [load_image('../textures/particles/speed/speed_'+str(i)+'.png') for i in range(1)]
# for i in range(1):
#     print(i)


class Player:
    def __init__(self, screen):
        self.all_sprites = pygame.sprite.Group()

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image('../textures/entities/Player/player_1.png')
        self.image = '../textures/items/hand.png'
        self.sprite.rect = self.sprite.image.get_rect()
        self.level = 1

        self.block_is_near = False

        self.player_size = [64,64]
        self.speed = 5
        self.pos_x = 128
        self.pos_y = 60


        self.double_jump = 2
        self.in_air = True
        self.stopped = False
        self.up = False

        self.gravity_force = 1
        self.speed_down = 0
        self.right = True
        self.left = False

        self.money = 0
        self.sprite.rect.left = 128
        self.player = self.sprite.rect
        self.hand_obj_pos = [0, 0]
        self.hand_obj = Hand((0,0), True)
        self.player_power = self.hand_obj.power if self.hand_obj is not None else 1
        self.max_health = 100
        self.health = self.max_health

        self.image_default = load_image('../textures/entities/Player/player_1.png')
        self.image_flip = load_image('../textures/entities/Player/player_-1.png')

        self.regen_cnt = 0
        self.regen = 1
        self.move([0, 100])

        self.power = 1
        self.upgrade_cost = 25
        self.all_sprites.add(self.sprite)


    def draw_player(self, screen):
        if self.health <= 0:
            self.all_sprites.empty()
        elif self.health > self.max_health:
            self.health = self.max_health
        if self.right:
            self.sprite.image = self.image_default
        else:
            self.sprite.image = self.image_flip
        self.sprite.rect = self.player
        self.move([self.speed, self.speed_down])
        self.gravity()
        self.actions()
        self.all_sprites.draw(screen)

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
        self.player_power = self.hand_obj.power + self.power

    def get_type(self):
        return 'Just_a_fist'
