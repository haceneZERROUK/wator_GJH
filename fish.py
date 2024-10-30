class fish:
    def __init__(self, position : tuple, vivant : bool, indice_reproduction : int):
        self.position = position
        self.vivant = vivant
        self.indice_reproduction = indice_reproduction

    Haut = (-1, 0)
    Bas = (1, 0)
    gauche = (0, -1)self.position[0]
    droite = (0,1)

    valeurinitiale = 10

    # def scan(self):
    #     scan_eau=[]
    #     scan_shark=[]
    #     scan_fish=[]
    #     for x in ([i-1,j], [i+1,j], [i,j-1], [i,j+1]):
    #         if world[x[0]][x[1]] ==0:
    #             scan_eau.append(x)
    #         if world[x[0]][x[1]] ==1:
    #             scan_fish.append(x)
    #         if world[x[0]][x[1]] ==2:
    #             scan_shark.append(x)
    #     return scan_eau, scan_fish, scan_shark

    def scan(self):
        scan_eau=[]
        scan_shark=[]
        scan_fish=[]

        for x in ([self.position[0]-1,self.position[1]], \
                  [self.position[0]+1,self.position[1]], \
                  [self.position[0],self.position[1] - 1], \
                  [self.position[0]+1,self.position[1] + 1], \

            if world[x[0]][x[1]] ==0:
                scan_eau.append(x)
            if world[x[0]][x[1]] ==1:
                scan_fish.append(x)
            if world[x[0]][x[1]] ==2:
                scan_shark.append(x)
        return scan_eau, scan_fish, scan_shark



    eau , poisson ,requin = scan(1,1)

    def maj_reproduction(self):
        self.indice_reproduction += 1

    def reproduction(self):


