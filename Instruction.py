import numpy as np


def create_instr(main_grid, comp_grid, squares_size):
    main_size = len(main_grid)
    comp_size = main_size // 2

    instruction = np.zeros((main_size, main_size, 3))

    # loop through main grid
    for i in range(main_size):
        for j in range(main_size):
            cur_main_cage = main_grid[i, j]
            min_error = 100000
            # loop through comp grid
            for k in range(comp_size):
                for l in range(comp_size):
                    prop = np.average(cur_main_cage) / \
                        np.average(comp_grid[k, l])

                    deviation = comp_grid[k, l] * prop - cur_main_cage

                    error = np.sum(deviation**2)

                    if error < min_error:
                        min_error = error
                        instruction[i, j] = np.array([k, l, prop])

    return instruction
