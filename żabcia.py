import pygame
import sys
import os

### okno ###
width = 600
height = 640
okno = pygame.display.set_mode([width, height])
pygame.display.set_caption("Żabber")

### grafiki ###
tlo_gry = pygame.image.load("plansza1.png")
postac = pygame.image.load("zaba_postac1.png")

### rzeczy do ruchu postaci czy coś ###
## lokacja startowa żaby:
postac_x = 280
postac_y = 560

## jeden krok żabki i szerokość "pasów ruchu"
postac_liczba_pikseli = 40


running = True
while running:
    for akcja in pygame.event.get():
        if akcja.type == pygame.QUIT:
            running = False

    ruch_zaby = pygame.key.get_pressed()
    if ruch_zaby[pygame.K_LEFT] or ruch_zaby[pygame.K_a]:
        postac_x -= postac_liczba_pikseli
    elif ruch_zaby[pygame.K_RIGHT] or ruch_zaby[pygame.K_d]:
        postac_x += postac_liczba_pikseli
    elif ruch_zaby[pygame.K_DOWN] or ruch_zaby[pygame.K_s]:
        postac_y += postac_liczba_pikseli
    elif ruch_zaby[pygame.K_UP] or ruch_zaby[pygame.K_w]:
        postac_y -= postac_liczba_pikseli

    pygame.time.delay(100)

    okno.blit(tlo_gry, [0, 0])
    okno.blit(postac, [postac_x, postac_y])
    pygame.display.update()


pygame.quit()
