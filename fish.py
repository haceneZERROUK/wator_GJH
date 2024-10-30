class Fish:
    def __init__(self, position : tuple, indice_reproduction : int):
        self.position = position
        self.indice_reproduction = indice_reproduction
        self.current_reproduction = 0

    def maj_reproduction(self):
        self.current_reproduction += 1
    def are_you_reproducible(self):
        return self.indice_reproduction <= self.current_reproduction
    def reinitialise_reproduction(self):
        self.current_reproduction = 0
    
    


