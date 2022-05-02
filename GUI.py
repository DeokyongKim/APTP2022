from turtle import color

import pygame
import sys


class Color:
    color = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }


class Key:
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


class Screen:
    def __init__(self, size):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(size)

    def ShowText(self, word, size, color, position):
        """
        Function to show text on screen
        :param word: str
        :param size: int
        :param color: set
        :param position: set
        :return: none
        """
        font = pygame.font.SysFont("notosanscjkk", size)
        word = font.render(str(word), True, color)
        self.screen.blit(word, position)
        pygame.display.flip()

    def ShowScreen(self):
        self.screen.fill(Color.color['white'])


if __name__ == '__main__':
    a = Screen((300, 300))

    while True:
        a.ShowScreen()
        a.ShowText("Hi There", 90, Color.color['black'], (20, 20))
