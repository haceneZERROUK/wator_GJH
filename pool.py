from fish import Fish
from shark import Shark


class Grid:


    def __init__(self, row:int, column:int):
        """
        Initializes the grid environment with the specified dimensions.

        Parameters:
            row (int): The number of rows in the grid.
            column (int): The number of columns in the grid.
        """
        self.column = column
        self.row = row
        self.pool = self.generate_wator_table(row, column)
        self.form_table = []

    def generate_wator_table(self, row, column):
        table = []
        for i in range(row):
            table.append([0] * column)
        return table


    def get_value(self, pos:tuple) -> int|object|None:
        """
        Returns the value or object at the specified position in the grid.

        Parameters:
            pos (tuple): A tuple (row, column) indicating the grid position.

        Returns:
            int | object | None: The value or object at the given position.
        """
        row = pos[0]
        column = pos[1]
        return self.pool[row][column]
    
    def set_value(self, pos:tuple, value: object|int) -> None:
        """
        Sets the value at a specific position in the grid.

        Parameters:
            pos (tuple): A tuple (row, column) indicating the grid position.
            value (object | int): The value to set at the given position.
        
        Returns:
            None
        """
        row = pos[0]
        column = pos[1]
        self.pool[row][column] = value



    def generate_alternative_grid(self):
        """
        Generates a simplified grid representation with symbols for different entities.

        Iterates through the `pool` grid, replacing:
            - `Shark` objects with 'S',
            - `Fish` objects with 'F',
            - Empty cells (0) with '0'.
        
        Updates the `form_table` attribute with these symbols.

        Returns:
            None
        """
        for row_grid in self.pool:
            for column_grid in row_grid:
                if isinstance(column_grid , Shark):
                    self.form_table.append('\U0001F988')
                elif isinstance(column_grid, Fish):
                    self.form_table.append('\U0001F41F')
                elif column_grid == 0:
                    self.form_table.append('\U0001F30A')
                
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
        for row in self.pool:
            for column in row:
                if isinstance(column, Shark):
                    if column.chronon <5:
                        print('\U0001F990', end = ' ')
                    else :
                        print('\U0001F99E', end = ' ')
                elif isinstance(column, Fish):
                    if column.chronon <5:
                        print('\U0001F421', end = ' ')
                    else:
                        print('\U0001F420', end = ' ')
                else:
                    print('\U0001F30A', end = ' ')

            print ('')
