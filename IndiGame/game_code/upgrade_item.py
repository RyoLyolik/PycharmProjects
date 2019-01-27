import pygame
from loading_image import load_image
font = pygame.font.Font('seriffr.fon', 50)
small_font = pygame.font.Font('serifer.fon', 50)
class Upgrade:
    def __init__(self):
        self.on_display = False
        self.all_sprites = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.show_description = False
        self.main_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, screen, player):
        self.obj = player.hand_obj if player.hand_obj.get_type() != 'Hand' else player
        mouse_rect = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
        self.main_rect = pygame.Rect(0, 0, 0, 0)
        if self.on_display:
            self.main_rect = pygame.draw.rect(screen, (75,50,26), (475,46, 250, 79), 0)
            pygame.draw.rect(screen, (95, 53, 29), (479, 50, 242, 71), 0)


            self.beauty = pygame.draw.rect(screen, (115, 63, 34), (481, 60, 58, 50), 0)
            self.beauty_2 = pygame.draw.rect(screen, (115, 63, 34), (485, 56, 50, 58), 0)
            # pygame.draw.circle(screen, (115, 63, 34), (30, 60), 4)
            # pygame.draw.circle(screen, (115, 63, 34), (80, 60), 4)
            # pygame.draw.circle(screen, (115, 63, 34), (30, 110), 4)
            # pygame.draw.circle(screen, (115, 63, 34), (80, 110), 4)

            obj_charact = font.render('Power: '+str(self.obj.power), 1, (255, 255, 255), 5)
            screen.blit(obj_charact, (550, 50))

            obj_level = small_font.render('Lvl:' + str(self.obj.level), 1,(255,255,255), 5)
            screen.blit(obj_level, (550,70))

            self.upgrade_rect_border = pygame.draw.rect(screen, (133, 68, 37), (545, 90, 150, 30), 0)
            self.upgrade_rect = pygame.draw.rect(screen, (118, 61, 33), (547, 92, 146, 26), 0)

            upg_cost = font.render('Upgrade: '+str(self.obj.upgrade_cost) + '$', 1, (255, 255, 255), 5)
            screen.blit(upg_cost, (550, 95))

            if not self.all_sprites.has(self.sprite):
                self.sprite.image = load_image(self.obj.image)
                self.sprite.rect = self.sprite.image.get_rect()
                self.sprite.rect = (486, 61, 48, 48)
                self.all_sprites.add(self.sprite)
            self.all_sprites.draw(screen)

            if self.show_description and (self.beauty.colliderect(mouse_rect) or self.beauty_2.colliderect(mouse_rect)):
                x,y = pygame.mouse.get_pos()
                pygame.draw.rect(screen, (115, 63, 34), (x-50,y+50, 136,32), 0)
                pygame.draw.rect(screen, (115, 63, 34), (x-46, y+46, 128, 40), 0)
                pygame.draw.circle(screen, (115, 63, 34), (x-46, y+50), 4)
                pygame.draw.circle(screen, (115, 63, 34), (x + 82, y + 50), 4)
                pygame.draw.circle(screen, (115, 63, 34), (x-46, y+50+32), 4)
                pygame.draw.circle(screen, (115, 63, 34), (x + 82, y + 50+32), 4)

                pygame.draw.rect(screen, (75, 50, 26), (x-46, y+50, 128, 32), 0)

                descript = font.render(' '.join(self.obj.get_type().split('_')), 1, (255, 255, 255), 5)
                screen.blit(descript, (x-15,y+55))

        else:
            self.main_rect = pygame.Rect(0,0,0,0)

    def check_for_updates(self, mouse_rect, player, screen):
        if self.on_display and self.upgrade_rect_border.colliderect(mouse_rect) and player.money >= self.obj.upgrade_cost:
            player.money -= self.obj.upgrade_cost

            if self.obj == player:
                player.max_health = int(round(((player.max_health)*1.04),0))
                player.regen = round(player.regen * 1.04, 5)
                self.obj.power = int(round(((self.obj.power + 1) * 1.03), 0))
                self.obj.upgrade_cost = int(round(((self.obj.upgrade_cost) * 1.06), 0))

            else:
                self.obj.power = int(round(((self.obj.power + 1) * 1.06), 0))
                self.obj.upgrade_cost = int(round(((self.obj.upgrade_cost) * 1.06), 0))

            self.obj.level += 1


        elif self.on_display and (self.beauty.colliderect(mouse_rect) or self.beauty_2.colliderect(mouse_rect)):
            self.show_description = not self.show_description


