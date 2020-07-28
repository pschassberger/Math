# make planet functions
M_SUN = 1.989e30 
M_EARTH = 5.972e24
AU = 150e6 
class Planet:
    # constructor
    def __init__ (self, name, mass, xpos, ypos, zpos, 
                    xvel, yvel, zvel, xaccel, yaccel, zaccel):
        self.name = name
        self.mass = mass
        # position lists
        self.x_pos_list = [xpos]
        self.y_pos_list = [ypos]
        self.z_pos_list = [zpos]
        # velocity list
        self.x_vel_list = [xvel]
        self.y_vel_list = [yvel]
        self.z_vel_list = [zvel]
        # accelleration list
        self.x_accel_list = [xaccel]
        self.y_accel_list = [yaccel]
        self.z_accel_list = [zaccel]
    

sun = Planet("Sun", M_SUN, 20, 20, 20, 0, 0, 0, 0, 0, 0)
earth = Planet("Earth", M_EARTH, AU, 0, 0, -0.2, 1.630, 0, -4.0, 0, 0)
sun.y_pos_list.append(45)
#print(sun.y_pos_list)