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

    while True:
        do_while_stop_flag = False
        element = -1
        index_temp = -1

        for index in range(len(newline)):
            if newline[index] == 0:
                if need_shift(index, newline):
                    # shift array and append a zero
                    newline = shift(index, newline)
                    break
            else:
                if element == newline[index]:
                    # merge elements, shift array and append a zero
                    newline[index_temp] *= 2
                    newline = shift(index, newline)
                    break
                else:
                    element = newline[index]
                    index_temp = index

            if index == len(newline) - 1:
                do_while_stop_flag = not can_merge(newline)

        if do_while_stop_flag:
            break

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


def need_shift(index, array):
    """
    Function that informs if shift is necessary i.e. there is a number different
    from zero after the index position
    :param array: elements list
    :param index: position from where we want to shift
    :return: boolean
    """
    result = False
    for i in range(len(array)):
        if i > index:
            result |= array[i] != 0

    return result


def shift(index, array):
    """
    Function that remove the element from array index position and append a zero
    :param array: elements list
    :param index: position from where we want to shift
    :return: new array of elements after the shift
    """
    if 0 <= index <= len(array) - 1:
        array = array[0:index] + array[index + 1:len(array)]
        array.append(0)

    return array
