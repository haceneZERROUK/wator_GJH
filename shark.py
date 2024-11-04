from fish import Fish


class Shark(Fish):
    ENERGY_REQUIN_INITIALE = 10

    def __init__(self, position : tuple, valeur_accouchement : int = 10, chronon : int = 0, energy : int = ENERGY_REQUIN_INITIALE):
        """
        Initialise une instance de Shark.

        Args:
            position (tuple): Position du requin sous forme de tuple (x, y).
            valeur_accouchement (int, optional): Valeur associée à l'accouchement. Par défaut, 10.
            chronon (int, optional): Compteur de temps (chronon). Par défaut, 0.
            energy (int, optional): Énergie initiale du requin. Par défaut, 10.
        """
        super().__init__(position, valeur_accouchement, chronon)

        self.energy = energy
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0

    def eat(self):
        """Restaure l'énergie du requin à sa valeur initiale."""
        self.energy = Shark.ENERGY_REQUIN_INITIALE

    def perte_energy(self):
        """Diminue l'énergie du requin de 1."""
        self.energy -= 1
    


