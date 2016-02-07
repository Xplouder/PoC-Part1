"""
Assessment of test case coverage for merge() (Homework 4)
"""


def merge_original(line):
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


# ------------------------------------------------------------------------------

# Another (wrong) implementations of merge function

def merge1(line):
    ret_list = []
    tmp_line = list(line)
    for i in (0, len(line)):
        ret_list.append(0)
    return ret_list


def merge4(line):
    return [0, 0, 0, 0]


def merge18(line):
    result = [0 for numbers in line]
    for x in line:
        if line[x] != 0:
            print line[x]
            result[x] = line[x]
    return result


def merge12(line):
    result = [0, 0, 0, 0]
    for i in range(len(line)):
        if (line[i] != 0) and (i < 3):
            result[(i + 1)] = line[i]
        elif line[i] != 0:
            result[0] = line[i]
    return result


def merge35(line):
    place = 0
    result = [0, 0, 0, 0]
    for i in line:
        if i != 0:
            result[place] = i
            (+ (+ place))
    return result


def merge57(line):
    merged_line = []
    for index in range(len(line)):
        if index == 0:
            merged_line.append(line[index])
        elif (line[index] == merged_line[(-1)]) or (merged_line[(-1)] == 0):
            merged_line[(-1)] += line[index]
    while len(merged_line) != 4:
        merged_line.append(0)
    return merged_line


def merge127(line):
    n = len(line)
    newline = ([0] * n)
    i = 0
    for j in range(0, n):
        if line[j] != 0:
            if i == 0:
                newline[i] = line[j]
                i += 1
            elif line[j] == newline[(i - 1)]:
                newline[(i - 1)] += line[j]
                i += 1
            else:
                newline[i] = line[j]
    return newline


def merge130(line):
    if len(line) == 1:
        return line
    first = 0
    second = 0
    line2 = []
    while first < len(line):
        if line[first] != 0:
            line2.append(line[first])
        first += 1
    while len(line2) < len(line):
        line2.append(0)
    line3 = []
    first = 0
    second = 1
    while first < len(line2):
        if line2[first] == line2[second]:
            line3.append((line2[first] * 2))
        else:
            line3.append(line2[first])
            line3.append(line2[second])
        first += 2
        second += 2
        if second >= len(line):
            line3.append(line2[(-1)])
    while len(line3) < len(line):
        line3.append(0)
    return line3


def merge159(line):
    result = ([0] * len(line))
    merged_tiles = ([False] * len(line))
    for idx in range(len(line)):
        if line[idx] != 0:
            if idx == 0:
                result[0] = line[idx]
            else:
                for i in range(idx):
                    if result[i] == 0:
                        result[i] = line[idx]
                        if ((result[i] == result[(i - 1)]) and (
                                    merged_tiles[(i - 1)] == False)):
                            result[(i - 1)] = (2 * result[(i - 1)])
                            result[i] = 0
                            merged_tiles[(i - 1)] = True
                        break
    return result
    return []


def merge189(line):
    line1 = []
    line2 = []
    for i in range(4):
        if line[i] != 0:
            line1.append(line[i])
        else:
            pass
    while len(line1) < 4:
        line1.append(0)
    y = 0
    while y < (len(line1) - 1):
        if line1[y] == line1[(y + 1)]:
            line2.append((line1[y] + line1[(y + 1)]))
            y = (y + 2)
        else:
            line2.append(line1[y])
            y += 1
    while len(line2) < 4:
        line2.append(0)
    return line2


def merge209(line):
    head = 0
    for tail in xrange(1, len(line)):
        if line[tail] == 0:
            continue
        if line[head] == 0:
            line[head] = line[tail]
        elif line[head] == line[tail]:
            line[head] += line[tail]
            head += 1
        else:
            head += 1
            line[head] = line[tail]
        line[tail] = 0
    return line


def merge233(line):
    working_list = [0, 0, 0, 0]
    result_list = [0, 0, 0, 0]
    j = 0
    for i in range(len(line)):
        if line[i] != 0:
            working_list[j] = line[i]
            j = (j + 1)
    for i in range(len(working_list)):
        if working_list[(i - 1)] == working_list[i]:
            working_list[(i - 1)] += working_list[i]
            working_list[i] = 0
    k = 0
    for i in range(len(working_list)):
        if working_list[i] != 0:
            result_list[k] = working_list[i]
            k = (k + 1)
    return result_list


def merge238(line):
    result_list = [0, 0, 0, 0]
    acc = 0
    already_merged = False
    for entry in line:
        if entry > 0:
            result_list[acc] = entry
            acc += 1
        else:
            acc += 0
    for i in range(1, (len(result_list) - 1)):
        if (result_list[i] == result_list[(i - 1)]) and (not already_merged):
            result_list[(i - 1)] += result_list[i]
            already_merged = True
            result_list.append(0)
            result_list.pop(i)
    return result_list


