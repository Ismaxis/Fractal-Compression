import numpy as np


class Cage:
    def __init__(self):
        self.Items = np.array()


def gridding(image, squares_size):
    grid_size = (len(image[0])//squares_size[0], len(image)//squares_size[1])
    output = np.zeros(grid_size, dtype=Cage)
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            g = image[0:20, 0:20]
            slice = ((i * squares_size[0], (i + 1) * squares_size[0]),
                     (j * squares_size[0], (j + 1) * squares_size[0]))
            output[i, j] = image[(slice[0][0]):(
                slice[0][1]), (slice[1][0]):(slice[1][1])]

    return output
