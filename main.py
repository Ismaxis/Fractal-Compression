import numpy as np
from PIL import Image

from Compression import compression
from Gridding import gridding
from Instruction import create_instr
from Recovery import recovery


# import image
image = Image.open("images\\svt.png")
image = image.convert('L')

start_data = np.asarray(image)
del image

# global variables
WIN_SIZE = len(start_data)
SQUARES_SIZE = 5

# compression
instruction, deviations = create_instr(start_data, SQUARES_SIZE)
del start_data

# recovery
RECOVERY_SIZE = WIN_SIZE * 2
recovered = np.asarray(Image.open("images\white.png").convert('L'))

for i in range(10):
    big_grid = compression(
        gridding(recovered, SQUARES_SIZE * 2 * RECOVERY_SIZE//WIN_SIZE), 2)

    recovered = recovery(instruction, deviations,
                         big_grid, RECOVERY_SIZE, SQUARES_SIZE * RECOVERY_SIZE//WIN_SIZE)

Image.fromarray(recovered).convert('RGB').save("result.png")
