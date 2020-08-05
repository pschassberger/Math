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
    