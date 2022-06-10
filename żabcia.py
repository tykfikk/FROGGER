
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
    def __init__(self, szybkosc, x, y):
        self.rect = autko.get_rect()
        self.x_auto = x
        self.y_auto = y
        self.szybkosc = szybkosc


    def ruch_auta(self):
        self.x_auto -= self.szybkosc
        if self.x_auto<-120:
            self.x_auto = 600 
            self.y_auto = self.y_auto

    def ruch_auta_prawo(self):
        self.x_auto += self.szybkosc
        if self.x_auto>720:
            self.x_auto = -120
            self.y_auto = self.y_auto

class Kloda():
    def __init__(self, szybkosc, x, y):
        self.rect = klody.get_rect()
        self.x_kloda = x
        self.y_kloda = y
        self.szybkosc = szybkosc


    def ruch_klody(self):
        self.x_kloda -= self.szybkosc
        if self.x_kloda<-120:
            self.x_kloda = 600 
            self.y_kloda = self.y_kloda

    def ruch_klody_prawo(self):
        self.x_kloda += self.szybkosc
        if self.x_kloda>720:
            self.x_kloda = -120
            self.y_kloda = self.y_kloda

class Zolwie():
    def __init__(self, szybkosc, x, y):
        self.rect = zolwiki.get_rect()
        self.x_zolw = x
        self.y_zolw = y
        self.szybkosc = szybkosc


    def ruch_zolwia(self):
        self.x_zolw -= self.szybkosc
        if self.x_zolw<-120:
            self.x_zolw = 600 
            self.y_zolw = self.y_zolw

    def ruch_zolwia_prawo(self):
        self.x_zolw += self.szybkosc
        if self.x_zolw>720:
            self.x_zolw = -120
            self.y_zolw = self.y_zolw 



zabka=Zaba()
auto1=Auto(10,560,520)
auto2=Auto(15,200,480)
auto3=Auto(12,400,440)
auto4=Auto(16,700,400)
auto5=Auto(13,300,360)
kloda1=Kloda(9,230,280)
kloda2=Kloda(11,-120,200)
kloda3=Kloda(6,100,120)
zolwie1=Zolwie(8,890,240)
zolwie2=Zolwie(13,500,160)

## jeden krok żabki i szerokość "pasów ruchu"
postac_liczba_pikseli = 40


running = True
while running:
    for akcja in pygame.event.get():
        if akcja.type == pygame.QUIT:
            running = False

    zabka.ruch_postaci()
    auto1.ruch_auta()
    auto2.ruch_auta()
    auto3.ruch_auta_prawo()
    auto4.ruch_auta()
    auto5.ruch_auta_prawo()
    kloda1.ruch_klody()
    zolwie1.ruch_zolwia_prawo()
    kloda2.ruch_klody()
    zolwie2.ruch_zolwia()
    kloda3.ruch_klody_prawo()
 
 
    pygame.time.delay(60)

    okno.blit(tlo_gry, [0, 0])
    okno.blit(klody, [kloda1.x_kloda, kloda1.y_kloda])
    okno.blit(klody, [kloda2.x_kloda, kloda2.y_kloda])
    okno.blit(klody, [kloda3.x_kloda, kloda3.y_kloda])   
    okno.blit(zolwiki, [zolwie1.x_zolw, zolwie1.y_zolw])
    okno.blit(zolwiki, [zolwie2.x_zolw, zolwie2.y_zolw])
    okno.blit(postac, [zabka.x_zaba, zabka.y_zaba])
    okno.blit(autko, [auto1.x_auto, auto1.y_auto])
    okno.blit(autko, [auto2.x_auto, auto2.y_auto])
    okno.blit(autko, [auto3.x_auto, auto3.y_auto])
    okno.blit(autko, [auto4.x_auto, auto4.y_auto])
    okno.blit(autko, [auto5.x_auto, auto5.y_auto])
    pygame.display.update()


pygame.quit() 
