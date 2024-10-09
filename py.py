import pygame

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 860, 484
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Animación Personaje')
icono=pygame.image.load('src/player1.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('src/back.png')

# Carga de imagen para personaje posición quieto
quieto = pygame.image.load('src/img/idle0.png')
quieto = pygame.transform.scale(quieto, (100, 100))
# Carga de imágenes para personaje caminar a la derecha
caminaD = [
    pygame.image.load('src/img/walk0.png'),
    pygame.image.load('src/img/walk1.png'),
    pygame.image.load('src/img/walk2.png'),
    pygame.image.load('src/img/walk3.png'),
    pygame.image.load('src/img/walk4.png')]

caminaDerecha = [pygame.transform.scale(i, (100, 100)) for i in caminaD]

# Carga de imágenes para personaje caminar a la izquierda
caminaIzq = caminaD.copy()

caminaIzquierda = [pygame.transform.scale(i, (100, 100)) for i in caminaIzq]
caminaIzquierda = [pygame.transform.flip(
    i, True, False) for i in caminaIzquierda]

# Carga de imágenes para personaje saltar
salta = [pygame.image.load('src/img/jump0.png'),
         pygame.image.load('src/img/jump1.png'),
         pygame.image.load('src/img/jump2.png'),
         pygame.image.load('src/img/jump3.png'),
         pygame.image.load('src/img/jump4.png'),
         pygame.image.load('src/img/jump5.png'),
         pygame.image.load('src/img/jump6.png'),
         pygame.image.load('src/img/jump7.png'),
         pygame.image.load('src/img/jump8.png')]

salta = [pygame.transform.scale(i, (100, 100)) for i in salta]

# Variables de posición y movimiento del personaje
x = 0
px = 50
py = 290
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variable para salto inicializar
salto = False
# Contador de salto inicializar
cuentaSalto = 9  # Controlar la altura y la duración del salto del personaje

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento


def recarga_pantalla():
    # Variables globales
    global cuentaPasos
    global x

    # Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5

    # Contador de pasos y actualización de animaciones según dirección
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0

    # Si Movimiento a la izquierda muestra animaciones
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

        # Si Movimiento a la derecha, muestra animaciones
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
        print(F"PASO {cuentaPasos}")

    else:
        PANTALLA.blit(quieto, (int(px), int(py)))



ejecuta = True

# Bucle de acciones y controles
while ejecuta:
    # FPS
    reloj.tick(20)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla A - Movimiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # Tecla D - Movimiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        if salto: cuentaPasos = 0

    # Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    # Tecla S - Movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad

    # Tecla SPACE - Salto
    if not salto:
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        #ESTO AYUDA PARA EL SUELO
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    # Actualización de la ventana
    pygame.display.update()
    # Llamada a la función de actualización de la ventana
    recarga_pantalla()

# Salida del juego
pygame.quit()
