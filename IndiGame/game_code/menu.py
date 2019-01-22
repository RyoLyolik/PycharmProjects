import pygame
import os
import main_win

screen = None
size = w, h, = 720, 480
pygame.init()
font = pygame.font.Font('11939.ttf', 50)


class Menu:
    def __init__(self):
        global screen
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.levels_button = LevelsButton()
        self.mouse = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
        self.levels = LevelsRender()
        self.screen_update()

    def screen_update(self):
        self.event = True
        level = None

        while self.event:
            if level is not None:
                self.event = False
                run = main_win.Window(level)
            screen.fill((0, 0, 0))
            self.mouse = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.event = False
                    quit(0)

                if e.type == pygame.MOUSEBUTTONDOWN:
                    level = self.levels.get_lvl(pygame.mouse.get_pos())
                    if self.levels_button.button.colliderect(
                            self.mouse) and self.levels_button.show:
                        self.levels_button.show = False
                        self.levels.show = True
                        print('Pushed')

            self.levels_button.draw()
            self.levels.draw()
            pygame.display.flip()


class LevelsButton:
    def __init__(self):
        self.show = True
        self.w, self.h = 210, 75
        self.x, self.y = 360 - self.w//2, 240 - self.h//2

    def draw(self):
        if self.show:
            self.button = pygame.draw.rect(screen, (255, 255, 255),
                                           (self.x, self.y, self.w, self.h), 5)
            levels = font.render('Levels', 1, (255, 255, 255), 5)
            levels_x = (w / 2) - levels.get_width()//2
            levels_y = (h / 2) - levels.get_height()//2
            screen.blit(levels, (levels_x, levels_y))


class LevelsRender:
    def __init__(self):
        self.show = False
        self.lvls = os.listdir('../LEVELS')
        self.size = 75
        self.left, self.top = 67, 40
        self.max = 7

        self.lvls_grid = []
        for lvl in range(len(self.lvls)):
            if 'lvl' and '.txt' in self.lvls[lvl]:
                if lvl % self.max == 0:
                    self.lvls_grid.append([])

                self.lvls_grid[lvl // self.max].append(self.lvls[lvl])
        print(self.lvls_grid)

    def draw(self):
        if self.show == True:
            for i in range(len(self.lvls_grid)):
                for j in range(len(self.lvls_grid[i])):
                    pygame.draw.rect(screen, (255, 255, 255), (
                        j * (self.size + 10) + self.left, i * (self.size + 10) + self.top,
                        self.size,
                        self.size), 0)
                    pygame.draw.rect(screen, (0, 0, 0), (
                        j * (self.size + 10) + 3 + self.left, i * (self.size + 10) + 3 + self.top,
                        self.size - 6, self.size - 6), 0)
                    level = font.render(str(i * self.max + j + 1), 1, (255, 255, 255))
                    level_x = j * (
                            self.size + 10) + self.left + self.size // 2 - level.get_width() // 2
                    level_y = i * (self.size + 10) + self.top
                    screen.blit(level, (level_x, level_y))

    def get_lvl(self, pos):
        if self.show:
            for i in range(len(self.lvls_grid)):
                for j in range(len(self.lvls_grid[i])):
                    if j * (self.size + 10) + self.left < pos[0] < j * (
                            self.size + 10) + self.left + self.size and i * (
                            self.size + 10) + self.top < pos[1] < i * (
                            self.size + 10) + self.top + self.size:
                        return i * self.max + j
        return None


if __name__ == '__main__':
    win = Menu()
    pygame.quit()
