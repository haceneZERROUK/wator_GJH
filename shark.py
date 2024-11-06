from fish import Fish


class Shark(Fish):
    INITIAL_SHARK_ENERGY = 10

    def __init__(self, position : tuple, childbirth_value : int = 13, chronon : int = 0, energy : int = INITIAL_SHARK_ENERGY):
        """
        A class representing a shark, which inherits from the Fish class and adds energy management.

        Inherits from:
            Fish: The Shark class is a subclass of the Fish class, and inherits its position, reproduction, and age attributes.

        Attributes:
            INITIAL_SHARK_ENERGY (int): The initial energy of the shark when it is created. Default is 10.
            position (tuple): A tuple representing the position of the shark (e.g., (x, y) coordinates).
            childbirth_value (int): The reproduction value, indicating the number of offspring the shark can have. Default is 13.
            chronon (int): The time or age indicator for the shark. Default is 0.
            energy (int): The energy level of the shark, indicating its health or stamina. Default is set to `INITIAL_SHARK_ENERGY` (10).
            reproduction_index (int): A counter or indicator of the shark's reproduction cycle. Default is 0.

        Methods:
            __init__(self, position: tuple, childbirth_value: int = 13, chronon: int = 0, energy: int = INITIAL_SHARK_ENERGY):
                Initializes a new shark with the given position, reproduction value, age, and energy.
        """
        super().__init__(position, childbirth_value, chronon)
        self.energy = energy
        self.childbirth_value = childbirth_value
        self.reproduction_index = 0

    def eat(self):
        """
        Resets the shark's energy to its initial value.

        This method restores the shark's energy to the default initial energy value (`INITIAL_SHARK_ENERGY`), 
        which represents a full energy state for the shark. Typically called when the shark feeds.

        Returns:
            None
        """
        self.energy = Shark.INITIAL_SHARK_ENERGY

    def energy_loss(self):
        """
        Decreases the shark's energy by 1.

        This method reduces the shark's current energy level by 1, typically representing energy consumption 
        during the shark's activities such as swimming, hunting, or aging.

        Returns:
            None
        """
        self.energy -= 1
    


