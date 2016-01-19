"""
Clone of 2048 game.
"""

import random

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0), DOWN: (-1, 0), LEFT: (0, 1), RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    :param line: array with elements
    :return: new array of elements after the merge operation
    """

    newline = shift(list(line))

    for index in range(len(newline)):
        if index + 1 < len(newline):
            if newline[index] != 0 \
                    and newline[index] == newline[index + 1] != 0:
                newline[index] *= 2
                newline[index + 1] = 0
                newline = shift(newline)

    return newline


def shift(array):
    """
    Function that remove the zeros from array after it append them at the end
    :param array: elements list
    :return: new array of elements after the shift
    """

    total_zeros_counter = 0

    while True:
        zeros_counter = 0
        for index in range(len(array)):
            if array[index] == 0:
                del array[index]
                zeros_counter += 1
                break
        total_zeros_counter += zeros_counter

        if zeros_counter == 0:
            break

    for index in range(total_zeros_counter):
        array.append(0)

    return array


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = None
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0] * self.width for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = 0

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = "["
        for row in range(self.height):
            if row == 0:
                result += str(self.grid[row]) + "\n"
            elif row == self.height - 1:
                result += " " + str(self.grid[row]) + "]"
            else:
                result += " " + str(self.grid[row]) + "\n"
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add a new tile if any
        tiles moved.
        :param direction: direction of the move over the grid
        """

        if direction == UP:
            self.traverse_grid((0, 0), OFFSETS[UP], self.height)
        elif direction == DOWN:
            self.traverse_grid((0, 0), OFFSETS[DOWN], self.height)
        elif direction == LEFT:
            self.traverse_grid((0, 0), OFFSETS[LEFT], self.width)
        elif direction == RIGHT:
            self.traverse_grid((0, 0), OFFSETS[RIGHT], self.width)

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        random_num = random.randint(0, 10)
        new_tile_value = 4 if random_num > 9 else 2

        rand_tile_column_idx = random.randrange(0, self.width)
        rand_tile_row_idx = random.randrange(0, self.height)
        rand_tile = self.get_tile(rand_tile_row_idx, rand_tile_column_idx)

        while rand_tile != 0:
            rand_tile_column_idx = random.randrange(0, self.width)
            rand_tile_row_idx = random.randrange(0, self.height)
            rand_tile = self.get_tile(rand_tile_row_idx, rand_tile_column_idx)

        self.set_tile(rand_tile_row_idx, rand_tile_column_idx, new_tile_value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        :param value: tile value
        :param col: column index
        :param row: row index
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        :param col: column index
        :param row: row index
        """
        return self.grid[row][col]

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid in a linear direction
        :param num_steps: number of iterations
        :param direction: tuple that contains difference between consecutive
        cells in the traversal
        :param start_cell: tuple(row, col) denoting the starting cell
        """

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
