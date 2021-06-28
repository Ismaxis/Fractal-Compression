import numpy as np


class Cage:
    def __init__(self):
        self.Items = np.array()


# take grid 20x20 return 10x10
def compression(grid, k):
    grid_size = (len(grid[0]), len(grid))
    ingrid_size = (len(grid[0, 0][0]), len(grid[0, 0]))
    output = np.zeros(grid_size, dtype=Cage)

    for grid_i in range(0, grid_size[0]):
        for grid_j in range(0, grid_size[1]):
            cur_cage = grid[grid_i, grid_j]
            new_cage = np.zeros((ingrid_size[0]//k, ingrid_size[1]//k))
            for i in range(0, ingrid_size[0]//k):
                for j in range(0, ingrid_size[1]//k):
                    new_color = 0
                    for hpixel in range(k):
                        for vpixel in range(k):
                            new_color += cur_cage[i *
                                                  k + hpixel, j * k + vpixel]
                    new_color = new_color / k**2
                    new_cage[i, j] = int(new_color)

            output[grid_i, grid_j] = new_cage

    return output
