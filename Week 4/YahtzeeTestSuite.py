"""
Test suite for gen_all_holds in "Yahtzee"
"""

from aux import TestSuite as poc_simpletest


def run_suite(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    :param gen_all_holds:
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test gen_all_holds on various inputs
    hand = tuple([])
    suite.run_test(gen_all_holds(hand), {()}, "Test #1:")

    hand = tuple([2, 4])
    suite.run_test(gen_all_holds(hand), {(), (2,), (4,), (2, 4)}, "Test #2:")

    hand = tuple((3, 3, 3))
    suite.run_test(gen_all_holds(hand), {(), (3,), (3, 3), (3, 3, 3)},
                   "Test #4:")

    hand = tuple((1, 2, 2))
    suite.run_test(gen_all_holds(hand),
                   {(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)},
                   "Test #3:")

    hand = tuple([2, 3, 6])
    suite.run_test(gen_all_holds(hand),
                   {(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)},
                   "Test #5:")

    suite.report_results()
