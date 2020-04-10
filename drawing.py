import numpy as np
import cube as rubiks
from graphics import *

def draw_cube(rects, win):
    for i in range(3):
        for j in range(3):
            rects[i, j].draw(win)


def getcolor(n):
    if n == 0:
        return color_rgb(255, 255, 255)
    if n == 1:
        return color_rgb(255, 100, 0)
    if n == 2:
        return color_rgb(0, 255, 0)
    if n == 3:
        return color_rgb(255, 0, 0)
    if n == 4:
        return color_rgb(0, 0, 255)
    if n == 5:
        return color_rgb(253, 208, 35)


def set_colors(cube, rects):
    face = cube.sides[2]
    for i in range(3):
        for j in range(3):
            rects[i, j].setFill(getcolor(face[i, j]))
    return rects


def draw():
    cube1 = rubiks.Cube(3)
    cube2 = rubiks.Cube(3)

    win = GraphWin("My Circle", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    arr = [[None, None, None], [None, None, None], [None, None, None]]
    rects = np.array(arr, dtype=Rectangle)
    for i in range(3):
        for j in range(3):
            rects[i, j] = Rectangle(Point(100 * (j + 1), 100 * (i + 1)), Point(100 * (j + 2), 100 * (i + 2)))

    rects = set_colors(cube1, rects)
    draw_cube(rects, win)
    #cube1.scramble("uDLF")
    #cube2.scramble("uDLF")
    rects = set_colors(cube1, rects)
    cube2.scramble("FDr")
    cube1.solve3moves(cube2)
    a = None
    while a != -1:
        a = input()
        cube1.scramble(a)
        rects = set_colors(cube1, rects)
    win.getMouse()
    win.close()
