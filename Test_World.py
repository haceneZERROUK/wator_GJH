from world import World
from Test_Standard import TestRunner

# -------------------- Constantes de Configuration --------------------
LIGNE = 10
COLONNE = 10
NOMBRE_REQUIN = 50
NOMBRE_POISSON = 50
REQUIN_ENERGY = 8
REPRODUCTION_REQUIN = 13
REPRODUCTION_FISH = 2

# -------------------- Classe Parent: BaseTestWorld --------------------
class BaseToolsTestWorld:
    """Classe de base pour les classes de test, offrant des méthodes communes."""

    def __init__(self):
        self.list_exception = ("world_class", "print_all_methode_result")
        self.list_filter_except = ("_","__", "_BaseTestWorld__", "_TestClassWorld__", "_TestInstanceWorld__")

    # --- Méthodes utilitaires pour récupérer les méthodes filtrées ---
    def __get_method(self):
        return [
            method for method in dir(self)
            if callable(getattr(self, method)) and not method.startswith(self.list_filter_except)
        ]

    # --- Méthode d'affichage des résultats de méthodes de test ---
    def print_all_methode_result(self):
        for method in self.__get_method():
            if method not in self.list_exception:
                func = getattr(self, method)
                print(f"{method=}")
                print(f"Résultat de {method}: {func()}")

    # --- Getters pour accéder aux attributs de World ---
    def _get_number_sharks(self,new_world):
        return new_world.nombre_de_requins_initial

    def _get_number_fish(self,new_world):
        return new_world.nombre_de_poissons_initial

    def _get_ligne(self,new_world):
        return new_world.ligne

    def _get_colonne(self,new_world):
        return new_world.colonne



# -------------------- Classe de Test: TestInstanceWorld --------------------
# -------------------- Classe de Test: TestInstanceWorld --------------------
class ToolsTestInstanceWorld(BaseToolsTestWorld):
    """Classe pour tester les attributs et fonctions d'une instance de World."""

    def __init__(self, world_instance, world_class):
        super().__init__()
        self.world = world_instance
        self.world_class = world_class

    def test_area(self):
        """Test pour vérifier que l'aire est correcte."""
        expected_area = self._get_ligne(self.world) * self._get_colonne(self.world)
        return self.area() == expected_area

    def test_sum_fish_and_shark(self):
        """Test pour vérifier la somme des poissons et requins."""
        return self.sum_fish_and_shark() == (self._get_number_fish(self.world) + self._get_number_sharks(self.world))

    def test_is_inferior_or_equal_grid_sum_shark_and_fish(self):
        """Vérifie que la somme des poissons et requins est inférieure ou égale à l'aire."""
        return self.is_inferior_or_equal_grid_sum_shark_and_fish()

# -------------------- Classe de Test: TestClassWorld --------------------
class ToolsTestClassWorld(BaseToolsTestWorld):
    """Classe pour tester la création et configuration d'instances de World."""

    def __init__(self, world_class: World):
        super().__init__()
        self.world_class = world_class
        self.world = None

    def test_generate_init_world(self):
        """Test pour générer une instance de World et vérifier ses attributs."""
        world = self._generate_init_world(rows=10, cols=10, sharks=5, fish=5)
        return (world.nombre_de_requins_initial == 5 and 
                world.nombre_de_poissons_initial == 5 and 
                world.ligne == 10 and 
                world.colonne == 10)

# -------------------- Exécution des Tests --------------------
class TestInstanceWorld:
        def __init__(self):
            # Valeurs par défaut pour la configuration du monde
            self.default_ligne = 3
            self.default_colonne = 3
            self.default_energy_shark = 8
            self.default_number_fish = 5
            self.default_number_shark = 4
            self.default_reproduction_fish = 2
            self.default_reproduction_shark = 13
            self.new_world = None  # L'instance sera créée dans le test

        def test_init_new_world(self):
            """Initialisation de new_world avec les valeurs par défaut et vérification des attributs."""
            self.new_world = World(
                nombre_de_poissons_initial=self.default_number_fish,
                nombre_de_requins_initial=self.default_number_shark,
                ligne=self.default_ligne,
                colonne=self.default_colonne,
                requin_energy=self.default_energy_shark,
                reproduction_fish=self.default_reproduction_fish,
                reproduction_shark=self.default_reproduction_shark
            )
            if self.new_world is not None:
                if self.new_world.colonne != self.default_colonne:
                    raise Exception(f"{self.new_world.colonne=} != {self.default_colonne}")
                if self.new_world.ligne != self.default_ligne:
                    raise Exception(f"{self.new_world.ligne=} != {self.default_ligne}")
                if self.new_world.nombre_de_poissons_initial != self.default_number_fish:
                    raise Exception(f"{self.new_world.nombre_de_poissons_initial} != {self.default_number_fish}")
                

        def test_area(self):
            """Vérifie que la surface de la grille est correcte."""
            expected_area = self.default_ligne * self.default_colonne
            assert self.new_world.ligne * self.new_world.colonne == expected_area, f"Erreur : Surface attendue {expected_area}, obtenue {self.new_world.ligne * self.new_world.colonne}"
            print("test_area réussi.")

        def test_population_within_grid_limits(self):
            """Vérifie que la population totale de poissons et de requins n'excède pas la taille de la grille."""
            total_animals = self.new_world.nombre_de_poissons_initial + self.new_world.nombre_de_requins_initial
            max_capacity = self.default_ligne * self.default_colonne
            assert total_animals <= max_capacity, f"Erreur : {total_animals} animaux pour une grille de capacité {max_capacity}"
            print("test_population_within_grid_limits réussi.")

        def test_energy_levels(self):
            """Vérifie que l'énergie des requins est correctement initialisée."""
            assert self.new_world.requin_energy == self.default_energy_shark, f"Erreur : Énergie requin attendue {self.default_energy_shark}, obtenue {self.new_world.requin_energy}"
            print("test_energy_levels réussi.")

        def run_all_tests(self):
            """Méthode pour exécuter tous les tests de la classe."""
            self.test_init_new_world()
            self.test_area()
            self.test_population_within_grid_limits()
            self.test_energy_levels()
            print("Tous les tests de TestInstanceWorld ont réussi.")
            
        
# Utilisation de TestRunner
runner = TestRunner([TestInstanceWorld])  # Passer les classes de test
runner.run(debug=True)  # Exécute les tests avec le mode débogage activé