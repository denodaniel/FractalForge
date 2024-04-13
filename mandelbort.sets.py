import numpy as np
import matplotlib.pyplot as plt

def mandelbort(c, max_iter ):
    z = 0
    for n in range (max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter
 
def mandelbrot_set(minx, maxx, miny, maxy, width, height, max_iter):
    x = np.linspace(minx, maxx, width)
    y = np.linspace(maxy, miny, height)  # Fixed the order of height and width
    mset = np.zeros((height, width))  # Corrected order of arguments for np.zeros

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbort(c, max_iter)

    return mset


minx , maxx , miny , maxy = -2.0, 1.0, -1.5, 1.5 #SETIING THE PARAMETERS
width = 1000
height = 1000
max_iter = 100


mandelbort_image = mandelbrot_set(minx, maxx, miny,maxy, width,height,max_iter)

plt.imshow(mandelbort_image, extent=[minx,maxx,miny,maxy], cmap= 'hot')
plt.colorbar()
plt.title('MANDLEBROT')
plt.xlabel('REAL')
plt.ylabel('IMAGINARY')
plt.show()






   
