# create a visualization of the mandelbrot set 

# theorem f(z) = z^2 + C;   z0 = 0; z1 = C^2 + C ...
# C can be defined as (a^2 + bi)

import numpy as np
from PIL import Image

# image bounds
PIXEL = 200
WIDTH = 3
HEIGHT = 3
ITTER = 1000
X1 = -2
Y1 = -1.5

def mandelbrot(c1, c2):
    x=y=0
    for i in range(ITTER):
        x, y = x*x - y*y + c1