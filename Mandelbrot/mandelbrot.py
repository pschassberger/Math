# create a visualization of the mandelbrot set 

# theorem f(z) = z^2 + C;   z0 = 0; z1 = C^2 + C ...
# C can be defined as (a^2 + bi)

import numpy as np
from PIL import Image

# image bounds
WIDTH = 3
HEIGHT = 3
X1 = -2
Y1 = -1.5
PIXEL_SCALE = 300
image_width = int(PIXEL_SCALE * WIDTH)
image_height = int(PIXEL_SCALE * HEIGHT)
# x and y coordiante calc
def mandelbrot(c1, c2):
    x=y=0
    for i in range(1000):
        x, y = (x * x) - (y * y) + c1, 2 * x * y + c2
        if ((x * x) + (y * y)) > 4:
            return i + 1
    return 0
# color map for values
def mandel_colors(v):
    values = [0, 64, 128, 196]
    b = values[v % 4] 
    g = values[(v//4) % 4] 
    r = values[(v//16) % 4]
    return (r, g, b)
# matrix to store pixels
matrix = np.zeros((image_height, 
                    image_width,
                    3),
                    dtype=np.uint8)

# loop to populate matrix
def mandel_plot():
    for i in range(image_width):
        # initial points, itterating from x1, y1
        c1 = X1 + i / PIXEL_SCALE
        for j in range(image_height):
            c2 = Y1 + j / PIXEL_SCALE
            value = mandelbrot(c1, c2)
            if value:
                matrix[j, i,] = mandel_colors(value)
    # plot matrix
    mandel_set = Image.fromarray(matrix)
    mandel_set.save('mandelbrotSet.png')
# test it
mandel_plot()
