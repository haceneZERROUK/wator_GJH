import random
from fish import Fish
from shark import Shark
import bassin

COLONNE = 10
LIGNE = 10
# def generate_wator_table(col, row):
#     table = []
#     for i in range(col):
#         table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
#     return table


class World:
    LIGNE = 3
    COLONNE = 3
    def __init__(self, nombre_de_poissons_initial, nombre_de_requins_initial, ligne = LIGNE, colonne = COLONNE):
        self.ligne = ligne
        self.colonne = colonne
        self.grid = bassin.Grid(ligne,colonne)
        self.list_fishes = []
        self.list_sharks = []
        self.nombre_de_requins_initial = nombre_de_requins_initial
        self.nombre_de_poissons_initial = nombre_de_poissons_initial
    
    def placer_les_animaux_initialement(self):
        while self.nombre_de_requins_initial > 0 or self.nombre_de_poissons_initial > 0:
            choice_random = random.randint(1, 2)
            generate_col = random.randint(0, self.colonne - 1)
            generate_line = random.randint(0, self.ligne - 1)
            if choice_random == 1 and Fish > 0:
                if self.grid.get_value((generate_col,generate_line)) == 0:
                    self.nombre_de_poissons_initial -= 1
                    new_fish = Fish((generate_col,generate_line))
                    self.grid.set_value((generate_col,generate_line), new_fish)
                    self.list_fishes.append(new_fish)
                    
            elif choice_random == 2 and self.nombre_de_requins_initial > 0:
                if self.grid.get_value((generate_col,generate_line)) == 0:
                    self.nombre_de_requins_initial -= 1
                    new_shark = Shark((generate_col,generate_line))
                    self.grid.set_value((generate_col,generate_line), new_shark)
                    self.list_sharks.append(new_shark)
        

    def scan_cases_autour(self, position:tuple):
        scan_eau=[]
        scan_shark=[]
        scan_fish=[]
        directions = [
            [(position[0] - 1) % LIGNE, position[0]], # Haut
            [(position[0] + 1) % LIGNE,position[1]], # Bas
            [position[0],(position[1] - 1) % COLONNE], # Gauche
            [position[0],(position[1] + 1) % COLONNE] # Droite
        ]
        for coord in directions:
            if self.grid[coord[0]][coord[1]] == 0:
                scan_eau.append(coord)
            elif isinstance(self.grid[coord[0]][coord[1]], Fish):
                scan_fish.append(coord)
            elif isinstance(self.grid[coord[0]][coord[1]], Shark):
                scan_shark.append(coord)
        return [scan_eau, scan_fish, scan_shark]

    scan_cases = scan_cases_autour()

    def move_and_reproduction(self,scan_cases):
        self.list_fishes = [Fish(0.1), Fish(1,2)]
        for fish in self.list_fishes:
            postion_check_actual = self.fish.get_position()
            self.scan_cases()
            if isinstance((self.grid.get_value(fish.position), Fish)):
                if scan_cases[0]!=[]:
                    if Fish.possibilite_reproduction():
                        x_temporaire,y_temporaire = self.grid[0], self.grid[1]
                        fish.set_position(random.choice(scan_cases[0]))
                        Fish.reset_indice_reproduction()
                        new_fish = Fish(x_temporaire,y_temporaire)
                        liste_fish.append(new_fish)
                        grid.set_position(fish, self.grid[0], self.grid[1])
                        grid.set_position(new_fish, x_temporaire,y_temporaire)
                    else:
                        fish.set_position(random.choice(scan_cases[1]))
                        fish.incrementation_indice_reproduction()
                        grid.set_position(fish,self.grid[0], self.grid[1])
            elif isinstance((self.grid[0], self.grid[1]), Shark):
                if scan_cases[1]!= []:
                    shark.eat()
                    (x_poisson_mange,y_poisson_mange) = random.choice(scan_cases[1])
                    if shark.possibilite_reproduction():
                        x_temporaire,y_temporaire = self.grid[0], self.grid[1]
                        liste_fish = [fish for fish in liste_fish if fish.position != (x_poisson_mange,y_poisson_mange)]
                        shark.set_position(x_poisson_mange,y_poisson_mange)
                        new_shark = Shark(x_temporaire,y_temporaire)
                        list_shark.append(new_shark)
                        grid.set_position(shark, self.grid[0], self.grid[1])
                        grid.set_position(new_shark, x_temporaire,y_temporaire)
                        shark.reset_indice_reproduction()
                    else:
                        x_temporaire,y_temporaire = self.grid[0], self.grid[1]
                        liste_fish = [fish for fish in liste_fish if fish.position != (x_poisson_mange,y_poisson_mange)]
                        shark.set_position(x_poisson_mange,y_poisson_mange)
                        grid.set_position(shark, x_poisson_mange,y_poisson_mange)
                        grid.set_position(0, x_temporaire,y_temporaire)
                elif scan_cases[0]!=[]:
                    if shark.possibilite_reproduction():
                        x_temporaire,y_temporaire = self.grid[0], self.grid[1]
                        shark.set_position(random.choice(scan_cases[1]))
                        new_shark = Shark(x_temporaire,y_temporaire)
                        list_shark.append(new_shark)
                        grid.set_position(shark, self.grid[0], self.grid[1])
                        grid.set_position(new_shark, x_temporaire,y_temporaire)
                        shark.reset_indice_reproduction()
                    else:
                        x_temporaire,y_temporaire = self.grid[0], self.grid[1]
                        shark.set_position(random.choice(scan_cases[1]))
                        grid.set_position(shark, self.grid[0], self.grid[1])
                        grid.set_position(0, x_temporaire,y_temporaire)
                        shark.reset_indice_reproduction()


bbfish=Fish((1,2))
bbfish.get_position()
list_fishes=[]
list_fishes.append(bbfish)
postion_check_actual = list_fishes[0].get_position()
print(bbfish.get_position())

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
