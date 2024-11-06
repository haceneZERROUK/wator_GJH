import random
from fish import Fish
from shark import Shark
from bassin import Grid

COL = 50
ROW = 50
# def generate_wator_table(col, row):
#     table = []
#     for i in range(col):
#         table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
#     return table


class World:

    def __init__(self, nombre_de_poissons_initial, nombre_de_requins_initial, row = ROW, columns = COL):
        self.row = row
        self.columns = columns
        self.grid = Grid(row,columns)
        self.list_fishes = []
        self.list_sharks = []
        self.nombre_de_requins_initial = nombre_de_requins_initial
        self.nombre_de_poissons_initial = nombre_de_poissons_initial
    
    def check_death_and_kill(self, shark):
        if shark.energy <= 0:
            self.grid.set_value((shark.position),0)
            self.list_sharks.remove(shark)


    def placer_les_animaux_initialement(self):
        while self.nombre_de_requins_initial > 0 or self.nombre_de_poissons_initial > 0:
            choice_random = random.randint(1, 2)
            generate_col = random.randint(0, self.columns - 1)
            generate_line = random.randint(0, self.row - 1)
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


    def scan_cases_autour(self, position:tuple):
        scan_eau=[]
        scan_shark=[]
        scan_fish=[]
        directions = [
            ((position[0] - 1) % ROW, position[1]), # Haut
            ((position[0] + 1) % ROW,position[1]), # Bas
            (position[0],(position[1] - 1) % COL), # Gauche
            (position[0],(position[1] + 1) % COL) # Droite
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
        if animal.chronon == 0:
            pass
        else:
            scan_cases = self.scan_cases_autour(animal.get_position())
            if isinstance((self.grid.get_value(animal.position)), Shark):
                if scan_cases[1]!= []:
                    animal.eat()
                    (x_eaten_fish,y_fish_eaten) = random.choice(scan_cases[1])
                    if animal.possibilite_reproduction():
                        (x_temporary,y_temporary) = animal.get_position()
                        self.list_fishes.remove(self.grid.get_value((x_eaten_fish,y_fish_eaten)))
                        animal.set_position((x_eaten_fish,y_fish_eaten))
                        new_shark = Shark((x_temporary,y_temporary))
                    
                        self.list_sharks.append(new_shark)
                        self.grid.set_value((x_eaten_fish,y_fish_eaten),animal)
                        self.grid.set_value((x_temporary,y_temporary), new_shark)
                        animal.reset_indice_reproduction()
                    else:
                        (x_temporary,y_temporary) = animal.get_position()
                        self.list_fishes.remove(self.grid.get_value((x_eaten_fish,y_fish_eaten)))
                        animal.set_position((x_eaten_fish,y_fish_eaten))
                        self.grid.set_value((x_eaten_fish,y_fish_eaten), animal)
                        self.grid.set_value((x_temporary,y_temporary), 0)
                        animal.incrementation_indice_reproduction()
                elif scan_cases[0]!=[]:
                    if animal.possibilite_reproduction():
                        (x_temporary,y_temporary) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        new_shark = Shark((x_temporary,y_temporary))
                        self.list_sharks.append(new_shark)
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporary,y_temporary), new_shark)
                        animal.reset_indice_reproduction()
                    else:
                        (x_temporary,y_temporary) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporary,y_temporary), 0)
                        animal.incrementation_indice_reproduction()
            elif isinstance(self.grid.get_value(animal.position), Fish):
                if scan_cases[0]!=[]:
                    if animal.possibilite_reproduction():
                        (x_temporary,y_temporary) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        animal.reset_indice_reproduction()
                        new_fish = Fish((x_temporary,y_temporary))
                        self.list_fishes.append(new_fish)
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporary,y_temporary), new_fish)
                    else:
                        (x_temporary,y_temporary) = animal.get_position()
                        animal.set_position(random.choice(scan_cases[0]))
                        animal.incrementation_indice_reproduction()
                        self.grid.set_value((animal.get_position()), animal)
                        self.grid.set_value((x_temporary,y_temporary), 0)
                
