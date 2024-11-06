from fish import Fish
from shark import Shark

def generate_wator_table(lignes, colonnes):
    table = []
    for i in range(lignes):
        table.append([0] * colonnes)  # Utilisation de la multiplication pour créer des listes
    return table


class Grid:
    
    def __init__(self, ligne:int, colonne:int):
        """
        Initialise une instance de Grid.

        Args:
            colone (int): Le nombre de colonnes dans la grille.
            ligne (int): Le nombre de lignes dans la grille.
        """
        self.colonne = colonne
        self.ligne = ligne
        self.bassin = generate_wator_table(ligne, colonne)
        self.form_table = []

    def get_value(self, pos:tuple) -> int|object|None:
        """
        Retourne la valeur à la position spécifiée dans la grille.

        Args:
            pos (tuple): Un tuple contenant les coordonnées (ligne, colonne).

        Returns:
            int | object | None: La valeur à la position spécifiée, ou None si la position est invalide.
        """
        ligne = pos[0]
        colonne = pos[1]
        return self.bassin[ligne][colonne]
    
    def set_value(self, pos:tuple, value: object|int) -> None:
        """
        Définit la valeur à la position spécifiée dans la grille.

        Args:
            pos (tuple): Un tuple contenant les coordonnées (ligne, colonne).
            value (object | int): La valeur à assigner à la position spécifiée.
        """
        ligne = pos[0]
        colonne = pos[1]
        self.bassin[ligne][colonne] = value



    def generate_alternative_grid(self):
        for ligne_grid in self.bassin:
            for colonne_grid in ligne_grid:
                if isinstance(colonne_grid , Shark):
                    self.form_table.append('\U0001F988')
                elif isinstance(colonne_grid, Fish):
                    self.form_table.append('\U0001F41F')
                elif colonne_grid == 0:
                    self.form_table.append('\U0001F30A')
                
                else:
                    ValueError()
 


    def print_grid(self):
        for ligne in self.bassin:
            for colonne in ligne:
                if isinstance(colonne, Shark):
                    if colonne.chronon <5:
                        print('\U0001F990', end = ' ')
                    else :
                        print('\U0001F99E', end = ' ')
                elif isinstance(colonne, Fish):
                    if colonne.chronon <5:
                        print('\U0001F421', end = ' ')
                    else:
                        print('\U0001F420', end = ' ')
                else:
                    print('\U0001F30A', end = ' ')

            print ('')
