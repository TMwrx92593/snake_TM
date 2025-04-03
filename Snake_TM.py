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
