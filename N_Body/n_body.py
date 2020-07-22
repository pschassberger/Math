'''
This program will be a simulation of the N_Body problem 
according to classical mechanics. 
F = m*a
m(dvx/dt) = -GMmx / r**3
m(dvy/dt) = -GMmy / r**3
m(dvz/dt) = -GMmz / r**3
r = sqrt(x**2 + y**2 + z**2)
'''
import numpy as np
import matplotlib as plt

# Constants in SI
GC = 6.673e-11
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 




