from fish import Fish



class Shark(Fish):
    def __init__(self, position : tuple, valeur_accouchement = VALEUR_CHOISIE_ACCOUCHEMENT_REQUIN, chronon = 0, energy  = 10):
        super().__init__(position, valeur_accouchement, chronon)

        self.energy = energy
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0

        def eat(self):
            self.energy = 10

        def perte_energy(self):
            self.energy -= 1


