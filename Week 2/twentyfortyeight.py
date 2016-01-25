"""
Clone of 2048 game.
"""

import random

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


def to_right(vector):
    """
    Anchor non zero numbers in a MERGED vector to the right side
    :param vector: initial vector
    :return: vector with non zeros at right side
    """
    if has_non_zero(vector):
        new_vector = list(vector)
        while new_vector[0] != 0:
            aux = new_vector.pop(0)
            new_vector.append(aux)
        return new_vector
    return vector


def has_non_zero(vector):
    """
    Returns saying if the input vector has an element > 0
    :param vector: initial vector
    :return: condition result
    """
    if len(vector) == 0:
        return False

    for elem in vector:
        if elem != 0:
            return True

    return False


def rotate_cw_matrix(matrix):
    """
    Rotate matrix clockwise
    :param matrix: input matrix
    :return: rotated matrix
    """
    aux = zip(*matrix[::-1])
    return [list(row) for row in aux]


def rotate_ccw_matrix(matrix):
    """
    Rotate matrix counter clockwise
    :param matrix: input matrix
    :return: rotated matrix
    """
    aux = zip(*matrix)[::-1]
    return [list(row) for row in aux]


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = None
        self.reset()

    def reset(self):
        """
        Reset the game so the _grid is empty except for two
        initial tiles.
        """
        self._grid = [[0] * self._width for _ in range(self._height)]
        for row in range(self._height):
            for col in range(self._width):
                self._grid[row][col] = 0

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the _grid for debugging.
        """
        result = "["
        for row in range(self._height):
            if row == 0:
                result += str(self._grid[row]) + "\n"
            elif row == self._height - 1:
                result += " " + str(self._grid[row]) + "]"
            else:
                result += " " + str(self._grid[row]) + "\n"
        return result

    def get_grid_height(self):
        """
        Get the _height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the _width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add a new tile if any
        tiles moved.
        :param direction: direction of the move over the _grid
        """
        initial_grid = self._grid

        if direction == UP:
            rotated_grid = rotate_ccw_matrix(self._grid)
            rotated_grid = [merge(row) for row in rotated_grid]
            self._grid = rotate_cw_matrix(rotated_grid)

        elif direction == DOWN:
            rotated_grid = rotate_cw_matrix(self._grid)
            rotated_grid = [merge(row) for row in rotated_grid]
            self._grid = rotate_ccw_matrix(rotated_grid)

        elif direction == LEFT:
            self._grid = [merge(row) for row in self._grid]

        elif direction == RIGHT:
            self._grid = [to_right(merge(row)) for row in self._grid]

        if initial_grid != self._grid:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if not self.is_grid_full():
            random_num = random.randint(0, 10)
            new_tile_value = 4 if random_num > 9 else 2

            while True:
                rand_column_idx = random.randrange(0, self._width)
                rand_row_idx = random.randrange(0, self._height)

                if self.get_tile(rand_row_idx, rand_column_idx) == 0:
                    self.set_tile(rand_row_idx, rand_column_idx, new_tile_value)
                    break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        :param value: tile value
        :param col: column index
        :param row: row index
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        :param col: column index
        :param row: row index
        """
        return self._grid[row][col]

    def is_grid_full(self):
        """
        Return if the grid has any empty (0) tile
        """
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    return False
        return True


game = TwentyFortyEight(4, 4)
print game

print "\n\nUP"
game.move(UP)
print game

print "\n\nDOWN"
game.move(DOWN)
print game

print "\n\nRIGHT"
game.move(RIGHT)
print game

print "\n\nLEFT"
game.move(LEFT)
print game

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
