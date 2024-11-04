import random
import bassin
from world import World
import os
import time
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

CONSTANTES = 0

NBRE_FISH_INITAL = 70
NBRE_SHARK_INITAL = 30



new_world = World(NBRE_FISH_INITAL, NBRE_SHARK_INITAL)
new_world.placer_les_animaux_initialement()
new_world.grid.print_grid()
print()

while True:

    time.sleep(0.3)
    

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
    clear()
    new_world.grid.print_grid()
    print(len(new_world.list_fishes))
    print(len(new_world.list_sharks))
    print()
