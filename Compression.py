import numpy as np


class Cage:
    def __init__(self):
        self.Items = np.array()


def compression(grid):
    grid_size = (len(grid[0]), len(grid))
    ingrid_size = (len(grid[0, 0][0]), len(grid[0, 0]))
    output = np.zeros(grid_size, dtype=Cage)

    for grid_i in range(0, grid_size[0]):
        for grid_j in range(0, grid_size[1]):
            cur_cage = grid[grid_i, grid_j]
            new_cage = np.zeros((ingrid_size[0]//2, ingrid_size[1]//2))
            for i in range(0, ingrid_size[0]//2):
                for j in range(0, ingrid_size[1]//2):
                    new_color = 0
                    for hpixel in range(2):
                        for vpixel in range(2):
                            new_color += cur_cage[i *
                                                  2 + hpixel, j * 2 + vpixel]
                    new_color = new_color / 4
                    new_cage[i, j] = int(new_color)

            output[grid_i, grid_j] = new_cage

    return output
