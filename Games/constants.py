import pygame, sys
from pygame.locals import *
import time


SIZE = 720
BORDER = 60
FRAME = 600


block_size = 15
border_block = BORDER / block_size
snake_len = 4
move_direction = 'right'

speed = [1,0]
alpha = 0.05