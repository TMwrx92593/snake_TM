import pygame
import random

pygame.init()

biały = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (213, 50, 80)
zielony = (0, 255, 0)
niebieski = (50, 153, 213)
cegla = (139, 69, 19)

szerokość = 600
wysokość = 400
okno = pygame.display.set_mode((szerokość, wysokość))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
szybkość = 10 


wielkosc_segmentu = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
wynik_font = pygame.font.SysFont("comicsansms", 35)


def pokaz_wynik(wynik):
    value = wynik_font.render(f"Twoje wyniki: {wynik}", True, czarny)
    okno.blit(value, [0, 0])


def rysuj_weza(wielkosc_segmentu, lista_segmentów):
    for x in lista_segmentów:
        pygame.draw.rect(okno, zielony, [x[0], x[1], wielkosc_segmentu, wielkosc_segmentu])



def ekran_powitalny():
    okno.fill(niebieski)
    powitanie_text = font_style.render("Snake let's play - Push the button", True, czarny)
    powitanie_x = (szerokość - powitanie_text.get_width()) / 2  
    powitanie_y = wysokość / 2 - 25  
    okno.blit(powitanie_text, [powitanie_x, powitanie_y])

 
    instrukcja_text = font_style.render("Naciśnij dowolny klawisz, aby rozpocząć!", True, czarny)
    instrukcja_x = (szerokość - instrukcja_text.get_width()) / 2  
    instrukcja_y = wysokość / 2 + 25 
    okno.blit(instrukcja_text, [instrukcja_x, instrukcja_y])

    pygame.display.update()

def rysuj_obramowanie():
    cegła_szerokość = 20  
    cegła_wysokość = 10  

    for x in range(0, szerokość, cegła_szerokość):
        pygame.draw.rect(okno, cegla, [x, 0, cegła_szerokość, cegła_wysokość])
        pygame.draw.rect(okno, cegla, [x, wysokość - cegła_wysokość, cegła_szerokość, cegła_wysokość]) 
    
    for y in range(0, wysokość, cegła_wysokość):
        pygame.draw.rect(okno, cegla, [0, y, cegła_szerokość, cegła_wysokość])  
        pygame.draw.rect(okno, cegla, [szerokość - cegła_szerokość, y, cegła_szerokość, cegła_wysokość])  

def generuj_jablko():
 
    safe_zone_start = 20 
    safe_zone_end_x = szerokość - 20  
    safe_zone_end_y = wysokość - 20  

    jabłko_x = round(random.randrange(safe_zone_start, (safe_zone_end_x // wielkosc_segmentu)) - 1) * wielkosc_segmentu
    jabłko_y = round(random.randrange(safe_zone_start, (safe_zone_end_y // wielkosc_segmentu)) - 1) * wielkosc_segmentu
    return jabłko_x, jabłko_y

def pokaz_game_over(wynik):
    game_over_text = font_style.render("Game Over!", True, czarny)
    wynik_text = font_style.render(f"Twój wynik: {wynik}", True, czarny)
    
    tekst_x = (szerokość - game_over_text.get_width()) / 2
    tekst_y = wysokość / 2 - 50
    okno.blit(game_over_text, [tekst_x, tekst_y])

    wynik_x = (szerokość - wynik_text.get_width()) / 2
    wynik_y = wysokość / 2
    okno.blit(wynik_text, [wynik_x, wynik_y])


def gra():
    game_over = False
    game_close = False

    
    x1 = szerokość / 2
    y1 = wysokość / 2

    x1_zmiana = 0
    y1_zmiana = 0

  
    segmenty_węża = []
    dlugosc_węża = 1

  
    jabłko_x, jabłko_y = generuj_jablko()

    pierwszy_ruch = False

    ostatni_kierunek = None

    while not game_over:

        while game_close:
            okno.fill(niebieski)
            rysuj_obramowanie()
            pokaz_game_over(dlugosc_węża - 1)
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if not pierwszy_ruch:
                    pierwszy_ruch = True 

                
                if event.key == pygame.K_LEFT and ostatni_kierunek != "RIGHT":
                    x1_zmiana = -wielkosc_segmentu
                    y1_zmiana = 0
                    ostatni_kierunek = "LEFT"
                elif event.key == pygame.K_RIGHT and ostatni_kierunek != "LEFT":
                    x1_zmiana = wielkosc_segmentu
                    y1_zmiana = 0
                    ostatni_kierunek = "RIGHT"
                elif event.key == pygame.K_UP and ostatni_kierunek != "DOWN":
                    y1_zmiana = -wielkosc_segmentu
                    x1_zmiana = 0
                    ostatni_kierunek = "UP"
                elif event.key == pygame.K_DOWN and ostatni_kierunek != "UP":
                    y1_zmiana = wielkosc_segmentu
                    x1_zmiana = 0
                    ostatni_kierunek = "DOWN"

        if not pierwszy_ruch:
            continue

        if x1 >= szerokość - wielkosc_segmentu or x1 < wielkosc_segmentu or y1 >= wysokość - wielkosc_segmentu or y1 < wielkosc_segmentu:
           game_close = True

        x1 += x1_zmiana
        y1 += y1_zmiana
        okno.fill(niebieski)

        rysuj_obramowanie()

        pygame.draw.rect(okno, czerwony, [jabłko_x, jabłko_y, wielkosc_segmentu, wielkosc_segmentu])

        segment_węża = []
        segment_węża.append([x1, y1])
        if len(segmenty_węża) > dlugosc_węża:
            del segmenty_węża[0]

        segmenty_węża.append(segment_węża[0])

        for x in segmenty_węża[:-1]:
            if x == segment_węża[0]:
                game_close = True

        rysuj_weza(wielkosc_segmentu, segmenty_węża)
        pokaz_wynik(dlugosc_węża - 1)

        pygame.display.update()


        if x1 == jabłko_x and y1 == jabłko_y:
            jabłko_x, jabłko_y = generuj_jablko()
            dlugosc_węża += 1

        clock.tick(szybkość)



    pygame.quit()
    quit()

def menu():
    ekran_powitalny()
    rozpocznij_grę = False
    while not rozpocznij_grę:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                rozpocznij_grę = True
                gra()

menu()