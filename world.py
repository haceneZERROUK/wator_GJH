import random
from fish import Fish
from shark import Shark
import bassin

COLONNE = 50
LIGNE = 50
# def generate_wator_table(col, row):
#     table = []
#     for i in range(col):
#         table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
#     return table


class World:

    def __init__(self, nombre_de_poissons_initial, nombre_de_requins_initial, ligne = LIGNE, colonne = COLONNE):
        self.ligne = ligne
        self.colonne = colonne
        self.grid = bassin.Grid(ligne,colonne)
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
        

    def scan_cases_autour(self, position:tuple):
        scan_eau=[]
        scan_shark=[]
        scan_fish=[]
        directions = [
            ((position[0] - 1) % LIGNE, position[1]), # Haut
            ((position[0] + 1) % LIGNE,position[1]), # Bas
            (position[0],(position[1] - 1) % COLONNE), # Gauche
            (position[0],(position[1] + 1) % COLONNE) # Droite
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
                    (x_poisson_mange,y_poisson_mange) = random.choice(scan_cases[1])
                    if animal.possibilite_reproduction():
                        (x_temporaire,y_temporaire) = animal.get_position()
                        print((x_temporaire,y_temporaire))
                        self.list_fishes.remove(self.grid.get_value((x_poisson_mange,y_poisson_mange)))
                        animal.set_position((x_poisson_mange,y_poisson_mange))
                        new_shark = Shark((x_temporaire,y_temporaire))
                        self.list_sharks.append(new_shark)
                        self.grid.set_value((x_poisson_mange,y_poisson_mange),animal)
                        self.grid.set_value((x_temporaire,y_temporaire), new_shark)
                        animal.reset_indice_reproduction()
                    else:
                        (x_temporaire,y_temporaire) = animal.get_position()
                        self.list_fishes.remove(self.grid.get_value((x_poisson_mange,y_poisson_mange)))
                        animal.set_position((x_poisson_mange,y_poisson_mange))
                        self.grid.set_value((x_poisson_mange,y_poisson_mange), animal)
                        self.grid.set_value((x_temporaire,y_temporaire), 0)
                        animal.incrementation_indice_reproduction()
                elif scan_cases[0]!=[]:
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
                


# if __name__ == "__main__":
#     # Exemple d'utilisation
#     new_world = World(1,1)

#     new_world.placer_les_animaux_initialement()
#     new_world.grid.print_grid()
#     print()
#     # print(new_world.list_fishes[0].position)
#     # print(new_world.list_fishes[0].indice_reproduction)
#     for i in range(30):
#         for animal in new_world.list_fishes:
#             new_world.scan_cases_autour(animal.get_position())
#             new_world.move_and_reproduction(animal)
#             animal.incrementation_indice_reproduction()
#         for animal in new_world.list_sharks:
#             new_world.scan_cases_autour(animal.get_position())
#             new_world.move_and_reproduction(animal)
#             animal.perte_energy()
#             new_world.check_death_and_kill(animal)
#         new_world.grid.print_grid()
#         print()
# print(len(new_world.list_fishes))
# # print(new_world.scan_cases_autour(new_world.list_sharks.position))
# print()
# new_world.grid.print_grid()
# # print(new_world.list_fishes[0].indice_reproduction)
# # new_world.grid.print_grid()

# bbfish=Fish((1,2))
# bbfish.get_position()
# list_fishes=[]
# list_fishes.append(bbfish)
# postion_check_actual = list_fishes[0].get_position()
# print(bbfish.get_position())

#------------------------PARTIE JASON----------------------------

# def scan(self):
#         scan_eau=[]
#         scan_shark=[]
#         scan_fish=[]
#         # x = self.position[0]
#         # y = self.position[1]
#         directions = [
#             [self.position[0] - 1, self.position[0]], # Haut
#             [self.position[0]+1,self.position[1]], # Bas
#             [self.position[0],self.position[1] - 1], # Gauche
#             [self.position[0]+1,self.position[1] + 1] # Droite
#         ]
#         for coord in directions:
#             if world[coord[0]][coord[1]] == 0:
#                 scan_eau.append(coord)
#             elif world[coord[0]][coord[1]] == 1:
#                 scan_fish.append(coord)
#             elif world[coord[0]][coord[1]] == 2:
#                 scan_shark.append(coord)
#         return scan_eau, scan_fish, scan_shark

# eau , poisson ,requin = scan(1,1)
# print(eau)

# class World:
    
#     def __init__(self, titre, chronon, colone, ligne):
#         self.titre = titre
#         self.colone = colone
#         self.ligne = ligne
#         self.chronon = chronon
#         self.world_matrix = generate_wator_table(colone, ligne)
#         self.shark = []
#         self.fish = []

#     def initialiser_world(self, shark=1, fish=2):
#         while shark > 0 or fish > 0:
#             choice_random = random.randint(1, 2)
#             if choice_random == 1 and fish > 0:
#                 fish_generate_col = random.randint(0, self.colone - 1)
#                 fish_generate_line = random.randint(0, self.ligne - 1)
#                 if self.world_matrix[fish_generate_col][fish_generate_line] == 0:
#                     fish -= 1
#                     self.world_matrix[fish_generate_col][fish_generate_line] = 1
                    
#             elif choice_random == 2 and shark > 0:
#                 shark_generate_col = random.randint(0, self.colone - 1)
#                 shark_generate_line = random.randint(0, self.ligne - 1)
#                 if self.world_matrix[shark_generate_col][shark_generate_line] == 0:
#                     shark -= 1
#                     self.world_matrix[shark_generate_col][shark_generate_line] = Shark(([shark_generate_col],[shark_generate_line]))
#     def init_list_fish_and_shark(self):
#         for line in range(self.ligne):
#             for col in range(self.colone):
#                 if self.world_matrix[line][col] == 1:
#                     self.fish.append(Fish((line, col, True)))
#                 elif self.world_matrix[line][col] == 2:
#                     self.shark.append(Shark(line, col, 0, 4, True))
                    
#     def where_is_the_fish(self):
#         return
#     def where_is_the_water(self):
#         return
# if __name__ == "__main__":
#     # Exemple d'utilisation
#     world = World("Mon monde", 1, 3, 3)
#     world.initialiser_world(3,6)
#     for line in world.world_matrix:
#         print(line)
#     print("Autre\n")
#     world.init_list_fish_and_shark()
#     print(f"{world.shark=}")
#     print(f"{world.fish=}")
