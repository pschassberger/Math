import numpy as np
import matplotlib.pyplot as plt
from planet import Planet
# Constants in SI
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 
dt = 0.1


# construct planets
sun = Planet("Sun", M_SUN, [0,0], [0,0])
earth = Planet("Earth", M_EARTH, [0,AU], [0,400])
# calculate the force of gravity 
def gravitationalF(planet_1, planet_2):
    G = 6.673e-11
    diff = np.subtract(planet_1.pos_vector, planet_2.pos_vector)
    radii = np.sqrt(diff ** 2)
    #
    if radii.all() > 0.0:
        rcube_inv = 1.0 / radii**3
    else:
        rcube_inv = 0
    # calculate force
    force = -G * planet_1.mass * planet_2.mass * rcube_inv
    return force


def SolarSystem(days, planet_1, planet_2):
    while(days > 0):
        star_force = gravitationalF(planet_1, planet_2)
        planet_force = gravitationalF(planet_2, planet_1)

        star_momentum = planet_1.momentum_vector + star_force * dt
        planet_momentum = planet_2.momentum_vector + planet_force * dt
        # update position
        planet_1.pos_vector = (planet_1.pos_vector + star_momentum) / (planet_1.mass * dt)
        planet_2.pos_vector = (planet_2.pos_vector + star_momentum) / (planet_2.mass * dt)


        print(planet_1.pos_vector, planet_2.pos_vector)
        days -= 1
    #plot
    plt.plot(planet_1.pos_vector, color="yellow")
    plt.plot(planet_2.pos_vector, color="blue")
    plt.ylim(-2*AU, 2*AU)
    plt.xlim(-2*AU, 6*AU)
    #plt.savefig("Orbital.png")
    plt.show()

SolarSystem(365,sun,earth)
