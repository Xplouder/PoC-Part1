"""
Unit tests for Yahtzee
"""
import unittest
import Yahtzee


class TestsYahtzee(unittest.TestCase):
    def test_expected_value1(self):
        expected_result = Yahtzee.expected_value((2, 2), 6, 2)
        self.assertAlmostEqual(5.83333333333, expected_result)

    def test_expected_value2(self):
        expected_result = Yahtzee.expected_value((2, 2), 2, 2)
        self.assertAlmostEqual(6, expected_result)

    def test_gen_all_holds1(self):
        expected_result = Yahtzee.gen_all_holds((1,))
        self.assertEqual({(), (1,)}, expected_result)

    def test_gen_all_holds2(self):
        expected_result = Yahtzee.gen_all_holds((5, 5))
        self.assertEqual({(5,), (), (5, 5)}, expected_result)

    def test_gen_all_holds3(self):
        expected_result = Yahtzee.gen_all_holds((4, 6))
        self.assertEqual({(4, 6), (), (6,), (4,)}, expected_result)

    def test_gen_all_holds4(self):
        expected_result = Yahtzee.gen_all_holds((1, 3, 5))
        self.assertEqual(
            {(1, 3), (1,), (3,), (1, 3, 5), (1, 5), (5,), (), (3, 5)},
            expected_result)

    def test_gen_all_holds5(self):
        expected_result = Yahtzee.gen_all_holds((2, 2, 4))
        self.assertEqual({(), (2, 2), (2,), (2, 2, 4), (2, 4), (4,)},
                         expected_result)

    def test_gen_all_holds6(self):
        expected_result = Yahtzee.gen_all_holds((1, 1, 2, 2))
        self.assertEqual(
            {(1, 2), (1, 1, 2, 2), (1,), (1, 2, 2),
             (2,), (1, 1, 2), (), (2, 2), (1, 1)}, expected_result)

    def test_gen_all_holds7(self):
        expected_result = Yahtzee.gen_all_holds((2, 4, 6, 6))
        self.assertEqual(
            {(2, 6), (4, 6), (6, 6), (2,), (2, 4, 6), (4,), (2, 4, 6, 6), (),
             (6,), (2, 6, 6), (4, 6, 6), (2, 4)}, expected_result)

    def test_gen_all_holds8(self):
        expected_result = Yahtzee.gen_all_holds(tuple([]))
        self.assertEqual({()}, expected_result)

    def test_gen_all_holds9(self):
        expected_result = Yahtzee.gen_all_holds(tuple([2, 4]))
        self.assertEqual({(), (2,), (4,), (2, 4)}, expected_result)

    def test_gen_all_holds10(self):
        expected_result = Yahtzee.gen_all_holds(tuple((3, 3, 3)))
        self.assertEqual({(), (3,), (3, 3), (3, 3, 3)}, expected_result)

    def test_gen_all_holds11(self):
        expected_result = Yahtzee.gen_all_holds(tuple((1, 2, 2)))
        self.assertEqual({(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)},
                         expected_result)

    def test_gen_all_holds12(self):
        expected_result = Yahtzee.gen_all_holds(tuple([2, 3, 6]))
        self.assertEqual(
            {(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)},
            expected_result)

    def test_score1(self):
        expected_result = Yahtzee.score((1,))
        self.assertEqual(1, expected_result)

    def test_score2(self):
        expected_result = Yahtzee.score((4, 5))
        self.assertEqual(5, expected_result)

    def test_score3(self):
        expected_result = Yahtzee.score((3, 3, 3))
        self.assertEqual(9, expected_result)

    def test_strategy(self):
        expected_result = Yahtzee.strategy((1,), 6)
        self.assertEqual((3.5, ()), expected_result)


if __name__ == '__main__':
    unittest.main()
