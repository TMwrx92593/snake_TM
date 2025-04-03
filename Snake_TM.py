import pygame
import time
import random

pygame.init()

biały = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (213, 50, 80)
zielony = (0, 255, 0)
niebieski = (50, 153, 213)

szerokość = 600
wysokość = 400
okno = pygame.display.set_mode((szerokość, wysokość))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
szybkość = 1 


wielkosc_segmentu = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
wynik_font = pygame.font.SysFont("comicsansms", 35)


def pokaz_wynik(wynik):
    value = wynik_font.render(f"Twoje wyniki: {wynik}", True, czarny)
    okno.blit(value, [0, 0])


def rysuj_weza(wielkosc_segmentu, lista_segmentów):
    for x in lista_segmentów:
        pygame.draw.rect(okno, zielony, [x[0], x[1], wielkosc_segmentu, wielkosc_segmentu])

def gra():
    game_over = False
    game_close = False

    
    x1 = szerokość / 2
    y1 = wysokość / 2

    x1_zmiana = 0
    y1_zmiana = 0

  
    segmenty_węża = []
    dlugosc_węża = 1

  
    jabłko_x = round(random.randrange(0, szerokość - wielkosc_segmentu) / 10.0) * 10.0
    jabłko_y = round(random.randrange(0, wysokość - wielkosc_segmentu) / 10.0) * 10.0

    while not game_over:

        while game_close:
            okno.fill(niebieski)
            pokaz_wynik(dlugosc_węża - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gra()
