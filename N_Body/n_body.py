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
vy = 1.630
vx = 0.0

def calculations(time):
    radii = np.sqrt(x**2 + y**2)
    # acceleration
    a_x = -x / radii**3
    a_y = -y / radii**3
    r_cube = 1 / radii**3
    # store coordinates
    x_pos=[]
    y_pos=[]
    radii_list=[]
    r_cube_list=[]
    ax_list=[]
    ay_list=[]
    # velocities
    v_x = vx + a_x * radii
    v_y = vy + a_y * radii

    for i in range(time):
        x1 = x + v_x * dt
        y1 = y + v_y * dt
        radii1 = np.sqrt(x1**2 + y1**2)
        r_cube1 = 1 / radii1**3
        a_x1 = -x1 / radii1**3
        a_y1 = -y1 / radii1**3

        x_pos.append(x1)
        y_pos.append(y1)
        radii_list.append(radii1)
        r_cube_list.append(r_cube1)
        ax_list.append(a_x1)
        ay_list.append(a_y1)

        dt += 0.1

    print(x_pos, y_pos, radii_list, r_cube_list, ax_list, ay_list)

calculations(10)



