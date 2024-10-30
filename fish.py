class Fish:
    def __init__(self, position : tuple, valeur_accouchement = 1, chronon = 0 ):
        self.position = position
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0
        self.chronon = chronon


    def incrementation_chronon(self):
        self.chronon += 1

    def incrementation_indice_reproduction(self):
        self.indice_reproduction += 1

    def reset_indice_reproduction(self):
        self.indice_reproduction = 0

    def set_position(self, x,y):
        self.position = (x,y)
    
    def get_position(self):
        return self.position
