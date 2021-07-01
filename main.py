import numpy as np
from PIL import Image

from Compression import compression
from Gridding import gridding
from Instruction import create_instr
from Recovery import recovery


# import image
image = Image.open("images\svt.png")
image = image.convert('L')

start_data = np.asarray(image)

# global variables
WIN_SIZE = len(start_data)
SQUARES_SIZE = 10

# compression
instruction, deviations = create_instr(start_data, SQUARES_SIZE)

# recovery
recovered = np.random.randint(0, 255, (WIN_SIZE, WIN_SIZE))

for i in range(10):
    big_grid = compression(gridding(recovered, SQUARES_SIZE * 2), 2)

    recovered = recovery(instruction, deviations,
                         big_grid, WIN_SIZE, SQUARES_SIZE)

    print(f'{i + 1} iteration')

Image.fromarray(recovered).convert('RGB').save("result.png")
