
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
sun = Planet("Sun", M_SUN, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
earth = Planet("Earth", M_EARTH, AU, 0.0, 0.0, -0.2, 460, 0.0, -4.44e-17, 0.0, 0.0)

# calculation
def calculations(time, planet_1, planet_2):
    # time increment
    dt = 3600
    radii_list=[]
    dr_radii = np.sqrt((planet_1.x_pos_list[0] - planet_2.x_pos_list[0])**2 
                        + (planet_1.y_pos_list[0] - planet_2.y_pos_list[0])**2
                        + (planet_1.z_pos_list[0] - planet_2.z_pos_list[0])**2)
    radii_list.append(dr_radii)
    rcube_inv_list=[]
    # itterate calculations
    for i in range(time):
        # x,y,z coords via x = x + velocity * time
        #planet_1
        dx_pln1 = planet_1.x_pos_list[i] + planet_1.x_vel_list[i] * dt
        planet_1.x_pos_list.append(dx_pln1)
        dy_pln1 = planet_1.y_pos_list[i] + planet_1.y_vel_list[i] * dt
        planet_1.y_pos_list.append(dy_pln1)
        dz_pln1 = planet_1.z_pos_list[i] + planet_1.z_vel_list[i] * dt
        planet_1.z_pos_list.append(dz_pln1)
        #planet_2
        dx_pln2 = planet_2.x_pos_list[i] + planet_2.x_vel_list[i] * dt
        planet_2.x_pos_list.append(dx_pln2)
        dy_pln2 = planet_2.y_pos_list[i] + planet_2.y_vel_list[i] * dt
        planet_2.y_pos_list.append(dy_pln2)
        dz_pln2 = planet_2.z_pos_list[i] + planet_2.z_vel_list[i] * dt
        planet_2.z_pos_list.append(dz_pln2)
        
        # raddii, acceleration r = sqrt((xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2)
        dr_radii = np.sqrt((planet_1.x_pos_list[i+1] - planet_2.x_pos_list[i+1])**2 
                            + (planet_1.y_pos_list[i+1] - planet_2.y_pos_list[i+1])**2
                            + (planet_1.z_pos_list[i+1] - planet_2.z_pos_list[i+1])**2)
        radii_list.append(dr_radii)
        
        # inverse of r**3 cube
        if radii_list[i+1] > 0.0:
            rcube_inv = 1.0 / radii_list[i+1]**3
            rcube_inv_list.append(rcube_inv)
        else:
            rcube_inv_list.append(0)
        
        # acceleration
        # dv/dt = -Gm(xi-xj) / r**3
        #planet 1
        dax_pln1 = -(planet_1.x_pos_list[i+1] - planet_2.x_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_2.mass
        planet_1.x_accel_list.append(dax_pln1)
        day_pln1 = -(planet_1.y_pos_list[i+1] - planet_2.y_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_2.mass
        planet_1.y_accel_list.append(day_pln1)
        daz_pln1 = -(planet_1.z_pos_list[i+1] - planet_2.z_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_2.mass
        planet_1.z_accel_list.append(daz_pln1)
        #planet 2
        dax_pln2 = -(planet_2.x_pos_list[i+1] - planet_1.x_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_1.mass
        planet_2.x_accel_list.append(dax_pln2)
        day_pln2 = -(planet_2.y_pos_list[i+1] - planet_1.y_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_1.mass
        planet_2.y_accel_list.append(day_pln2)
        daz_pln2 = -(planet_2.z_pos_list[i+1] - planet_1.z_pos_list[i+1]) * rcube_inv_list[i] * GC * planet_1.mass
        planet_2.z_accel_list.append(daz_pln2)
        
        # velocities
        # planet 1
        dvx_pln1 = planet_1.x_vel_list[i] + planet_1.x_accel_list[i+1] * dt
        planet_1.x_vel_list.append(dvx_pln1)
        dvy_pln1 = planet_1.y_vel_list[i] + planet_1.y_accel_list[i+1] * dt
        planet_1.y_vel_list.append(dvy_pln1)
        dvz_pln1 = planet_1.z_vel_list[i] + planet_1.z_accel_list[i+1] * dt
        planet_1.z_vel_list.append(dvz_pln1)
        # planet 2
        dvx_pln2 = planet_2.x_vel_list[i] + planet_2.x_accel_list[i+1] * dt
        planet_2.x_vel_list.append(dvx_pln2)
        dvy_pln2 = planet_2.y_vel_list[i] + planet_2.y_accel_list[i+1] * dt
        planet_2.y_vel_list.append(dvy_pln2)
        dvz_pln2 = planet_2.z_vel_list[i] + planet_2.z_accel_list[i+1] * dt
        planet_2.z_vel_list.append(dvz_pln2)
        

    #print(planet_2.x_pos_list, planet_2.y_pos_list)

    # fin
    # plot 
    plt.scatter(sun.x_pos_list, sun.y_pos_list, color="yellow")
    plt.scatter(earth.x_pos_list, earth.y_pos_list, color="blue")
    plt.ylim(-2*AU, 2*AU)
    plt.xlim(-2*AU, 2*AU)
    #plt.savefig("Orbital.png")
    plt.show()
    
calculations(365, sun, earth)


