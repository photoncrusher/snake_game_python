import pygame, sys
from pygame.locals import *
import pygame.mixer as mixer
import time
import os
import balls
import constants
import snake
import random

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))
def start():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((constants.SIZE, constants.SIZE))
    pygame.display.set_caption('Snake')
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    clock = pygame.time.Clock()
    FPS = 15
    background = pygame.image.load("images/khung.jpg")
    background.convert()
    background = pygame.transform.scale(background, (constants.SIZE, constants.SIZE))
    mixer.init()
    mixer.set_num_channels(3)
    mixer.Channel(1).play(mixer.Sound('music/in-game.mp3'),loops=-1)
    snake_array = snake.create_snake(constants.snake_len)
    move_direction = constants.move_direction
    length = constants.snake_len
    ball = []
    prev_color = random_color()
    END_GAME = False
    while not END_GAME:
        if not balls.check_ball_exist(ball):
            color = random_color()
            ball = balls.create_ball(snake_array, ball)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and move_direction != 'down':
                    move_direction = 'up'
                if event.key == pygame.K_a and move_direction != 'right':
                    move_direction = 'left'
                if event.key == pygame.K_s and move_direction != 'up':
                    move_direction = 'down'
                if event.key == pygame.K_d and move_direction != 'left':
                    move_direction = 'right'
        DISPLAYSURF.fill((0, 0, 0))
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(background, (0, 0))
        
        snake_array = snake.move(snake_array,move_direction,length)
        snake_array = snake.snake_count(snake_array)
        if snake_array[length-1]==ball[0]:
            mixer.Channel(0).play(mixer.Sound('music/eat.mp3'))
            prev_color = color
            color = random_color()
            snake_array = snake.increase_snake(snake_array,move_direction,length)
            ball = balls.remove_ball(ball)
            ball = balls.create_ball(snake_array,ball)
            snake.draw_snake(ball,DISPLAYSURF,color)
            length = length + 1
            FPS = FPS + 1
        else:
            snake.draw_snake(ball,DISPLAYSURF,color)
        snake.draw_snake(snake_array,DISPLAYSURF,prev_color)
        if(snake_array.count(snake_array[0])==2):
            END_GAME = True
            mixer.Channel(1).stop()
        pygame.display.update()
        clock.tick(FPS)

