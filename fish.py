class Fish:
    def __init__(self, position : tuple, childbirth_value = 2, chronon = 0 ):
        """
        A class representing a fish with attributes related to its position, reproduction, and age.

        Attributes:
            position (tuple): A tuple representing the position of the fish (e.g., (x, y) coordinates).
            childbirth_value (int): The reproduction value, indicating the number of offspring the fish can have at reproduction. Default is 2.
            reproduction_index (int): A counter or indicator of the fish's reproduction cycle. Default is 0.
            chronon (int): A time or age indicator for the fish. Default is 0.

        Methods:
            __init__(self, position: tuple, childbirth_value=2, chronon=0):
                Initializes a new fish with the given position, reproduction value, and age.
        """
        self.position = position
        self.childbirth_value = childbirth_value
        self.reproduction_index = 0
        self.chronon = chronon


    def chronon_increment(self):
        """
        Increments the age or time indicator (chronon) of the fish by 1.

        This method updates the `chronon` attribute, which typically represents the fish's age or the passage of time in the simulation.

        No parameters are required as it operates on the instance's `chronon` attribute directly.

        Returns:
            None
        """
        self.chronon += 1

    def reproduction_index_increment(self):
        """
        Increments the reproduction index (reproduction_index) of the fish by 1.

        This method updates the `reproduction_index` attribute, which tracks the fish's reproduction cycle or readiness for reproduction.

        No parameters are required as it operates on the instance's `reproduction_index` attribute directly.

        Returns:
            None
        """
        self.reproduction_index += 1

    def reset_reproduction_index(self):
        """
        Resets the reproduction index (reproduction_index) of the fish to 0.

        This method sets the `reproduction_index` attribute back to 0, typically used after the fish has reproduced or completed a reproduction cycle.

        No parameters are required as it operates on the instance's `reproduction_index` attribute directly.

        Returns:
            None
        """
        self.reproduction_index = 0

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
    
    def reproduction_possibility(self):
        """
        Checks if the fish is eligible for reproduction.

        This method compares the fish's reproduction index (`reproduction_index`) with its reproduction threshold (`childbirth_value`).
        If the reproduction index is greater than or equal to the threshold, the fish is considered ready to reproduce.

        Returns:
            bool: `True` if the fish's reproduction index is greater than or equal to its reproduction threshold, `False` otherwise.
        """
        return self.reproduction_index >= self.childbirth_value

    def get_position(self):
        """
        Returns the current position of the fish.

        This method retrieves the `position` attribute of the fish, which represents its location, typically as a tuple (x, y).

        Returns:
            tuple: The current position of the fish, represented as a tuple (x, y).
        """
        return self.position
    
    def get_chronon(self):
        """
        Retrieves the current chronon value.

        This method returns the value of the chronon attribute, which represents
        the current time or state within a time-based or event-driven system.

        Returns:
            The current value of the chronon (data type depends on the attribute).
        """
        return self.chronon

