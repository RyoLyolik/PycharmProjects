import pygame

class Invent:
    colors = {
        1: (118,81,77),
        -1: (200,100,100)
    }

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = [[-1] * w for _ in range(h)]
        self.cell_size = 50
        self.left = w*self.cell_size*0.4
        self.top = h*self.cell_size*0.5
        self.last_cell = (0,0)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (self.colors[self.board[j][i]]), (
                    self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)

                pygame.draw.rect(screen, (self.colors[self.board[j][i]]), (
                    (self.left + i * self.cell_size) + 1, (self.top + j * self.cell_size) + 1, self.cell_size - 2,
                    self.cell_size - 2), 1)

    def get_cell(self, pos, screen):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.left + column * self.cell_size < pos[0] and self.left + column * self.cell_size + self.cell_size > \
                        pos[0] and self.top + row * self.cell_size < pos[
                    1] and self.top + row * self.cell_size + self.cell_size > pos[1]:
                    self.last_cell = (column, row)
                    return self.on_click((self.left+column*self.cell_size, self.top+row*self.cell_size), screen, row,column)

    def on_click(self, coords, screen, row, column):
        for i in range(self.width):
            for j in range(self.height):
                if i == column and j == row:
                    self.board[row][column] = -1
                    pygame.draw.rect(screen, self.colors[1],
                                     (*coords, self.cell_size, self.cell_size), 0)
                    pygame.draw.rect(screen, self.colors[-1],
                                     (coords[0] + 1, coords[1] + 1, self.cell_size - 2, self.cell_size - 2), 0)
                elif i != column or j != row:
                    self.board[j][i] = 1
                    pygame.draw.rect(screen, (self.colors[-1]), (
                        self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)

                    pygame.draw.rect(screen, (self.colors[-1]), (
                        (self.left + i * self.cell_size) + 1, (self.top + j * self.cell_size) + 1, self.cell_size - 2,
                        self.cell_size - 2), 1)
    def get_last_cell(self):
        return self.last_cell