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



# calculation

def calculations(time):
    vy = 1.630
    vx = 0.0
    dt = 0.0
    x, y = 0.5, 0.0

    # t = 0
    for i in range(time):
        x, y = x + vx * dt, y + vy * dt
        radii = np.sqrt(x**2 + y**2)
        # acceleration
        ax, ay = -x / radii**3, -y / radii**3
        r_cube = 1 / radii**3
        # time increment
        dt += 0.05
        vx, vy = vx + ax * dt, vy + ay * dt
        dt += 0.05



    print(radii)

calculations(3)



