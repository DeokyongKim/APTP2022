import pygame
import random
from enum import Enum
from collections import namedtuple

# Moving Direction
class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# Coordination of point
Cord = namedtuple('Cord', ['x', 'y'])

# Constants
oneBlockSize = 20
headSpeed = 20
class snakeGame:
    def __init__(self, w=960, h=960):
        self.width = w
        self.height = h
        self.display = pygame.display.set_mode((self.width, self.height))

        self.dir = Dir.RIGHT

        self.head = Cord((self.width)/2, (self.height)/2)
        self.snake =
        self.item = Cord(0,0)
        self.tail = 0

    def _locateFood(self):
        x = random.randint(0, (self.width - oneBlockSize) // oneBlockSize) * oneBlockSize
        y = random.randint(0, (self.height - oneBlockSize) // oneBlockSize) * oneBlockSize
        self.item = Cord(x, y)
        if self.item
