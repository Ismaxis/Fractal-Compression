import numpy as np


class Cage:
    def __init__(self):
        self.Items = np.array()


def gridding(image, squares_size):
    grid_size = (len(image[0])//squares_size, len(image)//squares_size)
    output = np.zeros(grid_size, dtype=Cage)
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            slice = ((i * squares_size, (i + 1) * squares_size),
                     (j * squares_size, (j + 1) * squares_size))
            output[i, j] = image[(slice[0][0]):(
                slice[0][1]), (slice[1][0]):(slice[1][1])]

    return output


def creating_img(instruction, deviations, big_grid, WIN_SIZE, squares_size):
    data = np.zeros(WIN_SIZE)
    for k in range(len(instruction[0])):
        for l in range(len(instruction)):
            cage = big_grid[int(instruction[k, l, 0]),
                            int(instruction[k, l, 1])]

            for i in range(len(cage[0])):
                for j in range(len(cage)):
                    #color = cage[i, j] - deviations[k][l]
                    color = cage[i, j] - deviations[k][l][i][j]

                    if color < 0:
                        color = 0

                    elif color > 254:
                        color = 254

                    data[k*squares_size+i, l*squares_size+j] = color
    return data


def white_noise(WIN_SIZE):
    data = np.zeros(WIN_SIZE)
    for i in range(WIN_SIZE[0]):
        for j in range(WIN_SIZE[1]):
            data[i, j] = np.random.randint(0, 255)

    return data
