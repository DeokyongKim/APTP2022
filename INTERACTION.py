from GUI import Screen, pygame, sys, color


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
                adjust_position = (table_position[0] + j * self.cell_size - j * self.cell_border,
                                   table_position[1] + i * self.cell_size - i * self.cell_border)
                if 0 < mouseX - adjust_position[0] < self.cell_size and \
                        0 < mouseY - adjust_position[1] < self.cell_size:
                    self.table[i][j] = 1

    def GetDecision(self, start_position):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        for i in range(1, 5):
            adjust_position = (start_position[0] + i * self.cell_size - self.cell_border * i - 6 * self.cell_size / 2,
                               start_position[1] - self.cell_size)
            if 0 < mouseX - adjust_position[0] < self.cell_size and 0 < mouseY - adjust_position[1] < self.cell_size:
                return i + 1
        return -1

    def GetInput(self, start_position):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        for i in range(self.table_size[0]):
            for j in range(self.table_size[1]):
                adjust_position = (start_position[0] + j * self.cell_size - self.cell_border * j,
                                   start_position[1] + i * self.cell_size - self.cell_border * i + self.cell_size/2)
                if 0 < mouseX - adjust_position[0] < self.cell_size and 0 < mouseY - adjust_position[1] < self.cell_size:
                    if self.table[i][j] == 1:
                        self.table[i][j] = 0
                    elif self.table[i][j] == 0:
                        self.table[i][j] = 1

    def IsEvent(self, mode, start_position, event_list):
        # print('get event')
        for input_event in event_list:
            if input_event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'number':
                    return self.GetDecision(start_position)
                if mode == 'table':
                    self.GetInput(start_position)
                #     return self.MouseClick(start_position)

    def BackButton(self, sc_type):
        # print('show back button')
        pygame.draw.rect(self.screen, color['black'],
                         (30,
                          30,
                          self.cell_size / 2,
                          self.cell_size / 2),
                         self.cell_border)
        pygame.draw.polygon(self.screen, color['black'],
                            ((30 + 10, 30 + self.cell_size / 4),
                             (30 + self.cell_size / 2 - 10, 30 + 10),
                             (30 + self.cell_size / 2 - 10, 30 + self.cell_size / 2 - 10)
                             ))


if __name__ == '__main__':
    t = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    a = Interaction((800, 800), t, (4, 4), 130, 3)
    screen_type = 'decide'

    while True:
        el = pygame.event.get()

        for end_event in el:
            if end_event.type == pygame.QUIT:
                print('program ended')
                sys.exit()
        a.ShowScreen('white')

        if screen_type == 'decide':
            a.ShowDecisionPage('black', (a.screen_size[0] / 2, a.screen_size[1] / 2))
            decision = a.IsEvent('number', (a.screen_size[0] / 2, a.screen_size[1] / 2), el)
            if decision is not None:
                print(decision)
                if decision != -1:
                    if decision == 2:
                        a.table = [
                            [0, 0],
                            [0, 0]
                        ]
                        a.table_size = (2, 2)
                    if decision == 3:
                        a.table = [
                            [0, 0],
                            [0, 0],
                            [0, 0],
                            [0, 0]
                        ]
                        a.table_size = (4, 2)
                    if decision == 4:
                        a.table = [
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]
                        ]
                        a.table_size = (4, 4)
                    if decision == 5:
                        a.table = [
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]
                        ]
                        a.table_size = (4, 4)
                    screen_type = 'done'
        elif screen_type == 'done':
            a.BackButton(screen_type)
            stp = (a.screen_size[0] / 2 - a.table_size[1] * a.cell_size / 2.0,
                   a.screen_size[1] / 2 - a.table_size[0] * a.cell_size / 2.0 - a.cell_size / 2)

            for back_event in el:
                if back_event.type == pygame.MOUSEBUTTONDOWN:
                    (mx, my) = pygame.mouse.get_pos()
                    if 30 < mx < 30 + 150 / 2 and 30 < my < 30 + 150 / 2:
                        print('in')
                        screen_type = 'decide'
                        decision = None

            a.IsEvent('table', stp, el)
            a.ShowTable('black')

        pygame.display.flip()
