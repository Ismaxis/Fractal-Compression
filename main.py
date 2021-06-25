import pygame as pg
from PIL import Image
import numpy as np
from Draw import draw
from Gridding import gridding
from Compression import compression
from Compare import compare


image = Image.open("images\woman.png")
image = image.convert('L')

data = np.asarray(image)

WIN_SIZE = (len(data[0]), len(data))
WIN = pg.display.set_mode(WIN_SIZE)

small_grid = gridding(data, (10, 10))
big_grid = gridding(data, (20, 20))

big_grid = compression(big_grid)

instruction = compare(small_grid, big_grid)

# checking
data2 = np.zeros(WIN_SIZE)

'''
for k in range(len(big_grid[0])):
    for l in range(len(big_grid)):
        cage = big_grid[k, l]
        for i in range(len(cage[0])):
            for j in range(len(cage)):
                data2[k*10+i, l*10+j] = cage[i, j]
'''

for k in range(len(instruction[0])):
    for l in range(len(instruction)):
        cage = big_grid[int(instruction[k, l, 0]), int(instruction[k, l, 1])]
        for i in range(len(cage[0])):
            for j in range(len(cage)):
                data2[k*10+i, l*10+j] = cage[i, j]

draw(WIN, data2)

img = Image.fromarray(data2)

img = img.convert('RGB')

img.save("result.png")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
