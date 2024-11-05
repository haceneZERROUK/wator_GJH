
from fish import Fish
from shark import Shark
from world import World
from world import COLONNE, LIGNE
from bassin import Grid
# from main import new_world


import pygame
import sys


# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
GRID_SIZE = 40 
WIDTH, HEIGHT = COLONNE * GRID_SIZE , LIGNE * GRID_SIZE
NB_REQUIN_INI = 5
NB_POISSON_INI = 10
FPS = 30  # Nombre de frames par seconde

# Couleurs
WHITE = (0, 0, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
GREEN = (0,255,0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projet Wator GJH en colloboration avec Simplon")

# Fonction pour dessiner le quadrillage
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

# Fonction pour dessiner un objet (par exemple un cercle) dans une cellule
def draw_shrk(x, y):
    # Calcul des coordonnées de la cellule
    cell_x = x * GRID_SIZE + GRID_SIZE // 2
    cell_y = y * GRID_SIZE + GRID_SIZE // 2
    pygame.draw.circle(screen, (255, 0, 0), (cell_x, cell_y), 10)  # Dessine un cercle rouge

# Boucle principale du jeu
def main():
    clock = pygame.time.Clock()
    new_world = World(NB_POISSON_INI, NB_POISSON_INI)
    new_world.placer_les_animaux_initialement()


    print (new_world.list_fishes)

    while True:
        screen.fill(WHITE)  # Remplir l'écran avec du blanc

        # Dessiner le quadrillage
  
        # Exemple : dessiner des objets dans certaines cellules du quadrillage
        # draw_object(3, 2)  # Un objet dans la cellule (3, 2)
        # draw_object(0, 4)  # Un autre objet dans la cellule (5, 4)



        for fish in new_world.list_fishes:
            draw_object(fish.get_position()[0], fish.get_position()[1])
        # Gestion des événements (quitter, etc.)
        draw_grid()
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Mettre à jour l'affichage
        clock.tick(FPS)  # Limiter le nombre de frames par seconde

# Exécution du programme
if __name__ == "__main__":
    main()

