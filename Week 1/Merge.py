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
            if newline[index] != 0 and newline[index] == newline[
                        index + 1] != 0:
                newline[index] *= 2
                newline[index + 1] = 0
                newline = shift(newline)

    return newline


def can_merge(line):
    """
    Function that informs if is still possible merge the line
    :param line: array of elements
    :return: boolean
    """
    aux = -1
    for index in range(len(line)):
        if index == 0:
            aux = line[index]
        else:
            if aux == line[index] and line[index] != 0:
                return True
            else:
                aux = line[index]

    return False


def can_shift(array):
    """
    Function that informs if the array can be shifted
    :param array: elements list
    :return: boolean
    """

    has_first_non_zero = False
    first_non_zero_index = -1
    has_consecutive_zero = False
    has_last_non_zero = False

    for i in range(len(array)):
        if array[i] != 0:
            if not has_first_non_zero:
                has_first_non_zero = True
                first_non_zero_index = i
                continue
            if has_consecutive_zero:
                has_last_non_zero = True
        else:
            if first_non_zero_index < i:
                has_consecutive_zero = True

        if has_first_non_zero and has_consecutive_zero and has_last_non_zero:
            return True

    return False


def shift(array):
    """
    Function that remove the element from array index position and append a zero
    :param array: elements list
    :return: new array of elements after the shift
    """

    has_first_non_zero = False
    first_non_zero_index = -1

    for i in range(len(array)):
        if array[i] != 0:
            if not has_first_non_zero:
                has_first_non_zero = True
                first_non_zero_index = i
                continue
        else:
            if first_non_zero_index < i:
                array = array[0:i] + array[i + 1:len(array)]
                array.append(0)
    return array
