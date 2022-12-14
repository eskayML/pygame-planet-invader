import pygame
from pygame.locals import *

# sysfont = pygame.font.SysFont(None, 24)
# score_board = sysfont.render(sysfont, True , 'white')

screen_width, screen_height = 600, 500
pygame.init()
pygame.display.set_caption('Pygame Planet Invader')
screen = pygame.display.set_mode((screen_width, screen_height))


#load assets
weapon = pygame.image.load('assets/weapon.png').convert()
planet = pygame.image.load('assets/planet.png').convert()
background = pygame.image.load('assets/background.png').convert()
bullet = pygame.image.load('assets/bullet.png').convert()

#get bounding rectangles
planet_rect = planet.get_rect()
weapon_rect = weapon.get_rect()
background_rect = background.get_rect()
bullet_rect = bullet.get_rect()


weapon_rect.center = screen_width//2, round(screen_height*5/7)
bullet_rect.center = weapon_rect.center
# the bullet will be drawn exactly under the centre of the weapon making it look like
# as if it is being shot out of the gun

# velocity vectors
planet_speed = [2, 0]
bullet_speed = [0,-4]

fire = False
# GAME LOOP
score  = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            fire = True
            
            

    # screen.blit(background,background_rect)
    planet_rect = planet_rect.move(planet_speed)
    if planet_rect.left < 0 or planet_rect.right > screen_width:
        planet_speed[0] = -planet_speed[0]
        
        

    if fire == True:
        bullet_rect = bullet_rect.move(bullet_speed)
    if bullet_rect.colliderect(planet_rect):
        score += 1
        print(score)
    if bullet_rect.colliderect(planet_rect) or bullet_rect.top <=0:
        bullet_rect.center = weapon_rect.center
        fire = False
        
    screen.fill('black')
    screen.blit(bullet, bullet_rect)
    screen.blit(planet, planet_rect)
    screen.blit(weapon, weapon_rect)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
