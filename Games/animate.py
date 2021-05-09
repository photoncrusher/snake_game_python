import pygame
from pygame.locals import *
import constants
import time
from PIL import Image

def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame_image)
        print(1)
    return ret

pygame.init()
screen = pygame.display.set_mode((720, 720))
background = []
background = split_animated_gif("E:\\Working place\\PROJECT 20202\\Games\\images\\tenor.gif")
print(background)
for i in range(0,len(background)):
    background[i] = pygame.transform.scale(background[i], (constants.SIZE, constants.SIZE))
idx = 0

while 1:
    screen.fill((225,225,225))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    # screen.fill((0, 0, 0))
    screen.blit(background[idx], (0, 0))
    screen.blit(background[idx], (0, 0))
    idx = (idx+1)%len(background)
    # print(idx)
    pygame.display.update()
