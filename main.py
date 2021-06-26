import pygame as pg
from PIL import Image
import numpy as np
from Draw import draw
from Gridding import gridding, creating_img, white_noise
from Compression import compression
from Instruction import create_instr


image = Image.open("images\woman.png")
image = image.convert('L')

start_data = np.asarray(image)

WIN_SIZE = (len(start_data[0]), len(start_data))
WIN = pg.display.set_mode(WIN_SIZE)

# first cycle with creating instruction for recovery
small_grid = gridding(start_data, (10, 10))
big_grid = compression(gridding(start_data, (20, 20)))

instruction = create_instr(small_grid, big_grid)

img = white_noise(WIN_SIZE)

# recovery cycles
for i in range(100):
    big_grid = compression(gridding(img, (20, 20)))

    img = creating_img(instruction, big_grid, WIN_SIZE)

    print(f'{i} iteration')
    draw(WIN, img)

image = Image.fromarray(img)

image = image.convert('RGB')

image.save("result.png")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
