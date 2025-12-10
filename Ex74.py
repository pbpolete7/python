import pygame
import sys

# Inicialitzar Pygame
pygame.init()

# Configuració de la finestra
amplada = 800
alcada = 600
pantalla = pygame.display.set_mode((amplada, alcada))
pygame.display.set_caption("Arkanoid Bàsic")

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
ROIG = (255, 0, 0)
VERD = (0, 255, 0)
BLAVO = (0, 0, 255)

# FPS
reloj = pygame.time.Clock()
FPS = 60

# Barra del jugador
barra_imatge = pygame.image.load("barra.png")  # Fitxer al mateix directori
barra_rect = barra_imatge.get_rect()
barra_rect.midbottom = (amplada // 2, alcada - 30)
barra_vel = 8

# Pilota
pilota_imatge = pygame.image.load("pilota.png")  # Fitxer al mateix directori
pilota_rect = pilota_imatge.get_rect()
pilota_rect.center = (amplada // 2, alcada // 2)
pilota_vel = [5, -5]

# Maons
maons = []
bloc_amplada = 60
bloc_alcada = 20
files = 5
columnes = 10

for fila in range(filas):
    for columna in range(columnes):
        rect = pygame.Rect(columna*bloc_amplada + 35, fila*bloc_alcada + 50, bloc_amplada-5, bloc_alcada-5)
        maons.append(rect)

# Joc pausat fins prémer espai
joc_comencat = False

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                joc_comencat = True

    # Tecles premudes
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT] and barra_rect.left > 0:
        barra_rect.x -= barra_vel
    if tecles[pygame.K_RIGHT] and barra_rect.right < amplada:
        barra_rect.x += barra_vel

    if joc_comencat:
        pilota_rect.x += pilota_vel[0]
        pilota_rect.y += pilota_vel[1]

        # Col·lisions amb les parets
        if pilota_rect.left <= 0 or pilota_rect.right >= amplada:
            pilota_vel[0] *= -1
        if pilota_rect.top <= 0:
            pilota_vel[1] *= -1
        if pilota_rect.bottom >= alcada:
            joc_comencat = False
            pilota_rect.center = (amplada // 2, alcada // 2)

        # Col·lisions amb la barra
        if pilota_rect.colliderect(barra_rect):
            pilota_vel[1] *= -1

        # Col·lisions amb maons
        for bloc in maons[:]:
            if pilota_rect.colliderect(bloc):
                pilota_vel[1] *= -1
                maons.remove(bloc)

    # Pintar pantalla
    pantalla.fill(NEGRE)
    pantalla.blit(barra_imatge, barra_rect)
    pantalla.blit(pilota_imatge, pilota_rect)

    for bloc in maons:
        pygame.draw.rect(pantalla, ROIG, bloc)

    pygame.display.flip()
    reloj.tick(FPS)
