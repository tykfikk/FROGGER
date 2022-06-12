
import pygame
import sys
import os
from pygame import rect
from random import randint



### okno ###
szerokosc = 600
wysokosc = 640
okno = pygame.display.set_mode([szerokosc, wysokosc])
pygame.display.set_caption("Żabber")
zegar = pygame.time.Clock()

### grafiki ###
tlo_gry = pygame.image.load("plansza1.png")
postac = pygame.image.load("zaba_postac1.png").convert_alpha()
autko = pygame.image.load("auto1.png").convert_alpha()
autko_odwrocone = pygame.image.load("auto2.png").convert_alpha()
klody = pygame.image.load("kloda1.png").convert_alpha()
zolwiki = pygame.image.load("zolwie1.png").convert_alpha()
zolwiki_odwrocone = pygame.image.load("zolwie2.png").convert_alpha()
zaba_win = pygame.image.load("zaba_win3.png").convert_alpha()
zaba_ups = pygame.image.load("zaba_ups4.png").convert_alpha()
zaba_GO = pygame.image.load("zaba_GameOver2.png").convert_alpha
liczba_zyc0 = pygame.image.load("serca0.png").convert_alpha()
liczba_zyc1 = pygame.image.load("serca1.png").convert_alpha()
liczba_zyc2 = pygame.image.load("serca2.png").convert_alpha()
liczba_zyc3 = pygame.image.load("serca3.png").convert_alpha()

global liczba_smierci
liczba_smierci=0

class Zaba():
    def __init__(self):
        self.zaba = postac.get_rect()
        self.x_zaba = 280
        self.y_zaba = 560
        self.zaba_szerokosc = 40
        self.zaba_wysokosc = 40
        self.zycie = 1
   

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

    def zaba_wygrana(self):
        if self.y_zaba <79 and self.x_zaba <=600:
            okno.blit(zaba_win, [0,0])
            pygame.display.update()
            pygame.time.delay(2500)
            self.x_zaba= 280
            self.y_zaba = 560



class Auto():
    def __init__(self, szybkosc, x, y):
        self.auto_rect = autko.get_rect()
        self.x_auto = x
        self.y_auto = y
        self.auto_szerokosc = 95
        self.auto_wysokosc = 40
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
        self.kloda_rect = klody.get_rect()
        self.x_kloda = x
        self.y_kloda = y
        self.kloda_wysokosc = 40
        self.kloda_szerokosc = 240
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
        self.zolw_rect = zolwiki.get_rect()
        self.x_zolw = x
        self.y_zolw = y
        self.zolw_wysokosc = 40
        self.zolw_szerokosc = 216
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

def wykryj_kolizje(obiekt):
    if zabka.x_zaba >= obiekt.x_auto and (zabka.x_zaba+zabka.zaba_szerokosc)<=(obiekt.x_auto+obiekt.auto_szerokosc) and zabka.y_zaba<=obiekt.y_auto and (zabka.y_zaba-zabka.zaba_wysokosc)>=(obiekt.y_auto-obiekt.auto_wysokosc):
        return True

def kolizja(obiekt):
    if wykryj_kolizje(obiekt)==True:
        zabka.x_zaba = 280
        zabka.y_zaba = 560
        liczba_smierci+=1

def wykryj_klody(obiekt):
    if zabka.x_zaba >= obiekt.x_kloda and (zabka.x_zaba+zabka.zaba_szerokosc)<=(obiekt.x_kloda+obiekt.kloda_szerokosc) and zabka.y_zaba<=obiekt.y_kloda and (zabka.y_zaba-zabka.zaba_wysokosc)>=(obiekt.y_kloda-obiekt.kloda_wysokosc):
        return True

def wykryj_zolwie(obiekt):
    if zabka.x_zaba >= obiekt.x_zolw and (zabka.x_zaba+zabka.zaba_szerokosc)<=(obiekt.x_zolw+obiekt.zolw_szerokosc) and zabka.y_zaba<=obiekt.y_zolw and (zabka.y_zaba-zabka.zaba_wysokosc)>=(obiekt.y_zolw-obiekt.zolw_wysokosc):
        return True

def zaba_na_klodach_prawo(obiekt,dana_szybkosc):
    if wykryj_klody(obiekt)==True:
        zabka.x_zaba+=dana_szybkosc


def zaba_na_klodach_lewo(obiekt,dana_szybkosc):
    if wykryj_klody(obiekt)==True:
        zabka.x_zaba-=dana_szybkosc


def zaba_na_zolwiach_prawo(obiekt,dana_szybkosc):
    if wykryj_zolwie(obiekt)==True:
        zabka.x_zaba+=dana_szybkosc

