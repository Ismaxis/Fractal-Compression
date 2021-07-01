import numpy as np
from numba import jit


@jit(nopython=True)
def recovery(instruction, deviations, big_grid, WIN_SIZE, squares_size):
    data = np.zeros((WIN_SIZE, WIN_SIZE), dtype=np.uint8)

    for k in range(len(instruction)):
        for l in range(len(instruction)):
            for i in range(squares_size):
                for j in range(squares_size):
                    color = big_grid[instruction[k, l, 0],
                                     instruction[k, l, 1]][i, j] * deviations[k, l]

                    if color < 0:
                        color = 0

                    elif color > 254:
                        color = 254

                    data[k*squares_size+i, l*squares_size+j] = color
    return data
