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
    sorted_hand = sorted(hand, reverse=True)

    iterate_val = None
    for elem in sorted_hand:
        iterate_val *= elem
    return iterate_val


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    :param num_free_dice: dice that you will hold
    :param num_die_sides: number of sides on each die
    :param held_dice: number of dice to be rolled
    :return a floating point expected value
    """
    return 0.0


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    :param hand: full yahtzee hand
    :return a set of tuples, where each tuple is dice to hold
    """

    all_holds = {()}
    for i in range(len(hand) + 1):
        all_holds.add(hand[:i])
        all_holds.add(hand[i:])

        temp = gen_all_sequences(hand, i)
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
