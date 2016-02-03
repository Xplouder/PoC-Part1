"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
try:
    import codeskulptor
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import YahtzeeTestSuite as poc_holds_testsuite

codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    :param length:
    :param outcomes:
    """

    answer_set = {()}
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    :param hand: full yahtzee hand
    :return an integer score
    """

    # # Initial solution implementation using a single loop
    # max_score = 0
    # die_face_score = 0
    # die_face = 0
    #
    # for elem in hand:
    #     if elem > die_face:
    #         die_face = elem
    #         die_face_score = die_face
    #     elif elem == die_face:
    #         die_face_score += die_face
    #
    #     if die_face_score > max_score:
    #         max_score = die_face_score
    #
    # return max_score

    # Implementation using a dictionary however with more resources cost
    distinct_hand_elements = {}
    for hand_elem in hand:
        distinct_hand_elements[hand_elem] = 0

    for hand_elem in distinct_hand_elements:
        distinct_hand_elements[hand_elem] = hand.count(hand_elem) * hand_elem

    return max(distinct_hand_elements.values()) if \
        len(distinct_hand_elements.values()) > 0 else 0


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    :param held_dice: number of dice to be rolled
    :param num_die_sides: number of sides on each die
    :param num_free_dice: dice that you will hold
    :return a floating point expected value
    """
    total = score(held_dice)
    counter = 1

    for turn in range(num_free_dice):
        for possible_hand in gen_all_sequences(held_dice, turn):
            total += score(possible_hand)
            counter += 1
    return total / counter


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    :param hand: full yahtzee hand
    :return a set of tuples, where each tuple is dice to hold
    """

    all_holds = {()}
    for idx in range(len(hand) + 1):
        all_holds.add(hand[:idx])
        all_holds.add(hand[idx:])

        temp = gen_all_sequences(hand, idx)
        for elem in temp:
            sorted_elem = tuple(sorted(elem))
            if has_valid_number_of_occurrences(hand, sorted_elem):
                all_holds.add(sorted_elem)
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    :param num_die_sides: number of sides on each die
    :param hand: full yahtzee hand
    :return a tuple where the first element is the expected score and the second
     element is a tuple of the dice to hold
    """
    return 0.0, ()


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, \
        "with expected score", hand_score


def has_valid_number_of_occurrences(original, vector):
    """
    Ensure that vector has ALWAYS the same or less number of each element
    comparatively with original list
    :param original: primary vector with original set of elements
    :param vector: secondary vector formed from original
    :return: says if vector's elements has same number occurrences in original
    """
    for hand_elem in original:
        if original.count(hand_elem) < vector.count(hand_elem):
            return False
    return True

# run_example()

# print gen_all_sequences((1, 2, 3, 4, 5, 6), 5)

# poc_holds_testsuite.run_suite(gen_all_holds)
