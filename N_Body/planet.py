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
        self.x_pos_list = []
        self.y_pos_list = []
        self.z_pos_list = []
        # velocity list
        self.x_vel_list = []
        self.x_vel_list = []
        self.x_vel_list = []
        # accelleration list
        self.x_accel_list = []
        self.y_accel_list = []
        self.z_accel_list = []
    
