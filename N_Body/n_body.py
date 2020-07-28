
import numpy as np
import matplotlib.pyplot as plt
from planet import Planet
# Constants in SI
GC = 6.673e-11
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 

# construct planets
sun = Planet("Sun", M_SUN, 0, 0, 0, 0, 0, 0, 0, 0, 0)
earth = Planet("Earth", M_EARTH, 8*AU, 0, 0, -0.2, 1.630, 0, -4.0, 0, 0)

# calculation
def calculations(time, planet_1, planet_2):
    # time increment
    dt = 0.1
    # itterate calculations
    for i in range(time):
        # x,y,z coords via x = x + velocity * time
        #planet_1
        dx_pln1 =   planet_1.x_pos_list[i] +  planet_1.x_vel_list[i] * dt
        planet_1.x_pos_list.append(dx_pln1)
        dy_pln1 =   planet_1.y_pos_list[i] +  planet_1.y_vel_list[i] * dt
        planet_1.y_pos_list.append(dy_pln1)
        dz_pln1 =   planet_1.z_pos_list[i] +  planet_1.z_vel_list[i] * dt
        planet_1.z_pos_list.append(dz_pln1)
        #planet_2
        dx_pln2 =   planet_2.x_pos_list[i] +  planet_2.x_vel_list[i] * dt
        planet_2.x_pos_list.append(dx_pln1)
        dy_pln2 =   planet_2.y_pos_list[i] +  planet_2.y_vel_list[i] * dt
        planet_2.y_pos_list.append(dy_pln1)
        dz_pln2 =   planet_2.z_pos_list[i] +  planet_2.z_vel_list[i] * dt
        planet_2.z_pos_list.append(dz_pln1)
        
        # raddii, accelerations
        radii_list=[]
        dr_radii = np.sqrt((planet_1.x_pos_list[i+1] - planet_2.x_pos_list[i+1])**2 
                            + (planet_1.y_pos_list[i+1] - planet_2.y_pos_list[i+1])**2
                            + (planet_1.z_pos_list[i+1] - planet_2.z_pos_list[i+1])**2)
        radii_list.append(dr_radii)
        '''dradii = np.sqrt(x_pos[i+1]**2 + y_pos[i+1]**2 + z_pos[i+1]**2)
        r_val.append(dradii)'''
        # inverse of 3 cube
        rcube_inv_list=[]
        rcube_inv = 1.0 / np.pow(radii_list[i], 3)
        rcube_inv_list.append(rcube_inv)
        '''dr_cube = 1.0 / r_val[i+1]**3
        cube_val.append(dr_cube)'''
        # acceleration
        #planet 1
        dax_pln1 = -planet_1.x_pos_list[i+1] * rcube_inv_list[i]
        planet_1.x_accel_list.append(dax_pln1)
        day_pln1 = -planet_1.y_pos_list[i+1] * rcube_inv_list[i]
        planet_1.y_accel_list.append(day_pln1)
        daz_pln1 = -planet_1.z_pos_list[i+1] * rcube_inv_list[i]
        planet_1.z_accel_list.append(daz_pln1)
        #planet 2
        dax_pln2 = -planet_2.x_pos_list[i+1] * rcube_inv_list[i]
        planet_2.x_accel_list.append(dax_pln2)
        day_pln2 = -planet_2.y_pos_list[i+1] * rcube_inv_list[i]
        planet_2.y_accel_list.append(day_pln2)
        daz_pln2 = -planet_2.z_pos_list[i+1] * rcube_inv_list[i]
        planet_2.z_accel_list.append(daz_pln2)
        '''dax = -x_pos[i+1] * cube_val[i+1]
        day = -y_pos[i+1] * cube_val[i+1]
        x_accel.append(dax)
        y_accel.append(day)'''
        
        # velocities
        dvx = x_vel[i] + x_accel[i+1] * dt
        dvy = y_vel[i] + y_accel[i+1] * dt
        x_vel.append(dvx)
        y_vel.append(dvy)
        print(dx_pln1)

        # fin
    # plot 
    '''plt.scatter(x_pos, y_pos)
    plt.ylim(-5, 5)
    plt.xlim(-5, 5)
    plt.show()
    # print data
    print(x_pos)'''
calculations(1, sun, earth)