def zaba_na_zolwiach_lewo(obiekt,dana_szybkosc):
    if wykryj_zolwie(obiekt)==True:
        zabka.x_zaba-=dana_szybkosc


def zaba_na_wodzie():
    if zabka.x_zaba >= 0 and (zabka.x_zaba+zabka.zaba_szerokosc)<=600 and zabka.y_zaba<=280 and (zabka.y_zaba-zabka.zaba_wysokosc)>=80:
        return True

def win():
    if zabka.y_zaba<=79:
        return True

def liczba_serduszek():
    if liczba_smierci==0:
        okno.blit(liczba_zyc3, [10,0])
    elif liczba_smierci==1:
        okno.blit(liczba_zyc2, [10,0])
    elif liczba_smierci==2:
        okno.blit(liczba_zyc1, [10,0])
    else:
        okno.blit(liczba_zyc0, [10,0])
        pygame.display.update()
    
    

zabka=Zaba()
auto1=Auto(10,560,520)
auto2=Auto(15,200,480)
auto3=Auto(12,400,440)
auto4=Auto(16,700,400)
auto5=Auto(13,300,360)
kloda1=Kloda(9,230,280)
kloda2=Kloda(11,-120,200)
kloda3=Kloda(6,-400,120)
kloda4=Kloda(6,0,120)
zolwie1=Zolwie(8,890,240)
zolwie2=Zolwie(9,150,160)
zolwie3=Zolwie(8,300,240)
zolwie4=Zolwie(9,500,160)


## jeden krok żabki i szerokość "pasów ruchu"
postac_liczba_pikseli = 40


running = True
while running:
    for akcja in pygame.event.get():
        if akcja.type == pygame.QUIT:
            running = False

    czas = zegar.tick(10)

    if liczba_smierci<3:
        liczba_serduszek()
        zabka.ruch_postaci()
        zabka.zaba_wygrana()
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
        zolwie3.ruch_zolwia_prawo()
        kloda4.ruch_klody_prawo()
        zolwie4.ruch_zolwia()
        wykryj_kolizje(auto1)
        kolizja(auto1)
        wykryj_kolizje(auto2)
        kolizja(auto2)
        wykryj_kolizje(auto3)
        kolizja(auto3)
        wykryj_kolizje(auto4)
        kolizja(auto4)
        wykryj_kolizje(auto5)
        kolizja(auto5)
        if zaba_na_wodzie()==True:
            if wykryj_klody(kloda1)==True or wykryj_klody(kloda2)==True or wykryj_klody(kloda3)==True or wykryj_klody(kloda3)==True or wykryj_zolwie(zolwie1)==True or wykryj_zolwie(zolwie2)==True or wykryj_zolwie(zolwie3) or wykryj_zolwie(zolwie4)==True:
                zaba_na_klodach_lewo(kloda1,9)
                zaba_na_klodach_lewo(kloda2,11)
                zaba_na_klodach_prawo(kloda3,6)
                zaba_na_klodach_prawo(kloda4,6)
                zaba_na_zolwiach_prawo(zolwie1,8)
                zaba_na_zolwiach_lewo(zolwie2,13)
                zaba_na_zolwiach_prawo(zolwie3,8)
                zaba_na_zolwiach_lewo(zolwie4,9)
            else: 
                # liczba_smierci+=1
    # if win()==True:
                print("hura!")
    

 
    # pygame.time.delay(60)

    okno.blit(tlo_gry, [0, 0])
    okno.blit(klody, [kloda1.x_kloda, kloda1.y_kloda])
    okno.blit(klody, [kloda2.x_kloda, kloda2.y_kloda])
    okno.blit(klody, [kloda3.x_kloda, kloda3.y_kloda])  
    okno.blit(klody, [kloda4.x_kloda, kloda4.y_kloda]) 
    okno.blit(zolwiki_odwrocone, [zolwie1.x_zolw, zolwie1.y_zolw])
    okno.blit(zolwiki, [zolwie2.x_zolw, zolwie2.y_zolw])
    okno.blit(zolwiki_odwrocone, [zolwie3.x_zolw, zolwie3.y_zolw])
    okno.blit(zolwiki, [zolwie4.x_zolw, zolwie4.y_zolw])
    okno.blit(postac, [zabka.x_zaba, zabka.y_zaba])
    okno.blit(autko, [auto1.x_auto, auto1.y_auto])
    okno.blit(autko, [auto2.x_auto, auto2.y_auto])
    okno.blit(autko_odwrocone, [auto3.x_auto, auto3.y_auto])
    okno.blit(autko, [auto4.x_auto, auto4.y_auto])
    okno.blit(autko_odwrocone, [auto5.x_auto, auto5.y_auto])

    pygame.display.update()


pygame.quit() 


