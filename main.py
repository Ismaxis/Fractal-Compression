import pygame as pg
from PIL import Image
import numpy as np
from Draw import draw
from Gridding import gridding, creating_img, upscale, white_noise, upscale
from Compression import compression
from Instruction import create_instr


image = Image.open("images\woman.png")
image = image.convert('L')

start_data = np.asarray(image)

WIN_SIZE = (len(start_data[0]), len(start_data))
WIN = pg.display.set_mode(WIN_SIZE)
SQUARES_SIZE = 10

# first cycle with creating instruction for recovery
small_grid = gridding(start_data, SQUARES_SIZE)
big_grid = compression(gridding(start_data, SQUARES_SIZE * 2), 2)

#img = compression(small_grid, 10)
#img = upscale(img, 500)
img = white_noise(WIN_SIZE)
draw(WIN, img)

instruction = create_instr(small_grid, big_grid, SQUARES_SIZE)

# recovery cycles
for i in range(7):
    big_grid = compression(gridding(img, SQUARES_SIZE * 2), 2)

    img = creating_img(instruction, big_grid, WIN_SIZE, SQUARES_SIZE)

    print(f'{i + 1} iteration')

    draw(WIN, img)

image = Image.fromarray(img)

image = image.convert('RGB')

image.save("result.png")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
