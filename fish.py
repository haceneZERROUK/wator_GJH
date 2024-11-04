class Fish:
    def __init__(self, position : tuple, valeur_accouchement = 10, chronon = 0 ):
        """
        Initialise une instance de Fish.

        Args:
            position (tuple): Position du poisson sous forme de tuple (x, y).
            valeur_accouchement (int, optional): Valeur associée à l'accouchement. Par défaut, 1.
            chronon (int, optional): Compteur de temps (chronon). Par défaut, 0.
        """
        self.position = position
        self.valeur_accouchement = valeur_accouchement
        self.indice_reproduction = 0
        self.chronon = chronon


    def incrementation_chronon(self):
        """Incrémente le chronon du poisson de 1."""
        self.chronon += 1

    def incrementation_indice_reproduction(self):
        """Incrémente l'indice de reproduction du poisson de 1."""
        self.indice_reproduction += 1

    def reset_indice_reproduction(self):
        """Réinitialise l'indice de reproduction à 0."""
        self.indice_reproduction = 0

    def set_position(self, tuple_position):
        """
        Définit la position du poisson.

        Args:
            x (int): Coordonnée x de la nouvelle position.
            y (int): Coordonnée y de la nouvelle position.
        """
        self.position = (tuple_position)
    
    def possibilite_reproduction(self):
        return self.indice_reproduction >= self.valeur_accouchement

    def get_position(self):
        """
        Retourne la position actuelle du poisson.

        Returns:
            tuple: La position du poisson sous forme de tuple (x, y).
        """
        return self.position
