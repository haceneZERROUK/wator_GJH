import random
from fish import Fish
from shark import Shark
import bassin

COLONNE = 50
LIGNE = 50


class World:

    def __init__(self, nombre_de_poissons_initial, nombre_de_requins_initial, ligne = LIGNE, colonne = COLONNE):
        """
        Initializes the world with a grid and initial populations of fish and sharks.

        Parameters:
            nombre_de_poissons_initial (int): The initial number of fish.
            nombre_de_requins_initial (int): The initial number of sharks.
            ligne (int, optional): The number of rows in the grid. Default is `LIGNE`.
            colonne (int, optional): The number of columns in the grid. Default is `COLONNE`.
        """        
        self.ligne = ligne
        self.colonne = colonne
        self.grid = bassin.Grid(ligne,colonne)
        self.list_fishes = []
        self.list_sharks = []
        self.nombre_de_requins_initial = nombre_de_requins_initial
        self.nombre_de_poissons_initial = nombre_de_poissons_initial
    
    def check_death_and_kill(self, shark):
        """
        Checks if the shark's energy is zero or less and removes it from the grid and list.

        If the shark's energy is non-positive, it sets its position in the grid to 0 and removes the shark 
        from the `list_sharks`.

        Parameters:
            shark (Shark): The shark object to check and potentially remove.

        Returns:
            None
        """
        if shark.energy <= 0:
            self.grid.set_value((shark.position),0)
            self.list_sharks.remove(shark)


    def placer_les_animaux_initialement(self):
        """
        Places the initial animals (fish and sharks) randomly on the grid.

        The method randomly selects positions on the grid to place the initial number of fish and sharks. 
        It continues until all fish and sharks are placed. Fish are represented by `Fish` objects, and sharks by `Shark` objects.

        Returns:
            None
        """
        while self.nombre_de_requins_initial > 0 or self.nombre_de_poissons_initial > 0: # Continue placing sharks and fish until all have been placed
            choice_random = random.randint(1, 2) # 1 is for fish, 2 for sharks
            generate_col = random.randint(0, self.colonne - 1)
            generate_line = random.randint(0, self.ligne - 1)
            if choice_random == 1 and self.nombre_de_poissons_initial > 0:
                if self.grid.get_value((generate_line,generate_col)) == 0:
                    self.nombre_de_poissons_initial -= 1
                    new_fish = Fish((generate_line,generate_col))
                    self.grid.set_value((generate_line,generate_col), new_fish)
                    self.list_fishes.append(new_fish)           
            elif choice_random == 2 and self.nombre_de_requins_initial > 0:
                if self.grid.get_value((generate_line,generate_col)) == 0:
                    self.nombre_de_requins_initial -= 1
                    new_shark = Shark((generate_line,generate_col))
                    self.grid.set_value((generate_line,generate_col), new_shark)
                    self.list_sharks.append(new_shark)
        

    def scan_cases_autour(self, position:tuple) -> list:
        """
        Scans the surrounding cells of a given position on the grid.

        The method checks the four adjacent cells (up, down, left, right) around the given position and categorizes them 
        into empty cells (`0`), cells containing sharks, or cells containing fish.

        Parameters:
            position (tuple): A tuple (row, column) representing the current position to scan.

        Returns:
            list: A list containing three sub-lists:
                - `scan_eau`: List of empty cells (water).
                - `scan_fish`: List of cells containing fish.
                - `scan_shark`: List of cells containing sharks.
        """
        scan_eau=[]
        scan_shark=[]
        scan_fish=[]
        directions = [
            ((position[0] - 1) % LIGNE, position[1]), # Up
            ((position[0] + 1) % LIGNE,position[1]), # Down
            (position[0],(position[1] - 1) % COLONNE), # Left
            (position[0],(position[1] + 1) % COLONNE) # Right
        ]
        for coord in directions:
            if self.grid.get_value(coord) == 0:
                scan_eau.append(coord)
            elif isinstance(self.grid.get_value(coord), Shark):
                scan_shark.append(coord)
            elif isinstance(self.grid.get_value(coord), Fish):
                scan_fish.append(coord)
        return [scan_eau, scan_fish, scan_shark]


    def move_and_reproduction(self, animal):
        """
        Moves an animal and handles its reproduction or eating behavior.

        If the animal is a shark, it may eat a fish if nearby or move to an empty cell. 
        If the shark can reproduce, a new shark is created. Similarly, if the animal is a fish, 
        it may move to an empty cell and reproduce or just move.

        Parameters:
            animal (Fish or Shark): The animal to move and potentially reproduce.

        Returns:
            None
        """
        if animal.chronon == 0: # to avoid that new fishes move
            pass
        else:
            scan_cases = self.scan_cases_autour(animal.get_position())
            if isinstance((self.grid.get_value(animal.position)), Shark): #check if animal is a shark
                if scan_cases[1]!= []: # check if around the shark there is at least one fish
                    animal.eat() 
                    (x_poisson_mange,y_poisson_mange) = random.choice(scan_cases[1]) # creates a tuple with the position chosen by a random choice where the shark will go
                    if animal.possibilite_reproduction(): # check if shark can reproduce
                        (x_temporaire,y_temporaire) = animal.get_position() #creates a tuple with the current position of the shark
                        self.list_fishes.remove(self.grid.get_value((x_poisson_mange,y_poisson_mange))) # removes the fish that is going to be eaten
                        animal.set_position((x_poisson_mange,y_poisson_mange)) # moves the shark to its new position
                        new_shark = Shark((x_temporaire,y_temporaire)) # creates a new shark to the previous position of the shark
                        self.list_sharks.append(new_shark) # appends the new shark to the shark list
                        self.grid.set_value((x_poisson_mange,y_poisson_mange),animal) # updates the values in the grid
                        self.grid.set_value((x_temporaire,y_temporaire), new_shark) 
                        animal.reset_indice_reproduction()
                    else:
                        (x_temporaire,y_temporaire) = animal.get_position()
                        self.list_fishes.remove(self.grid.get_value((x_poisson_mange,y_poisson_mange)))
                        animal.set_position((x_poisson_mange,y_poisson_mange))
                        self.grid.set_value((x_poisson_mange,y_poisson_mange), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), 0)
                        animal.incrementation_indice_reproduction()
                elif scan_cases[0]!=[]: # else if there is no fish around but an empty position
                    if animal.possibilite_reproduction():
                        (x_temporaire,y_temporaire) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        new_shark = Shark((x_temporaire,y_temporaire))
                        self.list_sharks.append(new_shark)
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), new_shark)
                        animal.reset_indice_reproduction()
                    else:
                        (x_temporaire,y_temporaire) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), 0)
                        animal.incrementation_indice_reproduction()
            elif isinstance(self.grid.get_value(animal.position), Fish):
                if scan_cases[0]!=[]:
                    if animal.possibilite_reproduction():
                        (x_temporaire,y_temporaire) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        animal.reset_indice_reproduction()
                        new_fish = Fish((x_temporaire,y_temporaire))
                        self.list_fishes.append(new_fish)
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), new_fish)
                    else:
                        (x_temporaire,y_temporaire) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        animal.incrementation_indice_reproduction()
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), 0)
                
