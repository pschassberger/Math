# create a visualization of the mandelbrot set 

# theorem f(z) = z^2 + C;   z0 = 0; z1 = C^2 + C ...
# C can be defined as (a^2 + bi)

import numpy as np
from PIL import Image

# image bounds


def mandelbrot(c1, c2):
    x=y=0
    for i in range(10):
        dx, dy = x * x - y * y + c1, 2 * x * y + c2
        x, y = dx, dy
        print(x, y)

mandelbrot(0.2, 0.1)