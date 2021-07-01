import numpy as np
from numba import jit


# take grid nxn return (n/k)x(n/k)
@jit(nopython=True)
def compression(grid, k):
    grid_size = len(grid)
    ingrid_size = len(grid[0, 0])
    ingd_size_dev = ingrid_size // k
    output = np.zeros((grid_size, grid_size, ingrid_size//2,
                      ingrid_size//2), dtype=np.uint8)

    for grid_i in range(grid_size):
        for grid_j in range(grid_size):
            for i in range(ingd_size_dev):
                for j in range(ingd_size_dev):
                    new_color = 0
                    for hpixel in range(k):
                        for vpixel in range(k):
                            new_color += \
                                grid[grid_i, grid_j][i*k + hpixel, j*k + vpixel]
                    new_color = new_color / k**2
                    output[grid_i, grid_j, i, j] = int(new_color)

    return output
