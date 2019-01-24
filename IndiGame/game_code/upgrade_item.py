import pygame
from loading_image import load_image
font = pygame.font.Font('seriffr.fon', 50)
small_font = pygame.font.Font('serifer.fon', 50)
class Upgrade:
    def __init__(self):
        self.on_display = False
        self.all_sprites = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()

    def draw(self, screen, player):
        self.obj = player.hand_obj if player.hand_obj.get_type() != 'Hand' else player
        if self.on_display:

            pygame.draw.rect(screen, (75,50,26), (20,48, 250, 75), 0)
            pygame.draw.rect(screen, (140, 75, 39), (30, 60, 50, 50), 0)

            obj_charact = font.render('Power: '+str(self.obj.power), 1, (255, 255, 255), 5)
            screen.blit(obj_charact, (95, 50))

            obj_level = small_font.render('Lvl:' + str(self.obj.level), 1,(255,255,255), 5)
            screen.blit(obj_level, (95,70))

            self.upgrade_rect_border = pygame.draw.rect(screen, (140, 75, 39), (90, 90, 150, 30), 0)
            upgrade_rect = pygame.draw.rect(screen, (120, 60, 30), (92, 92, 146, 26), 0)

            upg_cost = font.render('Upgrade: '+str(self.obj.upgrade_cost) + '$', 1, (255, 255, 255), 5)
            screen.blit(upg_cost, (95, 95))

            if not self.all_sprites.has(self.sprite):
                self.sprite.image = load_image(self.obj.image)
                self.sprite.rect = self.sprite.image.get_rect()
                self.sprite.rect = (31, 61, 48, 48)
                self.all_sprites.add(self.sprite)
            self.all_sprites.draw(screen)
        else:
            self.upgrade_rect_border = pygame.Rect(0,0,0,0)

    def check_for_upgrade(self,mouse_rect):
        if self.on_display and self.upgrade_rect_border.colliderect(mouse_rect):
            self.obj.power = int(round(((self.obj.power+1)*1.1),0))
            self.obj.upgrade_cost = int(round(((self.obj.upgrade_cost+1)*1.1),0))
            self.obj.level += 1
