import pygame
from random import randint

pygame.init()

width, height = 1280, 720
clock = pygame.time.Clock()
dt = 0
running = True

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Race Game 1vs1")
tf = pygame.font.Font("src/contrast.ttf", 50)
background = pygame.transform.scale(pygame.image.load("src/circuit3.png"), (width, height))
sf = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("src/AE86.png"), (150, 70)),90)

rect_sf =  sf.get_rect()
angle = 0

def move(keys):
    global sf
    if keys[pygame.K_w]:
        rect_sf.y -= 1
    if keys[pygame.K_s]:
        rect_sf.y += 1
    if keys[pygame.K_a]:
        rect_sf.x -= 1
    if keys[pygame.K_d]:
        rect_sf.x += 1

def limit():
    global rect_sf
    if rect_sf.top <= 0: 
        rect_sf.top = 0
    
    if rect_sf.bottom >= height: 
        rect_sf.bottom = height

    if rect_sf.left <= 0: 
        rect_sf.left = 0

    if rect_sf.right >= width: 
        rect_sf.right = width


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                sf = pygame.transform.rotate(sf, 1)
                rect_sf = sf.get_rect()

                
    # BACKGROUND
    screen.blit(background, (0, 0))
    limit()
    pygame.draw.rect(screen, "Pink", rect_sf, 1)
    
    keys = pygame.key.get_pressed()
    move(keys)
    sf =  pygame.transform.rotate(sf, angle)
    angle += 1
    screen.blit(sf, rect_sf)
    pygame.display.update()
    dt = clock.tick(10)
    #print(dt)

pygame.quit()


