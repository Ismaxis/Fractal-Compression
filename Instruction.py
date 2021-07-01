import numpy as np
from numba import jit

from Compression import compression
from Gridding import gridding


@jit(nopython=True)
def create_instr(start_data, squares_size):
    main_grid = gridding(start_data, squares_size)
    big_grid = gridding(start_data, squares_size * 2)
    comp_grid = compression(big_grid, 2)

    main_size = len(main_grid)
    comp_size = main_size // 2

    instruction = np.zeros((main_size, main_size, 2), dtype=np.uint8)
    deviations = np.zeros((main_size, main_size), dtype=np.float32)

    # loop through main grid
    for i in range(main_size):
        for j in range(main_size):
            min_error = 100000

            # loop through comp grid
            for k in range(comp_size):
                for l in range(comp_size):
                    prop = main_grid[i, j].mean() / \
                        (comp_grid[k, l].mean() + 1)

                    cur_deviation = comp_grid[k, l] * prop - main_grid[i, j]

                    error = np.sum(cur_deviation**2)

                    if error < min_error:
                        min_error = error
                        instruction[i, j, 0] = k
                        instruction[i, j, 1] = l
                        deviations[i, j] = prop

    return instruction, deviations
