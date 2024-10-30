from fish import Fish


class Shark(Fish):
    ENERGY_REQUIN_INITIALE = 10

    def __init__(self, position : tuple, valeur_accouchement : int = 10, chronon : int = 0, energy : int = ENERGY_REQUIN_INITIALE):
        super().__init__(position, valeur_accouchement, chronon)

        self.energy = energy
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0

    def eat(self):
        self.energy = Shark.ENERGY_REQUIN_INITIALE

    def perte_energy(self):
        self.energy -= 1

