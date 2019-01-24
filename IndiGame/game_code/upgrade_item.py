import pygame
from loading_image import load_image
font = pygame.font.Font('seriffr.fon', 50)

class Upgrade:
    def __init__(self):
        self.on_display = False
        self.all_sprites = pygame.sprite.Group()

    def draw(self, screen, player):
        self.obj = player.hand_obj if player.hand_obj.get_type() != 'Hand' else player
        if self.on_display:

            pygame.draw.rect(screen, (75,50,26), (20,50, 250,100), 0)
            pygame.draw.rect(screen, (140, 75, 39), (30, 60, 50, 50), 0)

            obj_charact = font.render('Power: '+str(self.obj.power), 1, (255, 255, 255), 5)
            screen.blit(obj_charact, (85, 50))

            self.upgrade_rect_border = pygame.draw.rect(screen, (140, 75, 39), (90, 75, 150, 30), 0)
            upgrade_rect = pygame.draw.rect(screen, (120, 60, 30), (92, 77, 146, 26), 0)

            upg_cost = font.render('Upgrade: '+str(self.obj.upgrade_cost), 1, (255, 255, 255), 5)
            screen.blit(upg_cost, (95, 80))

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = load_image(self.obj.image)
            self.sprite.rect = self.sprite.image.get_rect()
            self.sprite.rect = (31, 61, 48, 48)
            self.all_sprites.add(self.sprite)
            self.all_sprites.draw(screen)

    def check_for_upgrade(self,mouse_rect):
        if self.on_display and self.upgrade_rect_border.colliderect(mouse_rect):
            self.obj.power = int(round(((self.obj.power+1)*1.1),0))
            self.obj.upgrade_cost = int(round(((self.obj.upgrade_cost+1)*1.1),0))
