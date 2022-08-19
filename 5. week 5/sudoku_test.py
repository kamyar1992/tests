import turtle
import time
import numpy as np
import random


def draw_grid(tortoise):

    # tortoise.hideturtle()
    # tortoise.speed(0)
    direction = 1
    tortoise.penup()
    tortoise.goto(-N * W / 2, -N * W / 2)
    tortoise.pendown()

    tortoise.pensize(5)
    for i in range(4):
        tortoise.forward(N * W)
        tortoise.left(90)

    for i in range(N):
        if i in range(0, 10, 3):
            tortoise.pensize(3)
        else:
            tortoise.pensize(1)

        tortoise.forward(N * W)
        tortoise.left(90 * direction)
        tortoise.forward(W)
        tortoise.left(90 * direction)
        direction = -1 * direction

    direction = 1

    for i in range(N):
        if i in range(2, 10, 3):
            tortoise.pensize(3)
        else:
            tortoise.pensize(1)

        tortoise.forward(W)
        tortoise.left(90 * direction)
        tortoise.forward(N * W)
        direction = -1 * direction
        tortoise.left(90 * direction)


def goto_xy(tortoise, x, y):  # top left means x = 0 and y = 0

    tortoise.penup()
    tortoise.setposition(-(N / 2 - (x + 0.5)) * W, (N / 2 - (y + 1.8 * ratio / 10)) * W)
    #  : I can not figure out how set the position it was done


def write_number(tortoise, num, x, y, color='black'):

    goto_xy(tortoise, x, y)
    tortoise.color(color)
    if num:
        tortoise.write(num, move=False, align='center', font=("Verdana", 4 * ratio, "normal"))


def check_rc(grid, rc, orientation='r'):
    """
    :param grid: take a matrix grid with all zero elements
    :param rc:  give row and column of the cells of the matrix
    :param orientation: check the matrix in row or column
    :return:
    """

    possible_values = set(range(1, 10))
    if orientation == 'r':
        available_choices = possible_values - set(grid.tolist()[rc])  # numpy does not convert to a set directly
        # you have to make it to a list the make it to a set

    elif orientation == 'c':
        columns = list(zip(*grid.tolist()))   # make column of the grid matrix
        available_choices = possible_values - set(columns[rc])

    else:
        available_choices = set()

    return available_choices


def check_square(grid, square_index):

    c = (square_index % 3) * 3  # column
    r = (square_index // 3) * 3  # row
    square = grid[r: r + 3, c: c + 3]
    possible_values = set(range(1, 10))
    available_choices = possible_values - set(sum(square.tolist(), []))
    return available_choices


def initialise(tortoise):  # make a matrix grid with all zero elements

    rows, cols = (N, N)
    # grid = [[0] * cols] * rows
    grid = np.zeros((rows, cols), dtype=int)
    tortoise.clear()
    return grid


def calculate_grid(tortoise):

    grid = initialise(tortoise)
    rc = 0

    while rc - 81:
        row = rc // 9
        col = rc % 9

        si = col // 3 if row < 3 else 3 + col // 3 if row < 6 else 6 + col // 3 if row < 9 else None

        available_square_options = check_square(grid, si)
        available_row_options = check_rc(grid, row, orientation='r')
        available_column_options = check_rc(grid, col, orientation='c')

        if not grid[row, col]:
            candidates = available_square_options.intersection(
                available_row_options).intersection(available_column_options)

            if candidates:
                grid[row, col] = random.choice(list(candidates))
                write_number(tortoise, grid[row, col], col, row)
                rc += 1
            else:
                rc = 0
                grid = initialise(tortoise)

    return grid


if __name__ == "__main__":
    N = 9
    W = 40
    ratio = W // 8
    turtle.tracer(0)
    # t1 = turtle.Turtle()
    # t1.speed(0)
    # turtle.speed(10)
    # draw_grid(t1)
    t2 = turtle.Turtle()

    # write_number(t2, 5, 5, 5)

    print(np.zeros((3, 3, 3, 3), dtype=int))
    # print(calculate_grid(t2))
    turtle.exitonclick()
