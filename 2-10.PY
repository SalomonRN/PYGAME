import pygame
from random import randint

pygame.init()

width, height = 1280, 720
clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimiento")
background = pygame.transform.scale(pygame.image.load("src/back.png"), (width, height))

sf = pygame.image.load("src/player1.png")
rect_sf =  sf.get_rect()

sf2 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("src/player2.png"), -90), (100, 50))
rect_sf2 =  sf2.get_rect()

sf3 = pygame.transform.scale(pygame.image.load("src/player3.png"), (100, 50))
rect_sf3 =  sf3.get_rect()

sf4 = pygame.transform.scale(pygame.image.load("src/player4.png"), (100, 50))
rect_sf4 =  sf4.get_rect()
players = [rect_sf, rect_sf2, rect_sf3, rect_sf4]
players = {"Player 1":rect_sf,"Player 2 ": rect_sf2,"Player 3": rect_sf3,"Player 4": rect_sf4}
move_speed = 10

rect_sf2.y = 30
rect_sf3.y = 60
rect_sf4.y = 120

def move(keys):
    global sf
    if keys[pygame.K_w]:
        rect_sf.y -= move_speed
    if keys[pygame.K_s]:
        rect_sf.y += move_speed
    if keys[pygame.K_a]:
        rect_sf.x -= move_speed
    if keys[pygame.K_d]:
        rect_sf.x += move_speed

def limit():
    global rect_sf, players, running
    
    for pl, player in players.items():
        if player.top <= 0: 
            player.top = 0
    
        if player.bottom >= height: 
            player.bottom = height

        if player.left <= 0: 
            player.left = 0

        if player.right >= width: 
            player.right = width
            print(f"Ganó {pl}")
            running = False
            


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    screen.blit(background, (0, 0))

    move(pygame.key.get_pressed())
    limit()
    
    screen.blit(sf, rect_sf)
    screen.blit(sf2, rect_sf2)
    screen.blit(sf3, rect_sf3)
    screen.blit(sf4, rect_sf4)
    

    rect_sf2.y += randint(1, 5)
    rect_sf3.x += randint(1, 5)
    rect_sf4.x += randint(1, 5)
    
    pygame.display.update()
    dt = clock.tick(60)

pygame.quit()


