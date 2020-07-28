
import numpy as np
import matplotlib.pyplot as plt
import planet
# Constants in SI
GC = 6.673e-11
M_SUN = 1.989e30 
M_EARTH = 5.972e24
M_JUPITER = 7.898e27
AU = 150e6 

# construct objects
sun = planet("Sun", M_SUN, 0, 0, 0, 0, 0, 0, 0, 0, 0)
earth = planet("Jupiter", M_JUPITER, 8*AU, 0, 0, 0, 1.63, 0, 0, 0, 0)

# calculation
def calculations(time, object1, object2):
    # time increment
    dt = 0.1
    # itterate calculations
    for i in range(time):
        # x,y coords
        dx = x_pos[i] + x_vel[i] * dt
        x_pos.append(dx)
        dy = y_pos[i] + y_vel[i] * dt
        y_pos.append(dy)
        dz = z_pos[i] + z_vel[i] * dt
        z_pos.append(dz)
        # raddii, accelerations
        dradii = np.sqrt(x_pos[i+1]**2 + y_pos[i+1]**2 + z_pos[i+1]**2)
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
        

        # fin
    # plot 
    plt.scatter(x_pos, y_pos)
    plt.ylim(-5, 5)
    plt.xlim(-5, 5)
    plt.show()
    # print data
    print(x_pos)
calculations(20)