def merge239(line):
    resultlist = [0, 0, 0, 0]
    pos_resultlist = 0
    for i in range(len(line)):
        if line[i] != 0:
            if i < (len(line) - 1):
                if line[i] == line[(i + 1)]:
                    line[i] += line[i]
                    line[(i + 1)] = 0
            resultlist[pos_resultlist] = line[i]
            pos_resultlist += 1
    return resultlist


def merge242(line):
    result_list = [0, 0, 0, 0]
    acc = 0
    already_merged = False
    for entry in line:
        if entry > 0:
            result_list[acc] = entry
            acc += 1
        else:
            acc += 0
    for i in range(1, (len(result_list) - 1)):
        if (result_list[i] == result_list[(i - 1)]) and (not already_merged):
            result_list[(i - 1)] += result_list[i]
            result_list.append(0)
            result_list.pop(i)
    return result_list


def merge254(line):
    while 0 in line:
        line.remove(0)
    for i in range(len(line)):
        print (i, line)
        if ((i + 1) < len(line)) and (line[i] == line[(i + 1)]):
            line[i] = (line[i] + line[i])
            line = (line[:(i + 1)] + line[(i + 2):])
    line += [0, 0, 0, 0]
    return line[:4]


def merge259(line):
    merged = ([val for val in line if val] + [val for val in line if (not val)])
    index = 0
    while index in range(0, len(merged)):
        if merged[index] == merged[(index + 1)]:
            merged[index] *= 2
            merged[(index + 1)] = 0
            index += 2
        else:
            index += 2
    return (
        [val for val in merged if val] + [val for val in merged if (not val)])


def merge286(line):
    result = []
    line_before = []
    for item in line:
        if item != 0:
            line_before.append(item)
    while len(line_before) < len(line):
        line_before.append(0)
    i = 0
    line_length = len(line_before)
    while i < line_length:
        if (i + 1) == 4:
            result.append(line_before[i])
            i += 1
        elif line_before[i] == line_before[(i + 1)]:
            result.append((line_before[i] * 2))
            i += 2
        elif line_before[i] != line_before[(i + 1)]:
            result.append(line_before[i])
            i += 1
    while len(result) < len(line):
        result.append(0)
    return result


def merge300(line):
    idx = 0
    jdx = 0
    kdx = 0
    ldx = 0
    line_len = len(line)
    entry = line[:]
    swap = entry[:]
    for idx in range(line_len):
        entry[idx] = 0
    for idx in range(len(line)):
        if line[idx] != 0:
            entry[jdx] = line[idx]
            jdx += 1
    idx = 0
    jdx = (idx + 1)
    while jdx < line_len:
        if (entry[idx] == entry[jdx]) and (entry[idx] != 0):
            entry[idx] += entry[jdx]
            entry[jdx] = 0
            for ldx in range(line_len):
                swap[ldx] = 0
            ldx = 0
            for kdx in range(len(entry)):
                if entry[kdx] != 0:
                    swap[ldx] = entry[kdx]
                    ldx += 1
        else:
            idx += 1
            jdx = (idx + 1)
    return swap


def merge306(line):
    compare = []
    squeeze = []
    zeroes = []
    for i in line:
        if i == 0:
            zeroes.append(0)
    if 0 not in line:
        line.append(0)
        line.append(0)
    for j in line:
        if j == 0:
            line.remove(j)
            line.append(j)
    while line != []:
        if compare == []:
            compare.append(line[0])
            if line == [0]:
                break
            compare.append(line[1])
            line.pop(0)
            line.pop(0)
        if len(compare) == 1:
            squeeze.append(compare[0])
        if compare[0] == compare[1]:
            if compare[0] != 0:
                squeeze.append((compare[0] + compare[1]))
                compare = []
                zeroes.append(0)
            elif compare[0] == 0:
                compare = []
        elif compare[0] != compare[1]:
            squeeze.append(compare[0])
            compare.pop(0)
            if line != []:
                compare.append(line[0])
                line.pop(0)
    squeeze.extend(zeroes)
    line = squeeze
    return line


def merge324(line):
    list1 = []
    list2 = []
    for num_line in line:
        if (num_line != 0) and (len(list1) < 4):
            list1.append(num_line)
    for i in range((len(line) - len(list1))):
        list1.append(0)
    for index_list1 in range(len(list1)):
        if ((index_list1 < (len(list1) - 1)) and (list1[index_list1] != 0) and (
                    list1[index_list1] == list1[(index_list1 + 1)])):
            list1[index_list1] = (list1[index_list1] * 2)
            list1[(index_list1 + 1)] = 0
    for i in list1:
        if (i != 0) and (len(list2) < 4):
            list2.append(i)
    for i in range((len(list1) - len(list2))):
        list2.append(0)
    return list2


