import numpy as np


def compare(main_grid, comp_grid):
    main_size = len(main_grid)
    comp_size = main_size // 2

    instruction = np.zeros((main_size, main_size, 2))

    # loop through main grid
    for i in range(main_size):
        for j in range(main_size):
            cur_main_cage = main_grid[i, j]
            min_error = 1000
            # loop through comp grid
            for k in range(comp_size):
                for l in range(comp_size):
                    deviation = cur_main_cage - comp_grid[k, l]
                    deviation = deviation**2

                    error = np.average(deviation)

                    if error < min_error:
                        min_error = error
                        instruction[i, j] = np.array([k, l])

    return instruction
