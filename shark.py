from fish import Fish


class Shark(Fish):
    def __init__(self, position : tuple, indice_reproduction : int, current_reproduction = 0, chronon = 0, energy  = 10):
        super().__init__(position, indice_reproduction, current_reproduction, chronon)
        self.energy = energy

        def eat(self):
            self.energy = 10
            
