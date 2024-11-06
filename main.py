import random
import bassin
from world import World, COLONNE, LIGNE
import os
import time
import pygame
import sys
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

CONSTANTES = 0
NBRE_FISH_INITAL = 50
NBRE_SHARK_INITAL = 2
chronon_counter = 0
taille_ecran = (1300,1000)
GRID_SIZE_HEIGHT = 1000//COLONNE 
GRID_SIZE_WIDTH = 1000//LIGNE 
WIDTH, HEIGHT = COLONNE * GRID_SIZE_HEIGHT , LIGNE * GRID_SIZE_WIDTH
FPS = 30  # Nombre de frames par seconde

# Couleurs
WHITE = (25, 119, 219)
BLACK = (0, 0, 0)
GRID_COLOR = (200, 200, 200)

new_world = World(NBRE_FISH_INITAL, NBRE_SHARK_INITAL)
new_world.placer_les_animaux_initialement()
counter = 0
screen = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Programme Wa Tor par JHG")

# Fonction pour dessiner le quadrillage
def draw_grid():
    for x in range(0, WIDTH+1, GRID_SIZE_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT+1, GRID_SIZE_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))
    
image_path=["requin.jpg", "poisson.jpg"]

images = []
for path in image_path:
    os.path.exists(path)
    images.append(pygame.image.load(path))

# Fonction pour dessiner un objet (par exemple un cercle) dans une cellule
def draw_fish(x, y):
    # Calcul des coordonnées de la cellule
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    screen.blit(pygame.transform.scale(images[1], (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)-10, min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)-10)), (cell_x+GRID_SIZE_HEIGHT//2-(min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)-10)//2, cell_y+5))
    # pygame.draw.circle(screen, (41, 233, 59), (cell_x, cell_y), 10)  # Dessine un cercle rouge
def draw_shark(x, y):
    # Calcul des coordonnées de la cellule
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    screen.blit(pygame.transform.scale(images[0], (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)-10, min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)-10)), (cell_x+GRID_SIZE_HEIGHT//2-min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT)//2, cell_y+5))  # Dessine un cercle rouge

def main():
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)  # Remplir l'écran avec du blanc

        # Dessiner le quadrillage
        draw_grid()
        
        for fish in new_world.list_fishes:
            draw_fish(fish.get_position()[1], fish.get_position()[0])
        for shark in new_world.list_sharks:
            draw_shark(shark.get_position()[1], shark.get_position()[0])
        # Gestion des événements (quitter, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Mettre à jour l'affichage
        clock.tick(FPS)  # Limiter le no
screen.fill(WHITE)  # Remplir l'écran avec du blancmbre de frames par seconde

screen.fill(WHITE)  # Remplir l'écran avec du blanc
couleur_texte = (0, 0, 0)
        # Dessiner le quadrillage
draw_grid()
pygame.font.init()
police = pygame.font.Font(None, 36)

while True:
    time.sleep(0.1)
    screen.fill(WHITE)
    draw_grid()
    if new_world.list_sharks == [] or new_world.list_fishes == []:
        break
    for animal in new_world.list_fishes:
        new_world.scan_cases_autour(animal.get_position())
        new_world.move_and_reproduction(animal)
        animal.incrementation_chronon()
    for animal in new_world.list_sharks:
        new_world.scan_cases_autour(animal.get_position())
        new_world.move_and_reproduction(animal)
        animal.perte_energy()
        animal.incrementation_chronon()
        new_world.check_death_and_kill(animal)
    counter+=1
    clear()
    new_world.grid.print_grid()
    texte = police.render(f"Nb poissons : {len(new_world.list_fishes)}", True, couleur_texte)
    texte2 = police.render(f"Nb requins : {len(new_world.list_sharks)}", True, couleur_texte)
    print(len(new_world.list_fishes))
    print(len(new_world.list_sharks))
    print(counter)
    for animal in new_world.list_fishes:
        draw_fish(animal.get_position()[1], animal.get_position()[0])
    for animal in new_world.list_sharks:
        draw_shark(animal.get_position()[1], animal.get_position()[0])
    screen.blit(texte, (1050,100))
    screen.blit(texte2, (1050,200))
    pygame.display.flip()
