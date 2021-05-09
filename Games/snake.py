import random
import pygame
from pygame.locals import *
import constants

def create_snake(snake_len):
    w_block = random.randrange(4, 40)
    h_block = random.randrange(4, 40)
    snake_array = []
    for i in range(w_block-snake_len,w_block):
        snake_array.append([i,h_block])
    return snake_array

def snake_count(snake_array):
    for snake in snake_array:
        snake[0] = snake[0] % 40
        snake[1] = snake[1] % 40
    return snake_array
def draw_snake(snake_array, DISPLAYSURF, color):
    for snake in snake_array:
        pygame.draw.rect(DISPLAYSURF,color,((constants.border_block+snake[0])*constants.block_size,(constants.border_block+snake[1])*constants.block_size,constants.block_size,constants.block_size),border_radius=5)

def move(snake_array, move_direction, length):
    if move_direction == 'up':
        snake_array.append([(snake_array[length-1][0]),(snake_array[length-1][1]-1)])
        snake_array.pop(0)
    if move_direction == 'left':
        snake_array.append([(snake_array[length-1][0]-1),(snake_array[length-1][1])])
        snake_array.pop(0)
    if move_direction == 'down':
        snake_array.append([(snake_array[length-1][0]),(snake_array[length-1][1]+1)])
        snake_array.pop(0)
    if move_direction == 'right':
        snake_array.append([(snake_array[length-1][0]+1),(snake_array[length-1][1])])
        snake_array.pop(0)
    return snake_array

def increase_snake(snake_array, move_direction, length):
    if move_direction == 'up':
        snake_array.append([(snake_array[length-1][0]),(snake_array[length-1][1]-1)])
    if move_direction == 'left':
        snake_array.append([(snake_array[length-1][0]-1),(snake_array[length-1][1])])
    if move_direction == 'down':
        snake_array.append([(snake_array[length-1][0]),(snake_array[length-1][1]+1)])
    if move_direction == 'right':
        snake_array.append([(snake_array[length-1][0]+1),(snake_array[length-1][1])])
    return snake_array