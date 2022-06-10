
import pygame
import sys
import os
from pygame import rect


### okno ###
szerokosc = 600
wysokosc = 640
okno = pygame.display.set_mode([szerokosc, wysokosc])
pygame.display.set_caption("Żabber")

### grafiki ###
tlo_gry = pygame.image.load("plansza1.png")
postac = pygame.image.load("zaba_postac1.png").convert_alpha()
autko = pygame.image.load("auto1.png").convert_alpha()
klody = pygame.image.load("kloda1.png").convert_alpha()
zolwiki = pygame.image.load("zolwie1.png").convert_alpha()


class Zaba():
    def __init__(self):
        self.zaba = postac.get_rect()
        self.x_zaba = 280
        self.y_zaba = 560

    def ruch_postaci(self):
        ruch_zaby = pygame.key.get_pressed()
        if (ruch_zaby[pygame.K_LEFT] or ruch_zaby[pygame.K_a]) and zabka.x_zaba>0:
            zabka.x_zaba -= postac_liczba_pikseli
        elif (ruch_zaby[pygame.K_RIGHT] or ruch_zaby[pygame.K_d]) and zabka.x_zaba<560:
            zabka.x_zaba += postac_liczba_pikseli
        elif (ruch_zaby[pygame.K_DOWN] or ruch_zaby[pygame.K_s]) and zabka.y_zaba<560:
            zabka.y_zaba += postac_liczba_pikseli
        elif (ruch_zaby[pygame.K_UP] or ruch_zaby[pygame.K_w]) and zabka.y_zaba>40:
            zabka.y_zaba -= postac_liczba_pikseli


class Auto():
    def __init__(self):
        self.rect = autko.get_rect()
        self.x_auto = 560
        self.y_auto = 520
        self.szybkosc = 10


    def ruch_auta(self):
        self.x_auto -= self.szybkosc
        if self.x_auto<-120:
            self.x_auto = 600
            self.y_auto = 520



zabka=Zaba()
auto1=Auto()

## jeden krok żabki i szerokość "pasów ruchu"
postac_liczba_pikseli = 40


running = True
while running:
    for akcja in pygame.event.get():
        if akcja.type == pygame.QUIT:
            running = False

    zabka.ruch_postaci()
    auto1.ruch_auta()
 
 
    pygame.time.delay(60)

    okno.blit(tlo_gry, [0, 0])
    okno.blit(postac, [zabka.x_zaba, zabka.y_zaba])
    okno.blit(autko, [auto1.x_auto, auto1.y_auto])
    pygame.display.update()


pygame.quit() 
