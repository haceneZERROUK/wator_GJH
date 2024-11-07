import random
import pool
from world import World, ROW, COL
import os
import time
import pygame
import sys
clear = lambda: os.system("cls" if os.name == "nt" else "clear")


INITIAL_FISH_NUMBER = 500
INITIAL_SHARK_NUMBER = 250
SCREEN_SIZE = (1300,1000)
GRID_SIZE_HEIGHT = 1000//COL 
GRID_SIZE_WIDTH = 1000//ROW 
WIDTH, HEIGHT = COL * GRID_SIZE_HEIGHT , ROW * GRID_SIZE_WIDTH
FPS = 30  


GRID_COLOR = (200, 200, 200)
new_world = World(INITIAL_FISH_NUMBER, INITIAL_SHARK_NUMBER)
new_world.initial_animal_placing()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Programme Wa Tor par JHG")

# Grid drawing function
def draw_grid():
    """
    Draws a grid on the screen with vertical and horizontal lines.

    The grid lines are spaced according to GRID_SIZE_HEIGHT (for vertical lines)
    and GRID_SIZE_WIDTH (for horizontal lines), and are drawn using GRID_COLOR.

    Assumes the existence of the following constants:
        - WIDTH, HEIGHT: Screen dimensions.
        - GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH: Grid line spacing.
        - GRID_COLOR: Color of the grid lines.
        - screen: The pygame surface to draw on.

    Returns:
        None
    """
    for x in range(0, WIDTH+1, GRID_SIZE_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT+1, GRID_SIZE_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))
    
image_path=["requin.jpg", "poisson.jpg","aquarium.jpg" ]

images = []
for path in image_path:
    os.path.exists(path)
    images.append(pygame.image.load(path))


def draw_fish(x, y):
    """
    Draws a scaled fish icon at the specified grid position (x, y).

    The fish icon is scaled to fit within the grid cell, with a small margin.
    The icon is then drawn on the screen at the calculated position.

    Args:
        x (int): The horizontal grid position.
        y (int): The vertical grid position.

    Assumes the existence of the following:
        - GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH: Grid cell dimensions.
        - images[1]: The fish icon image.
        - screen: The pygame surface to draw on.

    Returns:
        None
    """
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    min_case = (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT))

    icon_size = (min_case * 0.9 , min_case * 0.9)
    icon_position= ((cell_x+(GRID_SIZE_HEIGHT-min_case *0.9)//2), (cell_y + 0.05 * GRID_SIZE_WIDTH))

    screen.blit(pygame.transform.scale(images[1], (icon_size[0], icon_size[1])), (icon_position[0], icon_position [1]))


def draw_shark(x, y):
    """
    Draws a scaled shark icon at the specified grid position (x, y).

    The shark icon is scaled to fit within the grid cell, with a small margin.
    The icon is then drawn on the screen at the calculated position.

    Args:
        x (int): The horizontal grid position.
        y (int): The vertical grid position.

    Assumes the existence of the following:
        - GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH: Grid cell dimensions.
        - images[0]: The shark icon image.
        - screen: The pygame surface to draw on.

    Returns:
        None
    """
    cell_x = x * GRID_SIZE_HEIGHT
    cell_y = y * GRID_SIZE_WIDTH
    min_case = (min(GRID_SIZE_WIDTH,GRID_SIZE_HEIGHT))

    icon_size = (min_case * 0.9 , min_case * 0.9)
    icon_position= ((cell_x+(GRID_SIZE_HEIGHT-min_case *0.9)//2), (cell_y + 0.05 * GRID_SIZE_WIDTH))

    screen.blit(pygame.transform.scale(images[0], (icon_size[0], icon_size[1])), (icon_position[0], icon_position [1]))

text_color = (255, 255, 255)

draw_grid()
pygame.font.init()
pygame.mixer.init()

music = pygame.mixer.Sound("song_theme.mp3")
music.play(loops= - 1, maxtime= 0)
police = pygame.font.Font(None, 24)



while True:
    time.sleep(0.1)
    screen.blit(images[2], (0,0))
    draw_grid()
    if new_world.list_sharks == [] or new_world.list_fishes == []:
        break
    for animal in new_world.list_fishes:
        new_world.surrounding_scan(animal.get_position())
        new_world.move_and_reproduction(animal)
        animal.chronon_increment()
    for animal in new_world.list_sharks:
        new_world.surrounding_scan(animal.get_position())
        new_world.move_and_reproduction(animal)
        animal.energy_loss()
        animal.chronon_increment()
        new_world.check_death_and_kill(animal)
    clear()
    new_world.grid.print_grid()

    fish_number = police.render(f"Fish number : {len(new_world.list_fishes)}", True, text_color)
    shark_number = police.render(f"Shark number : {len(new_world.list_sharks)}", True, text_color)
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

    if len(new_world.list_fishes) == 0 or len(new_world.list_sharks) == 0:
        print("UNE ESPECE S'EST ETEINTE")


        
    else:

        mean_age_sharks = int(total_chronon_shark / len(new_world.list_sharks))
        mean_age_fishes = int(total_chronon_fish / len(new_world.list_fishes))

        average_fish_age_display = police.render(f"Average fish age:", True, text_color)
        average_fish_age_var_display = police.render(f'{mean_age_fishes}', True, text_color)
        average_shark_age_display = police.render(f"Average shark age:", True, text_color)
        average_shar_age_var_display = police.render(f'{mean_age_sharks}', True, text_color)


        screen.blit(fish_number, (1050,100))
        screen.blit(shark_number, (1050,150))
        screen.blit(average_fish_age_display, (1050,200))
        screen.blit(average_fish_age_var_display, (1050,225))
        screen.blit(average_shark_age_display, (1050,250))
        screen.blit(average_shar_age_var_display, (1050,275))


        pygame.display.flip()
# Quitter Pygame
pygame.quit()
sys.exit()


