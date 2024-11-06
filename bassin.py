from fish import Fish
from shark import Shark

def generate_wator_table(lignes, colonnes):
    table = []
    for i in range(lignes):
        table.append([0] * colonnes)
    return table


class Grid:
    
    def __init__(self, ligne:int, colonne:int):
        """
        Initializes the grid environment with the specified dimensions.

        Parameters:
            ligne (int): The number of rows in the grid.
            colonne (int): The number of columns in the grid.
        """
        self.colonne = colonne
        self.ligne = ligne
        self.bassin = generate_wator_table(ligne, colonne)
        self.form_table = []

    def get_value(self, pos:tuple) -> int|object|None:
        """
        Returns the value or object at the specified position in the grid.

        Parameters:
            pos (tuple): A tuple (row, column) indicating the grid position.

        Returns:
            int | object | None: The value or object at the given position.
        """
        ligne = pos[0]
        colonne = pos[1]
        return self.bassin[ligne][colonne]
    
    def set_value(self, pos:tuple, value: object|int) -> None:
        """
        Sets the value at a specific position in the grid.

        Parameters:
            pos (tuple): A tuple (row, column) indicating the grid position.
            value (object | int): The value to set at the given position.
        
        Returns:
            None
        """
        ligne = pos[0]
        colonne = pos[1]
        self.bassin[ligne][colonne] = value



    def generate_alternative_grid(self):
        """
        Generates a simplified grid representation with symbols for different entities.

        Iterates through the `bassin` grid, replacing:
            - `Shark` objects with 'S',
            - `Fish` objects with 'F',
            - Empty cells (0) with '0'.
        
        Updates the `form_table` attribute with these symbols.

        Returns:
            None
        """
        for ligne_grid in self.bassin:
            for colonne_grid in ligne_grid:
                if isinstance(colonne_grid , Shark):
                    self.form_table.append('S')
                elif isinstance(colonne_grid, Fish):
                    self.form_table.append('F')
                elif colonne_grid == 0:
                    self.form_table.append('0')
                else:
                    ValueError()


    def print_grid(self):
        """
        Prints the grid with emoji representations for sharks, fish, and empty cells.

        - Sharks are represented by 🦐 (young) and 🦞 (adult) depending on age.
        - Fish are represented by 🐡 (young) and 🐠 (adult) depending on age.
        - Empty cells are represented by 🌊.

        Returns:
            None
        """
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
