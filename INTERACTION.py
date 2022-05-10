from GUI import Screen, pygame, sys
# import pygame
# import sys


class Interaction(Screen):
    """
    Responsibility on Interaction with User
    """
    def __init__(self, screen_size, table, table_size, cell_size, cell_border):
        super().__init__(screen_size, table, table_size, cell_size, cell_border)

    def MouseClick(self, table_position):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        for i in self.table_size[0]:
            for j in self.table_size[1]:
                adjust_position = (table_position[0] + j*self.cell_size - j*self.cell_border,
                                   table_position[1] + i*self.cell_size - i*self.cell_border)
                if 0 < mouseX - adjust_position[0] < self.cell_size and \
                        0 < mouseY - adjust_position[1] < self.cell_size:
                    self.table[i][j] = 1

    def GetDecisionPage(self, start_position):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        for i in range(5):
            adjust_position = (start_position[0] + i * self.cell_size - self.cell_border * i - 5*self.cell_size/2,
                               start_position[1] - self.cell_size)
            if 0 < mouseX - adjust_position[0] < self.cell_size and 0 < mouseY - adjust_position[1] < self.cell_size:
                return i
        return -1

    def IsEvent(self, mode, start_position):
        while True:
            for input_event in pygame.event.get():
                if mode == 'number':
                    if input_event.type == pygame.MOUSEBUTTONDOWN:
                        return 'number', self.GetDecisionPage(start_position)
                elif mode == 'table':
                    if input_event.type == pygame.MOUSEBUTTONDOWN:
                        self.MouseClick(start_position)


if __name__ == '__main__':
    t = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    a = Interaction((1000, 1000), t, (4, 4), 150, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        a.ShowScreen('white')
        a.ShowDecisionPage('black', (a.screen_size[0] / 2, a.screen_size[1]/2))
        decision = a.IsEvent('number', (a.screen_size[0] / 2, a.screen_size[1]/2))
        print(decision)
        # a.ShowTable(150, 'black', 3, (100, 100))
        # a.ShowText("Hi There", 90, 'black', (20, 20))
        pygame.display.flip()
