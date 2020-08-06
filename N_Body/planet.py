# make planet class
import numpy as np
class Planet:
    # constructor
    def __init__ (self, name, mass, pos_vector, momentum_vector):
        self.name = name
        self.mass = mass
        # position lists
        self.pos_vector = pos_vector
        # velocity list
        self.momentum_vector = momentum_vector
        
    

'''from astroquery.jplhorizons import Horizons

obj = Horizons(id='399', location='10',
            epochs={'start':'2017-10-01',
                    'stop':'2017-10-02',
                    'step':'10m'})
vec = obj.vectors()  
print()'''