def merge326(line):
    maxline = len(line)
    # inverse line order and put its 0 at the end
    for n in range(len(line))[::(-1)]:
        if line[n] is 0:
            line.append(line.pop(n))

    for n in range(len(line)):
        if (line[n] is not 0) and (line[(n + 1)] == line[n]):
            line[n] = (line[n] * 2)
            line.pop((n + 1))
            if len(line) < maxline:
                line.append(0)
    return line


def merge347(line):
    if any(line):
        merges = []
        for index in range((- len(line)), (-1)):
            if (line[(index + 1)] == line[index]) and line[index] and (
                    not (index in merges)):
                line[index] *= 2
                line[(index + 1)] = 0
                merges.append(index)
            elif (line[index] == 0) and (line[(index + 1)] != line[index]):
                while (line[index] == 0) and line[(index + 1)] and (
                            index >= (-4)):
                    line[index] = line[(index + 1)]
                    line[(index + 1)] = 0
                    if index > (-4):
                        if (line[index] == line[(index - 1)]) and (
                                not ((index - 1) in merges)):
                            line[(index - 1)] *= 2
                            line[index] = 0
                        index -= 1
    return line


def merge351(line):
    current_position = 0
    test_position = 1
    merged_line = []

    while current_position < (len(line) - 1):
        if line[current_position] == 0:
            current_position += 1
        else:
            test_position = (current_position + 1)
            if line[test_position] == 0:
                test_position += 1
            if line[current_position] == line[test_position]:
                line[current_position] = (2 * line[current_position])
                line[test_position] = 0
                current_position = (test_position + 1)
            else:
                current_position = test_position
    for dummy in line:
        if dummy != 0:
            merged_line.append(dummy)
    while len(merged_line) < len(line):
        merged_line.append(0)
    return merged_line


def merge352(line):
    size = len(line)
    res_list = ([0] * size)
    if size == 1:
        return line
    linecounter = 0
    line1counter = 1
    res_counter = 0
    line1 = line
    while line1counter < len(line):
        if (line[linecounter] == line1[line1counter]) and (
                    line[linecounter] != 0):
            new_var = (line[linecounter] + line1[line1counter])
            res_list[res_counter] = new_var
            linecounter += 1
            if line[linecounter] == 0:
                linecounter += 1
            line1counter += 1
            if (line1counter + 1) == len(line):
                res_counter += 1
                res_list[res_counter] = line[line1counter]
        elif (line[linecounter] != 0) and (line[line1counter] != 0):
            res_list[res_counter] = line[linecounter]
            if (line1counter + 1) == len(line):
                res_counter += 1
                res_list[res_counter] = line[line1counter]
        else:
            if (line[linecounter] == 0) and (line[line1counter] == 0):
                linecounter += 1
                line1counter += 1
                res_counter -= 1
            elif line[linecounter] == 0:
                res_counter -= 1
            elif line[line1counter] == 0:
                linecounter -= 1
                res_counter -= 1
            if (line1counter + 1) == len(line):
                res_counter += 1
                if line[linecounter] == 0:
                    res_list[res_counter] = line[line1counter]
                if line[line1counter] == 0:
                    linecounter += 1
                    res_list[res_counter] = line[linecounter]
        linecounter += 1
        line1counter += 1
        res_counter += 1
    return res_list


def merge355(line):
    lst = []
    index = 0
    merged = False
    for dummy_x in range(len(line)):
        lst.append(0)
    for num in line:
        if num != 0:
            if (lst[(index - 1)] != num) and (not merged):
                lst[index] = num
                index += 1
            elif (lst[(index - 1)] != num) and merged:
                lst[(index - 1)] = num
            elif lst[(index - 1)] == num:
                lst[(index - 1)] += num
                index += 1
                merged = True
    return lst


def merge360(line):
    for count in range(0, (len(line) - 1)):
        if line[count] == 0:
            line.insert(len(line), line[count])
            line.remove(line[count])
        if line[count] == line[(count + 1)]:
            line[count] += line[count]
            line[(count + 1)] = 0
    return line


def merge364(line):
    result_line = []
    ind = 0
    summa = False
    for index in range(len(line)):
        result_line.append(0)
    for number in line:
        if number > 0:
            result_line.insert(ind, number)
            result_line.pop()
            ind += 1
    for index_res in range(1, (len(result_line) - 1)):
        if result_line[index_res] == result_line[(index_res - 1)]:
            if summa == False:
                result_line.insert((index_res - 1),
                                   (result_line[index_res] * 2))
                result_line.remove(result_line[index_res])
                result_line.remove(result_line[index_res])
                result_line.append(0)
                summa = True
                if result_line[index_res] == result_line[(index_res + 1)]:
                    summa = False
    return result_line
