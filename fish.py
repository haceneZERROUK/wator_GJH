class Fish:
    def __init__(self, position : tuple, indice_reproduction : int, current_reproduction = 0, chronon = 0 ):
        self.position = position
        self.current_reproduction = current_reproduction
        self.indice_reproduction = indice_reproduction
        self.chronon = chronon


    def incrementation_chronon(self):
        self.chronon += 1

    def augmentation_current_reproduction(self):
        self.current_reproduction += 1

    def reset_current_reproduction(self):
        self.current_reproduction = 0

    def set_value(self, x,y):
        self.position = (x,y)
    
    def get_value(self):
        return self.position

        

