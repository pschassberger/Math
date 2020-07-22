'''
This program will be a simulation of the N_Body problem 
according to classical mechanics. 
F = m*a
mi(dv_ix / dt) = -G * mi * mj(xi - xj) / rij**3
mi(dv_iy / dt) = -G * mi * mj(yi - yj) / rij**3
mi(dv_iz / dt) = -G * mi * mj(zi - zj) / rij**3

rij = sqrt((xi - xj)**2 + (yi - yj)**2 + (zi -zj)**2)
'''
import numpy as np
import matplotlib as plt

# Constants in SI
GC = 6.673e-11
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 

dt = 0.1

# calculation
t = 0.0
x = 0.5
y = 0.0
v_x = 0.0
v_y = 1.63

def calculations(time):
    radii = np.sqrt(x**2 + y**2)
    # acceleration
    a_x = -x / radii**3





