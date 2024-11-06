from world import World
from Test_Standard import TestRunner
from fish import Fish
from shark import Shark
class ToolsTest:
    def __init__(self):
        self.result = None

    def is_eq(self, arg1, arg2):
        return arg1 == arg2

    def is_eqs(self, *args):
        if len(args) < 2:
            raise ValueError("Le nombre d'arguments doit être au moins 2")
        return all(self.is_eq(args[i], args[i + 1]) for i in range(len(args) - 1))

class ToolsWorld:
    def __init__(self):
        self.name = "ToolsWorld"
        # Valeurs par défaut pour les paramètres facultatifs
        self.default_params = {
            "ligne": 3,
            "colonne": 3,
            "requin_energy": 8,
            "reproduction_fish": 2,
            "reproduction_shark": 13,
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
            nombre_de_poissons_initial=number_fish,
            nombre_de_requins_initial=number_sharks,
            ligne=params["ligne"],
            colonne=params["colonne"],
            requin_energy=params["requin_energy"],
            reproduction_fish=params["reproduction_fish"],
            reproduction_shark=params["reproduction_shark"]
        )
    
    def place_animals(self,world):
        return world.placer_les_animaux_initialement()
    def area(self,world):
        return world.ligne * world.colonne
    def sum_shark_and_fish(self,world):
        return world.nombre_de_poissons_initial + world.nombre_de_requins_initial
    
    def number_less_than_or_equal_to_the_size_of_the_grid(self,world):
        return self.sum_shark_and_fish(world) <= self.area(world)
    def get_grid_bassin(self, world):
        if world.grid is None:
            raise ValueError("Le monde n'a pas été correctement initialisé : l'attribut 'grid' est None.")
        return world.grid.bassin
    def search_grid(self,world,focus)-> list[int|object]:
        list_focus = []
        if not isinstance(focus,object):
            for raw in self.get_grid_bassin(world):
                for col in raw:
                    if col == 0:
                        list_focus.append(0)
                    else:
                        ValueError("Valeur étrangére non prévu")
        else:
            for raw in self.get_grid_bassin(world):
                for col in raw:
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
    def move_shark(self,world):
        return world.move_and_reproduction(self.get_first_shark(world))
    def get_pos_animal(self,world,animal):
        return animal
    def move_animals(self,world,animal):
        pos_start = self.animal(world).get_position()
        world = self.move_shark(world)
        pos_end = self.get_first_shark(world).get_position()
    def check_shark_move(self,world):
        pos_start = self.get_first_shark(world).get_position()
        world = self.move_shark(world)
        pos_end = self.get_first_shark(world).get_position()
        return pos_start != pos_end
    
    
    

tool_test = ToolsTest()

class TestWorld:
    def __init__(self):
        self.name = "TestWorld"
        self.world = None
        self.tools = ToolsWorld()

    def test_create_world_with_required_params(self):
        # Test avec paramètres obligatoires et facultatifs personnalisés
        self.world = self.tools.create_world(
            3, 3,
            ligne=5,
            colonne=5,
            requin_energy=7
        )
        return isinstance(self.world, World) and \
               tool_test.is_eqs(self.world.ligne, 5) and \
               tool_test.is_eqs(self.world.requin_energy, 7)

    def test_create_world_with_defaults(self):
        # Test avec seulement les paramètres obligatoires, vérification des valeurs par défaut
        self.world = self.tools.create_world(5, 10)
        return isinstance(self.world, World) and \
               tool_test.is_eqs(self.world.ligne, self.tools.default_params["ligne"]) and \
               tool_test.is_eqs(self.world.colonne, self.tools.default_params["colonne"])

    def test_create_world_missing_required(self):
        # Test sans les paramètres obligatoires pour vérifier l'exception
        try:
            self.world = self.tools.create_world(number_sharks=5)  # Manque number_fish
        except TypeError:
            return True
        return False

    


print()
# print(f"{tool_test.is_eq(1,2)=}\n{tool_test.is_eq(2,2)=}\n")
#print(f"{tool_test.is_eqs(1,2)=}\n{tool_test.is_eqs(2,2)=}\n{tool_test.is_eqs(1,2,2)=}\n{tool_test.is_eqs(2,2,2)=}\n")


    
    
Test = TestRunner([TestWorld])
Test.run()
tool_test = ToolsTest()
tools_world = ToolsWorld()
new_worlds = tools_world.create_world(3,1,ligne = 3, colonne = 3)
tools_world.place_animals(new_worlds)
print(f"{tools_world.search_grid(new_worlds,Shark)}")
print(f"{tools_world.search_grid(new_worlds,Fish)}")
# print(f"{tools_world.area(new_worlds)=} {tools_world.get_grid_bassin(new_worlds)=}")