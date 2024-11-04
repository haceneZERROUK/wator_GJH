
from world import World



CONSTANTES = 0
REFRESH_RATE = 10
NBRE_FISH_INITAL = 2
NBRE_SHARK_INITAL = 2
COLONNE = 3
LIGNE = 3
chronon_counter = 0


new_world = World(NBRE_FISH_INITAL, NBRE_SHARK_INITAL)
new_world.placer_les_animaux_initialement()

while True:
    if chronon_counter == REFRESH_RATE:
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
        new_world.grid.print_grid()
        print()
        chronon_counter = 0
    else:
        chronon_counter +=1