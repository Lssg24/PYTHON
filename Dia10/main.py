import math
import random

import pygame

# inicializar pygame en nuestro codigo
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
incono = pygame.image.load('rocket.png')
pygame.display.set_caption('Invasión LuxitomaRio')
pygame.display.set_icon(incono)
fondo = pygame.image.load('espacio.jpg')

# puntaje
puntaje = 0

# Jugador
img_jugador = pygame.image.load('nave.png')
jugador_x = 368
jugador_y = 500
jugador_movimiento = 0

# Enemigo
img_enemigo = pygame.image.load('ufo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_movimiento_x = 0.3
enemigo_movimiento_y = 50

# Bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_movimiento_x = 0
bala_movimiento_y = 1
bala_visible = False


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# detectar coliciones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# loop del juego
se_ejecuta = True
while se_ejecuta:

    # rgb
    pantalla.blit(fondo, (0, 0))
    # pantalla.fill((205, 144, 100))

    # iterar eventos
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_movimiento = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_movimiento = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_movimiento = 0

    # movimiento bala

    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_movimiento_y

    # colision
    colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigo_x = random.randint(0, 736)
        enemigo_y = random.randint(50, 200)

    # modificar ubicacion jugador
    jugador_x += jugador_movimiento

    # matener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicacion enemigo
    enemigo_x += enemigo_movimiento_x

    # matener dentro de bordes enemigo
    if enemigo_x <= 0:
        enemigo_movimiento_x = 0.2
        enemigo_y += enemigo_movimiento_y
    elif enemigo_x >= 736:
        enemigo_movimiento_x = -0.2
        enemigo_y += enemigo_movimiento_y

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()
