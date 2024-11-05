from world import World
class TestInstanceWorld:
    def __init__(self,world_instance,world_class):
        self.world_instance = world_instance
        self.world_class = world_class
        self.list_exception = ("world_class","print_all_methode_result")
        self.list_filter_execpt = ("__","_TestInstanceWorld__")
    
    def get_number_sharks(self): # passe
        return self.world_instance.nombre_de_requins_initial
    def get_number_fish(self): # passe
        return self.world_instance.nombre_de_poissons_initial
    def get_ligne(self): # passe
        return self.world_instance.ligne
    def get_colonne(self): # passe
        return self.world_instance.colonne
    def area(self): # passe
        return self.get_ligne() * self.get_colonne()
    def sum_fish_and_shark(self): # passe
        return self.get_number_fish() + self.get_number_sharks()
    
    def is_inferior_or_equal_grid_sum_shark_and_fish(self): # passe
        return self.sum_fish_and_shark() <= self.area()
    
    def is_not_full_area_shark(self): # passe
        return self.get_number_sharks() < self.area()
    def is_not_full_area_fish(self): #passe
        return self.get_number_fish() < self.area()
    
    def print_all_methode_result(self):
        for method in self.__get_method():
            func = getattr(self, method)
            if method not in self.list_exception:
                print(f"{method=}")
                print(f"Résultat de {method}: {func()}")
    
        
    def __get_method(self):
        # ma_liste = []
        # for method in TestInstanceWorld.__dict__.keys():
        #     if '__' not in method:
        #         ma_liste.append(method)          
        return [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith(self.list_filter_execpt)]
    




LIGNE = 10
COLONNE = 10
NOMBRE_REQUIN = 50
NOMBRE_POISSON = 50
REQUIN_ENERGY = 8
REPRODUCTION_REQUIN = 13
REPRODUCTION_FISH = 2

new_world = World(NOMBRE_POISSON,NOMBRE_REQUIN,ligne = LIGNE,colonne = COLONNE,requin_energy = REQUIN_ENERGY,reproduction_shark = REPRODUCTION_REQUIN,reproduction_fish = REPRODUCTION_FISH)
test_world = TestInstanceWorld(new_world,World)
test_world.print_all_methode_result()

class TestClassWorld:
    def __init__(self,world_class:World):
        self.world_class = world_class
        self.list_filter_except = ('__','_TestClassWorld__')
        
    def __get_method(self):  
        return [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith(self.list_filter_except)]
    
    def generator_small_grid_one_shark(self):
        number_row = 3
        number_col = 3
        number_sharks = 1
        number_fish = 0
        energy_shark = 8
        reproduction_shark = 13
        reproduction_fish = 2
        return self.world_class(nombre_de_poissons_initial = number_fish,
                                nombre_de_requins_initial=number_sharks,
                                requin_energy=energy_shark,
                                reproduction_shark=reproduction_shark,
                                reproduction_fish = reproduction_fish,
                                ligne = number_row,
                                colonne = number_col)
    def generator_small_grid_one_fish(self):
        number_row = 3
        number_col = 3
        number_sharks = 0
        number_fish = 1
        energy_shark = 8
        reproduction_shark = 13
        reproduction_fish = 2
        return self.world_class(nombre_de_poissons_initial = number_fish,
                                nombre_de_requins_initial=number_sharks,
                                requin_energy=energy_shark,
                                reproduction_shark=reproduction_shark,
                                reproduction_fish = reproduction_fish,
                                ligne = number_row,
                                colonne = number_col)
    def generator_small_grid_one_shark_and_one_fish(self):
        number_row = 3
        number_col = 3
        number_sharks = 1
        number_fish = 1
        energy_shark = 8
        reproduction_shark = 13
        reproduction_fish = 2
        return self.world_class(nombre_de_poissons_initial = number_fish,
                                nombre_de_requins_initial=number_sharks,
                                requin_energy=energy_shark,
                                reproduction_shark=reproduction_shark,
                                reproduction_fish = reproduction_fish,
                                ligne = number_row,
                                colonne = number_col)
    def get_grid_one_shark_one_fish(self):
        return self.generator_small_grid_one_shark_and_one_fish().grid

test_class_world = TestClassWorld(World)
test_class_world.get_grid_one_shark_one_fish().print_grid()