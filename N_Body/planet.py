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
        self.xaccel = xaccel
        self.yaccel = yaccel
        self.zaccel = zaccel
    

def x_position(x, vx, ax):
    x_pos = []
    x_accel = []
    x_vel = []
    #calculations
    dx = x_pos[i] + x_vel[i] * dt
    x_pos.append(dx)
    return x_pos[]
def y_position(object, i):
    x_pos = []
    dy = y_pos[i] + y_vel[i] * dt
    y_pos.append(dy)
    return y_pos[]
def z_position(list, object, i):
    z_pos = []
    dz = z_pos[i] + z_vel[i] * dt
    x_pos.append(dz)
    return z_pos[]

