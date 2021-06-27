import numpy as np


class Cage:
    def __init__(self, coords, deviation):
        self.coords = np.array(coords)
        self.dev = deviation


def create_instr(main_grid, comp_grid, squares_size):
    main_size = len(main_grid)
    comp_size = main_size // 2

    instruction = np.zeros((main_size, main_size, 2))
    deviations = []

    # loop through main grid
    for i in range(main_size):
        deviations.append([])
        for j in range(main_size):
            # deviations[i].append(0)
            deviations[i].append([])

            for hpix in range(squares_size):
                deviations[i][j].append([])
                for vpix in range(squares_size):
                    deviations[i][j][hpix].append(0)

            cur_main_cage = main_grid[i, j]
            min_error = 1000
            # loop through comp grid
            for k in range(comp_size):
                for l in range(comp_size):
                    deviation = cur_main_cage - comp_grid[k, l]

                    error = np.average(deviation**2)

                    if error < min_error:
                        min_error = error
                        instruction[i, j] = np.array([k, l])
                        #deviations[i][j] = np.average(deviation)
                        # loop throught pixels

                        for hpix in range(squares_size):
                            for vpix in range(squares_size):
                                deviations[i][j][hpix][vpix] = deviation[hpix][vpix]

    return instruction, deviations
