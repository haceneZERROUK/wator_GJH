VALEUR_INITIALE_REPRODUCTION = 5


class Shark(Fish):
    def __init__(self, position,  indice_reproduction,  energy_value=3, vivant=True, valeur = 2,):
        super().__init__(position, indice_reproduction)
        self.valeur = valeur
        self.energy_value = energy_value
        self.indice_reproduction = indice_reproduction
        self.vivant = vivant

    def reproduction(self):
        if self.indice_reproduction >= VALEUR_INITIALE_REPRODUCTION:
            if Shark.scan(self.position):

    def maj_reproduction(self):
        self.indice_reproduction +=1
        return self.indice_reproduction
