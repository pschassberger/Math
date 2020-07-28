# make planet functions

class Planet:
    # constructor
    def __init__ (self, name, mass, xpos, ypos, zpos):
        self.name = name
        self.mass = mass
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
    def data(self):
        print(self.name, self.mass)




earth = Planet("meh",500,100,0,0)
sun=Planet("sun", 100,20,0,0)

x = earth.xpos - sun.xpos

print(x)