def generate_wator_table(col, row):
    table = []
    for i in range(col):
        table.append([0] * row)  # Utilisation de la multiplication pour créer des listes
    return table


class Grid:
    
    def __init__(self, colone:int, ligne:int):
        """
        Initialise une instance de Grid.

        Args:
            colone (int): Le nombre de colonnes dans la grille.
            ligne (int): Le nombre de lignes dans la grille.
        """
        self.colone = colone
        self.ligne = ligne
        self.bassin = generate_wator_table(colone, ligne)

    def get_value(self, pos:tuple) -> int|object|None:
        """
        Retourne la valeur à la position spécifiée dans la grille.

        Args:
            pos (tuple): Un tuple contenant les coordonnées (ligne, colonne).

        Returns:
            int | object | None: La valeur à la position spécifiée, ou None si la position est invalide.
        """
        line = pos[0]
        col = pos[1]
        return self.bassin[line][col]
    
    def set_value(self, pos:tuple, value: object|int) -> None:
        """
        Définit la valeur à la position spécifiée dans la grille.

        Args:
            pos (tuple): Un tuple contenant les coordonnées (ligne, colonne).
            value (object | int): La valeur à assigner à la position spécifiée.
        """
        line = pos[0]
        col = pos[1]
        self.bassin[line][col] = value

    def print_grid(self) -> str:
        """
        Affiche la grille sous forme de chaîne de caractères.

        Returns:
            str: Représentation textuelle de la grille.
        """
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
    
