from fish import Fish
VALEUR_INITIALE_REPRODUCTION = 5


class Shark(Fish):
    def __init__(self, position, indice_reproduction, energy_value, vivant):
        super().__init__(position, indice_reproduction)
        self.energy_value = energy_value
                

    def maj_reproduction(self):
        self.indice_reproduction +=1
        return self.indice_reproduction
    