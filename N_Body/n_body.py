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
    
    x, y = x + vx * dt, y + vy * dt
    radii = np.sqrt(x**2 + y**2)
    # acceleration
    ax, ay = -x / radii**3, -y / radii**3
    r_cube = 1 / radii**3
    # time increment
    dt += 0.05
    vx, vy = vx + ax * dt, vy + ay * dt
    dt += 0.05
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
        dradii = np.sqrt(x_pos[i]**2 + y_pos[i]**2)
        dax = -x_pos[i] / r_val[i]**3
        day = -y_pos[i] / r_val[i]**3
        r_val.append(dradii)
        x_accel.append(dax)
        y_accel.append(day)
        # inverse of 3 cube
        dr_cube = 1 / r_val[i]**3
        cube_val.append(dr_cube)
        # velocities
        dt += 0.05
        dvx = x_vel[i] + x_accel[i] * dt
        dvy = y_vel[i] + y_accel[i] * dt
        x_vel.append(dvx)
        y_vel.append(dvy)
        # fin
        dt += 0.05
        print(i)


    #print(x_pos)
    #print(x, vx, ax, y, vy, ay, radii, r_cube, dt)
calculations(2)



