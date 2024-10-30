def generate_wator_table(col, row):
    table = []
    for i in range(col):
        table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
    return table


class Grid:
    
    def __init__(self, colone:int, ligne:int):
        self.colone = colone
        self.ligne = ligne
        self.bassin = generate_wator_table(colone, ligne)

    def get_value(self, pos:tuple) -> int|object|None:
        line = pos[0]
        col = pos[1]
        return self.bassin[line][col]
    
    def set_value(self, pos:tuple, value: object|int) -> None:
        line = pos[0]
        col = pos[1]
        self.bassin[line][col] = value
    def print_grid(self) -> str:
        new_str = ""
        for index in range(self.ligne):
            new_str += f"{self.bassin[index]}"
            if index < self.ligne -1:
                new_str += "\n"
        print(new_str)
    
if __name__ == "__main__":
    # Exemple d'utilisation
    new_world = Grid(3,3)
    new_world.print_grid()
    
