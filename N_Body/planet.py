# make planet functions

class Planet:
    # constructor
    def __init__ (self, name, mass, xpos, ypos, zpos, 
                    xvel, yvel, zvel, xaccel, yaccel, zaccel):
        self.name = name
        self.mass = mass
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xvel = xvel
        self.yvel = yvel
        self.zvel = zvel
        # position lists
        self.x_pos_list = [xpos]
        self.y_pos_list = [ypos]
        self.z_pos_list = [zpos]
        # velocity list
        self.x_vel_list = [xvel]
        self.x_vel_list = [yvel]
        self.x_vel_list = [zvel]
        # accelleration list
        self.x_accel_list = [xaccel]
        self.y_accel_list = [yaccel]
        self.z_accel_list = [zaccel]
    

