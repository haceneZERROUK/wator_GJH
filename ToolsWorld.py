from world import World
from fish import Fish
from shark import Shark
import copy
class ToolsWorld:
    def __init__(self):
        self.name = "ToolsWorld"
        # Valeurs par défaut pour les paramètres facultatifs
        self.default_params = {
            "row": 3,
            "columns": 3
        }

    def create_world(self, number_fish, number_sharks, **kwargs):
        """Crée une instance de World en s'assurant que les paramètres obligatoires sont fournis.
        
        Args:
            number_fish (int): Nombre de poissons initial.
            number_sharks (int): Nombre de requins initial.
            kwargs: Autres arguments facultatifs, avec des valeurs par défaut pour ceux non fournis.
        
        Returns:
            World: Une instance de la classe World initialisée.
        
        Raises:
            ValueError: Si les paramètres obligatoires ne sont pas fournis.
        """
        # Vérification des paramètres obligatoires
        if number_fish is None or number_sharks is None:
            raise ValueError("Les paramètres 'number_fish' et 'number_sharks' sont obligatoires.")

        # Mise à jour des paramètres facultatifs avec les valeurs passées dans kwargs
        params = {**self.default_params, **kwargs}
        
        # Création de l'instance de World avec les paramètres requis et facultatifs
        return World(
            initial_fish_number=number_fish,
            initial_shark_number=number_sharks,
            row=params["row"],
            columns=params["columns"],
        )
    
    def place_animals(self,world):
        world.initial_animal_placing()
        world_copy = copy.deepcopy(world)
        return world_copy
    def area(self,world):
        return world.row * world.columns
    def sum_shark_and_fish(self,world):
        return world.initial_fish_number + world.initial_shark_number
    
    def number_less_than_or_equal_to_the_size_of_the_grid(self,world):
        return self.sum_shark_and_fish(world) <= self.area(world)
    def get_grid_pool(self, world):
        if world.grid is None:
            raise ValueError("Le monde n'a pas été correctement initialisé : l'attribut 'grid' est None.")
        return world.grid.pool
    def search_grid(self,world,focus)-> list[int|object]:
        list_focus = []
        if not isinstance(focus,object):
            for row in self.get_grid_pool(world):
                for col in row:
                    if col == 0:
                        list_focus.append(0)
                    else:
                        ValueError("Valeur étrangére non prévu")
        else:
            for row in self.get_grid_pool(world):
                for col in row:
                    if type(col) == focus:  # noqa: E721
                        list_focus.append(col)
        return list_focus
    def number_sharks_in_grid(self,world):
        return len(self.search_grid(world, Shark))
    def number_fishes_in_grid(self,world):
        return len(self.search_grid(world, Fish))
    
    def get_list_sharks(self, world):
        return world.list_sharks
    def get_list_fishes(self, world):
        return world.list_fishes
    def len_list_sharks(self,world):
        return len(self.get_list_sharks(world))
    def len_list_fishes(self,world):
        return len(self.get_list_fishes(world))
    def get_first_shark(self,world):
        return self.get_list_sharks(world)[0]
    def get_first_fish(self,world):
        return self.get_list_fishes(world)[0]
    def get_chronon_animal(self,animal):
        return animal.get_chronon()
    def is_len_zero_fishes(self,world):
        return self.len_list_fishes(world) == 0
    def is_len_zero_sharks(self, world):
        return self.len_list_sharks(world) == 0
    def is_eq_list_sharks_and_list_grid_sharks(self,world):
        return self.number_sharks_in_grid(world) == self.len_list_sharks(world)
    def is_eq_list_fishes_and_list_grid_fishes(self,world):
        return self.number_fishes_in_grid(world) == self.len_list_fishes(world)
    def is_conform_grid_and_list_animals(self,world):
        return self.is_eq_list_fishes_and_list_grid_fishes(world) and self.is_eq_list_sharks_and_list_grid_sharks(world)

    def get_pos_animal(self,animal):
        return animal.get_position()
    def get_box_around(self,world,position):
        print(f"{world.surrounding_scan(position)=}")
        return world.surrounding_scan(position)
    def scan_box_around_animal(self,world,animal):
        return self.get_box_around(world,self.get_pos_animal(animal))
    def move_animal(self, world, animal):
        world_copy = copy.deepcopy(world)  # Crée une copie indépendante
        world_copy.move_and_reproduction(animal)
        return world_copy

    def move_multiple_animals(self,world,list_animals):
        for animal in list_animals:
            world_copy = self.move_animal(world,animal)
        return world_copy
    def move_first_shark(self,world):
        world_copy = self.move_animal(world,self.get_first_shark(world))
        return world_copy
    def move_first_fish(self,world):
        world_copy = self.move_animal(world,self.get_first_fish(world))
        return world_copy
    def is_mature_animal(self,animal):
        return self.get_chronon_animal(animal) > 0
    def convert_mature_animal(self, animal):
        if not self.is_mature_animal(animal):
            animal.chronon_increment() # Augmente le chronon si l'animal n'est pas mature
        return animal  # Retourne l'animal sans faire de copie
    def check_animal_mature_move(self, world,animal):
        animal_copy = self.convert_mature_animal(animal)
        pos_start = self.get_pos_animal(animal_copy)  # Récupère la position avant le déplacement
        print(f"{pos_start=}")
        self.move_animal(world,animal_copy) # Déplace l'animal original dans le monde
        pos_end = self.get_pos_animal(animal_copy)  # Récupère la position après le déplacement
        print(f"{pos_end=}")
        return pos_start != pos_end  # Compare si la position a changé
    def check_shark_mature_move(self, world):
        return self.check_animal_mature_move(world,self.get_first_shark(world))

    def check_fish_mature_move(self, world):
        return self.check_animal_mature_move(world,self.get_first_fish(world))

if __name__ == "__main__":
    tools = ToolsWorld()
    new_world = tools.create_world(3,3)
    new_world.grid.print_grid()
    new_world = tools.place_animals(new_world)
    print("")
    new_world.grid.print_grid()