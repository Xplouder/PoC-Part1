"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    :param line: array with elements
    :return: new array of elements after the merge operation
    """
    newline = list(line)

    while can_shift(newline):
        newline = shift(newline)

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
    Function that remove the zeros and shift the right side to one left position
    and also append the removed 0 at the end
    :param array: elements list
    :return: new array of elements after the shift
    """

    has_first_non_zero = False
    first_non_zero_index = -1

    for index in range(len(array)):
        if array[index] != 0:
            if not has_first_non_zero:
                has_first_non_zero = True
                first_non_zero_index = index
                continue
        else:
            if first_non_zero_index < index:
                array = array[0:index] + array[index + 1:len(array)]
                array.append(0)
    return array


def can_shift(array):
    """
    Function that informs if the array can be shifted
    :param array: elements list
    :return: boolean
    """

    for index in range(len(array)):
        # limit protection
        if index - 1 >= 0:
            if array[index] != 0 and array[index - 1] == 0:
                return True

    return False
