import pygame
from pygame.locals import *
import os
import game
import pygame.mixer as mixer
import constants
from PIL import Image
pygame.init()
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Game Resolution
screen_width=720
screen_height=720
screen=pygame.display.set_mode((screen_width, screen_height))
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(255, 230, 179)
yellow=(51, 102, 255)

# Game Fonts
font = "font/Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS=20
mixer.init()
mixer.set_num_channels(3)
mixer.Channel(2).play(mixer.Sound('music/intro.mp3'),loops=-1)

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
    return ret

background = []
background = split_animated_gif("images/tenor.gif")
for i in range(0,len(background)):
    background[i] = pygame.transform.scale(background[i], (constants.SIZE, constants.SIZE))

def main_menu():
    idx = 0
    menu=True
    selected="start"
    END = False
    TEXT = "SNAKE GAME"
    col = yellow
    while menu:
        # Main Menu UI
        screen.fill((225,225,225))
        screen.blit(background[idx], (0, 0))
        screen.blit(background[idx], (0, 0))
        title=text_format(TEXT, font, 90, col)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Snake")
        idx = (idx+1)%len(background)
        # start
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        mixer.stop()
                        game.start()
                        END = True
                    if selected=="quit":
                        pygame.quit()
                        quit()
        
        if END == True:
            mixer.Channel(2).play(mixer.Sound('music/intro.mp3'),loops=-1)
            TEXT = "GAME OVER"
            col = red
            END = False
main_menu()