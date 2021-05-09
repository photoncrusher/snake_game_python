import snake
import random

def remove_ball(ball):
    ball = []
    return ball

def check_ball_exist(ball):
    if ball != []:
        return True
    else: return False

def create_ball(snake_array,ball):
    ball = [random.randrange(4, 40),random.randrange(4, 40)]
    while(snake_array.count(ball)!=0):
        ball = [random.randrange(4, 40),random.randrange(4, 40)]
    balls = []
    balls.append(ball)
    return balls