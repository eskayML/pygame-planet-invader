import pygame
from pygame.locals import *


pygame.init()
pygame.display.set_caption('Pygame For 2d Games')
screen = pygame.display.set_mode((600, 500))


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)



weapon = 'assets/gun.png'
planet = 'assets/earth.png'

running = True
background = BLACK
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            running = False
        

    screen.fill(background)
    pygame.display.update()


pygame.quit()
