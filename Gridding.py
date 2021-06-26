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


def creating_img(instruction, big_grid, WIN_SIZE):
    data = np.zeros(WIN_SIZE)
    for k in range(len(instruction[0])):
        for l in range(len(instruction)):
            cage = big_grid[int(instruction[k, l, 0]),
                            int(instruction[k, l, 1])]
            deviation = instruction[k, l, 2]

            for i in range(len(cage[0])):
                for j in range(len(cage)):
                    data[k*10+i, l*10+j] = cage[i, j] - deviation[i, j]

    return data


def white_noise(WIN_SIZE):
    data = np.zeros(WIN_SIZE)
    for i in range(WIN_SIZE[0]):
        for j in range(WIN_SIZE[1]):
            data[i, j] = np.random.randint(0, 255)

    return data
