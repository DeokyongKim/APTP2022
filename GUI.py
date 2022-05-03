import pygame
import sys
import TABLE

color = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

alphabet = {pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd', pygame.K_e: 'e',
            pygame.K_f: 'f', pygame.K_g: 'g', pygame.K_h: 'h', pygame.K_i: 'i', pygame.K_j: 'j',
            pygame.K_k: 'k', pygame.K_l: 'l', pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o',
            pygame.K_p: 'p', pygame.K_q: 'q', pygame.K_r: 'r', pygame.K_s: 's', pygame.K_t: 't',
            pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x', pygame.K_y: 'y',
            pygame.K_z: 'z'}

number = {pygame.K_0: '0', pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3', pygame.K_4: '4',
          pygame.K_5: '5', pygame.K_6: '6', pygame.K_7: '7', pygame.K_8: '8', pygame.K_9: '9'}

command = {pygame.K_BACKSPACE: 'backspace', pygame.K_RETURN: 'return', pygame.K_SPACE: ' '}

direction = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'}

key_l = [alphabet, number, command, direction]


class Interaction(TABLE.Table):
    """
    Responsibility on Interaction with User
    """
    def __init__(self, input_events, table, table_size):
        super().__init__(table, table_size)
        self.input_events = input_events

    def MouseClick(self, mouse_position, table_position, table_length, table_border):
        for i in self.table_size[0]:
            for j in self.table_size[1]:
                adjust_position = (table_position[0] + j*table_length - j*table_border,
                                   table_position[1] + i*table_length - i*table_border)
                if 0 < mouse_position[0] - adjust_position[0] < table_length and \
                        0 < mouse_position[1] - adjust_position[1] < table_length:
                    self.table[i][j] = 1

    def KeyboardPressed(self):
        for single_event in self.input_events:
            self.IsEnd(single_event)
            if single_event.type() == pygame.KEYDOWN:
                for i in key_l:
                    if single_event.key in i:
                        return i[self.input_events]

    @staticmethod
    def IsEnd(end_event):
        if end_event == pygame.QUIT:
            sys.exit()


class Screen(TABLE.Table):
    """
    Responsibility on Displaying Screen
    """

    def __init__(self, screen_size: tuple[int, int], table: list[list[int]], table_size: tuple[int, int]):
        """
        Screen Information
        :param screen_size: tuple[int, int]
        :param table: list[list[int]]
        :param table_size: tuple[int, int]
        """
        super().__init__(table, table_size)
        pygame.init()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)

    def ShowText(self, word, text_size, font_color, text_position):
        """
        Function to Show Text on Screen
        :param word: str
        :param text_size: int
        :param font_color: str
        :param text_position: tuple[int, int]
        :return: none
        """
        font = pygame.font.SysFont("notosanscjkk", text_size)
        word = font.render(str(word), True, color[font_color])
        self.screen.blit(word, text_position)

    def ShowScreen(self, screen_color):
        """
        Function to Show Screen
        :param screen_color: str
        :return: none
        """
        self.screen.fill(color[screen_color])

    def ShowTable(self, cell_size, cell_color, cell_border, start_position):
        """
        Function to Show Table
        :param cell_size: int
        :param cell_color: str
        :param cell_border: int
        :param start_position: tuple[int, int]
        :return: none
        """
        for i in range(self.table_size[0]):
            for j in range(self.table_size[1]):
                adjust_position = (start_position[0] + j * cell_size - cell_border * j,
                                   start_position[1] + i * cell_size - cell_border * i)
                pygame.draw.rect(self.screen, color[cell_color],
                                 (adjust_position[0],
                                  adjust_position[1],
                                  cell_size,
                                  cell_size),
                                 cell_border)
                self.ShowText(self.table[i][j], cell_size, cell_color,
                              (adjust_position[0] + cell_size/3,
                               adjust_position[1] + cell_size/6))


class FinalScene(Interaction, Screen):
    pass


if __name__ == '__main__':
    t = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    a = Screen((1000, 1000), t, (4, 4))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        a.ShowScreen('white')
        a.ShowTable(150, 'black', 3, (100, 100))
        # a.ShowText("Hi There", 90, 'black', (20, 20))
        pygame.display.flip()
