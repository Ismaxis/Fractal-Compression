import pygame as pg


# image is an array of black and white image
def draw(win, image):
    size = (len(image[0]), len(image))

    for j in range(size[1]):
        for i in range(size[0]):
            color = [int(image[j, i])] * 3
            pg.draw.line(win, color, (i, j), (i, j))

    pg.display.update()
