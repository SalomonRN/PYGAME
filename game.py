import pygame
from random import randint

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Aim Game")
tf = pygame.font.Font("src/contrast.ttf", 50)
clock = pygame.time.Clock()
dt = 0
running = True
score = 0
counter = 0


TIMER_EVENT = pygame.USEREVENT + 1

#pygame.time.set_timer(TIMER_EVENT, 1000)
line = pygame.surface.Surface((300, 0))
valo_surf = pygame.image.load("src/image.png")
valo_rect = valo_surf.get_rect(topleft=(0, 720))
player_surf = pygame.image.load("src/player.png").convert()
player_rect = player_surf.get_rect()
target_surf = pygame.image.load("src/target.png").convert()
target_rect = target_surf.get_rect(center = (randint(0, width),randint(0, height)))
gravity = 0

while running:
    if counter == 10:
        pygame.time.wait(2000)    
    if not pygame.display.get_active():
        pygame.time.delay(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TIMER_EVENT:
            counter+=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -21 
            if event.key == pygame.K_u:
                player_rect.y = -1000
                #pygame.display.toggle_fullscreen()
    
    screen.fill("black")
    fps = tf.render(f"FPS {(int(clock.get_fps()))}", False, "Green")
    txt_score = tf.render(f"Puntuacion {score}", False, "White")
    #pygame.draw.rect(player_surf, "Pink", player_rect)
    pygame.draw.line(screen, "Blue", (0, 300), (width, 300 ))
    gravity +=1
    player_rect.y += gravity
    if player_rect.top <= 0:
        pygame.time.delay(500)
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
         
    mouse_pos = pygame.mouse.get_pos()
    #screen.blit(target_surf, target_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(fps, (0, 0))
    screen.blit(txt_score, (width/2, 0))
    screen.blit(line, (0, 300))

    if target_rect.collidepoint(mouse_pos):
        target_rect = target_surf.get_rect(center = (randint(0, width),randint(0, height)))
        screen.blit(target_surf, target_rect)
        score += 1

    
    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()