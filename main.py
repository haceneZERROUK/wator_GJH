import random
import bassin
from world import World, ROW, COL
import os
import time
import pygame
import sys
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

CONSTANTES = 0
NBRE_FISH_INITAL = 150
NBRE_SHARK_INITAL = 25
chronon_counter = 0
taille_ecran = (1300,1000)
GRID_SIZE_HEIGHT = 1000//COL 
GRID_SIZE_WIDTH = 1000//ROW 
WIDTH, HEIGHT = COL * GRID_SIZE_HEIGHT , ROW * GRID_SIZE_WIDTH
FPS = 30  # Nombre de frames par seconde


GRID_COLOR = (200, 200, 200)
new_world = World(NBRE_FISH_INITAL, NBRE_SHARK_INITAL)
new_world.placer_les_animaux_initialement()
annee = 0
screen = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Programme Wa Tor par JHG")

# Fonction pour dessiner le quadrillage
def draw_grid():
    for x in range(0, WIDTH+1, GRID_SIZE_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT+1, GRID_SIZE_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))
    
image_path=["requin.jpg", "poisson.jpg","aquarium.jpg" ]

images = []
for path in image_path:
    os.path.exists(path)
    images.append(pygame.image.load(path))

# Fonction pour dessiner un objet (par exemple un cercle) dans une cellule
def draw_fish(x, y):
    
    # Calcul des coordonnées de la cellule
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    icon_size = ((min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10) , (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10))
    icon_position= ((cell_x+GRID_SIZE_HEIGHT//2-(min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10)//2, (cell_y + 5)))

    screen.blit(pygame.transform.scale(images[1], (icon_size[0], icon_size[1])), (icon_position[0], icon_position [1]))


def draw_shark(x, y):
    # Calcul des coordonnées de la cellule
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    icon_size = ((min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10) , (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10))
    icon_position= ((cell_x+GRID_SIZE_HEIGHT//2-(min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT) -10)//2, (cell_y + 5)))

    screen.blit(pygame.transform.scale(images[0], (icon_size[0], icon_size[1])), (icon_position[0], icon_position [1]))

def main():
    clock = pygame.time.Clock()

    while True:

        
        
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




couleur_texte = (255, 255, 255)
        # Dessiner le quadrillage
draw_grid()
pygame.font.init()
pygame.mixer.init()

music = pygame.mixer.Sound("song_theme.mp3")
music.play(loops= - 1, maxtime= 0)
police = pygame.font.Font(None, 24)

while True:
    time.sleep(0.5)
    # screen.fill(BLUE)
    screen.blit(images[2], (0,0))
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
    annee+=1
    clear()
    new_world.grid.print_grid()
    texte = police.render(f"Nb poissons : {len(new_world.list_fishes)}", True, couleur_texte)
    texte2 = police.render(f"Nb requins : {len(new_world.list_sharks)}", True, couleur_texte)
    print(len(new_world.list_fishes))
    print(len(new_world.list_sharks))
    print(annee)
    for animal in new_world.list_fishes:
        draw_fish(animal.get_position()[1], animal.get_position()[0])
    for animal in new_world.list_sharks:
        draw_shark(animal.get_position()[1], animal.get_position()[0])



    total_chronon_fish = 0

    for fish in new_world.list_fishes:
        total_chronon_fish += fish.get_chronon()

    total_chronon_shark = 0

    for shark in new_world.list_sharks:
        total_chronon_shark += shark.get_chronon()

    
    mean_age_sharks = int(total_chronon_shark / len(new_world.list_sharks))
    mean_age_fishes = int(total_chronon_fish / len(new_world.list_fishes))

    texte3 = police.render(f"age moyen des poissons:", True, couleur_texte)
    texte5 = police.render(f'{mean_age_fishes}', True, couleur_texte)
    texte4 = police.render(f"age moyen des requins:", True, couleur_texte)
    texte6 = police.render(f'{mean_age_sharks}', True, couleur_texte)


    screen.blit(texte, (1050,100))
    screen.blit(texte2, (1050,150))
    screen.blit(texte3, (1050,200))
    screen.blit(texte5, (1050,225))
    screen.blit(texte4, (1050,250))
    screen.blit(texte6, (1050,275))


    pygame.display.flip()
