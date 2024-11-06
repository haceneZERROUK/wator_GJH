class Fish:
    def __init__(self, position : tuple, valeur_accouchement = 2, chronon = 0 ):
        """
        A class representing a fish with attributes related to its position, reproduction, and age.

        Attributes:
            position (tuple): A tuple representing the position of the fish (e.g., (x, y) coordinates).
            valeur_accouchement (int): The reproduction value, indicating the number of offspring the fish can have at reproduction. Default is 2.
            indice_reproduction (int): A counter or indicator of the fish's reproduction cycle. Default is 0.
            chronon (int): A time or age indicator for the fish. Default is 0.

        Methods:
            __init__(self, position: tuple, valeur_accouchement=2, chronon=0):
                Initializes a new fish with the given position, reproduction value, and age.
        """
        self.position = position
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0
        self.chronon = chronon


    def incrementation_chronon(self):
        """
        Increments the age or time indicator (chronon) of the fish by 1.

        This method updates the `chronon` attribute, which typically represents the fish's age or the passage of time in the simulation.

        No parameters are required as it operates on the instance's `chronon` attribute directly.

        Returns:
            None
        """
        self.chronon += 1

    def incrementation_indice_reproduction(self):
        """
        Increments the reproduction index (indice_reproduction) of the fish by 1.

        This method updates the `indice_reproduction` attribute, which tracks the fish's reproduction cycle or readiness for reproduction.

        No parameters are required as it operates on the instance's `indice_reproduction` attribute directly.

        Returns:
            None
        """
        self.indice_reproduction += 1

    def reset_indice_reproduction(self):
        """
        Resets the reproduction index (indice_reproduction) of the fish to 0.

        This method sets the `indice_reproduction` attribute back to 0, typically used after the fish has reproduced or completed a reproduction cycle.

        No parameters are required as it operates on the instance's `indice_reproduction` attribute directly.

        Returns:
            None
        """
        self.indice_reproduction = 0

    def set_position(self, tuple_position):
        """
        Sets the position of the fish to a new location.

        This method updates the `position` attribute of the fish to the provided tuple, which represents the new coordinates (e.g., (x, y)).

        Parameters:
            tuple_position (tuple): A tuple containing the new position of the fish, typically in the form (x, y).

        Returns:
            None
        """
        self.position = (tuple_position)
    
    def possibilite_reproduction(self):
        """
        Checks if the fish is eligible for reproduction.

        This method compares the fish's reproduction index (`indice_reproduction`) with its reproduction threshold (`valeur_accouchement`).
        If the reproduction index is greater than or equal to the threshold, the fish is considered ready to reproduce.

        Returns:
            bool: `True` if the fish's reproduction index is greater than or equal to its reproduction threshold, `False` otherwise.
        """
        return self.indice_reproduction >= self.valeur_accouchement

    def get_position(self):
        """
        Returns the current position of the fish.

        This method retrieves the `position` attribute of the fish, which represents its location, typically as a tuple (x, y).

        Returns:
            tuple: The current position of the fish, represented as a tuple (x, y).
        """
        return self.position
    
    def get_chronon(self):
        
        return self.chronon

