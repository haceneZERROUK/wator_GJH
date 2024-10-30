import random

class Fish:
    def __init__(self, position : tuple, valeur = 1, vivant=True, indice_reproduction=0):
        self.position = position
        self.vivant = vivant
        self.indice_reproduction = indice_reproduction



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
                  [self.position[0]+1,self.position[1] + 1]):
            if isinstance(world[x[0]][x[1]], Fish):
                scan_fish.append(x)
            if isinstance(world[x[0]][x[1]], Shark):
                scan_shark.append(x)
            if world[x[0]][x[1]] ==0:
                scan_eau.append(x)
        return(scan_eau, scan_fish, scan_shark)
t

eau , poisson ,requin = scan(1,1)

    def reproduction_et_deplacement(self):
        if self.indice_reproduction >= VALEUR_INITIALE_REPRODUCTION:
            if self.scan[0] != []:
                (x,y) = self.position()
                liste_objets_poisson.append(fish((x,y)))
                self.position = random.choices[self.scan[0]]
            else:
                pass
        else:
            pass

    
    def maj_reproduction(self):
        self.indice_reproduction += 1
        return self.indice_reproduction()