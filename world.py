import random

def generate_wator_table(col, row):
    table = []
    for i in range(col):
        table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
    return table

class World:
    
    def __init__(self, titre, chronon, colone, ligne):
        self.titre = titre
        self.colone = colone
        self.ligne = ligne
        self.chronon = chronon
        self.world_matrix = generate_wator_table(colone, ligne)
        self.shark = []
        self.fish = []

    def initialiser_world(self, shark=1, fish=2):
        while shark > 0 or fish > 0:
            choice_random = random.randint(1, 2)
            if choice_random == 1 and fish > 0:
                fish_generate_col = random.randint(0, self.colone - 1)
                fish_generate_line = random.randint(0, self.ligne - 1)
                if self.world_matrix[fish_generate_col][fish_generate_line] == 0:
                    fish -= 1
                    self.world_matrix[fish_generate_col][fish_generate_line] = 1
                    
            elif choice_random == 2 and shark > 0:
                shark_generate_col = random.randint(0, self.colone - 1)
                shark_generate_line = random.randint(0, self.ligne - 1)
                if self.world_matrix[shark_generate_col][shark_generate_line] == 0:
                    shark -= 1
                    self.world_matrix[shark_generate_col][shark_generate_line] = 2
    def init_list_fish_and_shark(self):
        for line in range(self.ligne):
            for col in range(self.colone):
                if self.world_matrix[line][col] == 1:
                    self.fish.append("fish")
                elif self.world_matrix[line][col] == 2:
                    self.shark.append("shark")
                    
    def where_is_the_fish(self):
        return
    def where_is_the_water(self):
        return
if __name__ == "__main__":
    # Exemple d'utilisation
    world = World("Mon monde", 1, 3, 3)
    world.initialiser_world(3,6)
    for line in world.world_matrix:
        print(line)
    print("Autre\n")
    world.init_list_fish_and_shark()
    print(f"{world.shark=}")
    print(f"{world.fish=}")
