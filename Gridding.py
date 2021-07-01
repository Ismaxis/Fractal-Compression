import numpy as np
from numba import jit


@jit(nopython=True)
def gridding(image, squares_size):
    grid_size = len(image)//squares_size
    output = np.zeros((grid_size, grid_size,
                       squares_size, squares_size), dtype=np.uint8)
    for i in range(grid_size):
        for j in range(grid_size):
            for hpix in range(squares_size):
                for vpix in range(squares_size):
                    output[i, j] = image[i * squares_size:(i + 1) * squares_size,
                                         j * squares_size:(j + 1) * squares_size]

    return output
