import pygame
from pygame.locals import *

screen_width, screen_height = 600, 500
pygame.init()
pygame.display.set_caption('Pygame Planet Invader')
screen = pygame.display.set_mode((screen_width, screen_height))


# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)


weapon = pygame.image.load('assets/weapon.png').convert()
planet = pygame.image.load('assets/planet.png').convert()
background = pygame.image.load('assets/background.png').convert()


planet_rect = planet.get_rect()
weapon_rect = weapon.get_rect()
background_rect = background.get_rect()

weapon_rect.center = screen_width//2,round(screen_height*5/7)

planet_speed = [2, 0]

# GAME LOOP
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            running = False
            
            
    # screen.blit(background,background_rect)
    planet_rect = planet_rect.move(planet_speed)
    if planet_rect.left < 0 or planet_rect.right > screen_width:
        planet_speed[0] = -planet_speed[0]

    # print(planet_rect.size)
    # print(weapon_rect.size)
    screen.blit(planet, planet_rect)
    screen.blit(weapon, weapon_rect)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
