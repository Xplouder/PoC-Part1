"""
Unit tests for Yahtzee
"""
import unittest
import Yahtzee


class TestsYahtzee(unittest.TestCase):
    def test_expected_value(self):
        val = Yahtzee.expected_value((2, 2), 6, 2)
        self.assertEqual(5.83333333333, val)

    def test_gen_all_holds1(self):
        val = Yahtzee.gen_all_holds((1,))
        self.assertEqual({(), (1,)}, val)

    def test_gen_all_holds2(self):
        val = Yahtzee.gen_all_holds((5, 5))
        self.assertEqual({(5,), (), (5, 5)}, val)

    def test_gen_all_holds3(self):
        val = Yahtzee.gen_all_holds((4, 6))
        self.assertEqual({(4, 6), (), (6,), (4,)}, val)

    def test_gen_all_holds4(self):
        val = Yahtzee.gen_all_holds((1, 3, 5))
        self.assertEqual(
            {(1, 3), (1,), (3,), (1, 3, 5), (1, 5), (5,), (), (3, 5)}, val)

    def test_gen_all_holds5(self):
        val = Yahtzee.gen_all_holds((2, 2, 4))
        self.assertEqual({(), (2, 2), (2,), (2, 2, 4), (2, 4), (4,)}, val)

    def test_gen_all_holds6(self):
        val = Yahtzee.gen_all_holds((1, 1, 2, 2))
        self.assertEqual(
            {(1, 2), (1, 1, 2, 2), (1,), (1, 2, 2),
             (2,), (1, 1, 2), (), (2, 2), (1, 1)}, val)

    def test_gen_all_holds7(self):
        val = Yahtzee.gen_all_holds((2, 4, 6, 6))
        self.assertEqual(
            {(2, 6), (4, 6), (6, 6), (2,), (2, 4, 6), (4,), (2, 4, 6, 6), (),
             (6,), (2, 6, 6), (4, 6, 6), (2, 4)}, val)

    def test_score1(self):
        val = Yahtzee.score((1,))
        self.assertEqual(1, val)

    def test_score2(self):
        val = Yahtzee.score((4, 5))
        self.assertEqual(5, val)

    def test_score3(self):
        val = Yahtzee.score((3, 3, 3))
        self.assertEqual(9, val)

    def test_strategy(self):
        val = Yahtzee.strategy((1,), 6)
        self.assertEqual(3.5, (), val)


if __name__ == '__main__':
    unittest.main()
