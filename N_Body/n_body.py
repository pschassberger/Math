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
import matplotlib.pyplot as plt

# Constants in SI
GC = 6.673e-11
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 



# calculation

def calculations(time):
    vy = 1.630
    vx = -0.20
    dt = 0.0
    x, y = 0.5, 0.0
    radii = 0.5
    r_cube = 8.00
    ax = -4.0
    ay = 0.00
    dt = 0.1
    tick = 0.1
    # dict to store values
    '''data_dict = {
        'x_pos': [],
        'y_pos': [],
        'x_accel': [],
        'y_accel': [],
        'x_vel': [],
        'y_vel': [],
    }'''
    # t = 0
    x_pos = []
    y_pos = []
    x_accel = []
    y_accel = []
    x_vel = []
    y_vel = []
    r_val = []
    cube_val = []
    
    x_pos.append(x)
    y_pos.append(y)
    r_val.append(radii)
    x_accel.append(ax)
    y_accel.append(ay)
    cube_val.append(r_cube)
    x_vel.append(vx)
    y_vel.append(vy)
    # itterate calculations
    for i in range(time):
        # x,y coords
        dx = x_pos[i] + x_vel[i] * dt
        x_pos.append(dx)
        dy = y_pos[i] + y_vel[i] * dt
        y_pos.append(dy)
        # raddii, accelerations
        dradii = np.sqrt(x_pos[i+1]**2 + y_pos[i+1]**2)
        r_val.append(dradii)
        # inverse of 3 cube
        dr_cube = 1.0 / r_val[i+1]**3
        cube_val.append(dr_cube)
        # acceleration
        dax = -x_pos[i+1] * cube_val[i+1]
        day = -y_pos[i+1] * cube_val[i+1]
        x_accel.append(dax)
        y_accel.append(day)
        
        # velocities
        dvx = x_vel[i] + x_accel[i+1] * dt
        dvy = y_vel[i] + y_accel[i+1] * dt
        x_vel.append(dvx)
        y_vel.append(dvy)
        #dt += 0.05

        # fin
    # plot 
    plt.scatter(x_pos, y_pos)
    plt.ylim(-5, 5)
    plt.xlim(-5, 5)
    plt.show()
    # print data
    print(x_pos)
calculations(20)

