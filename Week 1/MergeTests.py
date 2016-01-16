"""
Merge function Unit Tests for 2048 game.
"""

import unittest

import Merge


class MyTestCase(unittest.TestCase):

    def test_merge_case1(self):
        self.assertSequenceEqual(Merge.merge([2, 0, 2, 4]), [4, 4, 0, 0])

    def test_merge_case2(self):
        self.assertSequenceEqual(Merge.merge([0, 0, 2, 2]), [4, 0, 0, 0])

    def test_merge_case3(self):
        self.assertSequenceEqual(Merge.merge([2, 2, 0, 0]), [4, 0, 0, 0])

    def test_merge_case4(self):
        self.assertSequenceEqual(Merge.merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])

    def test_merge_case5(self):
        self.assertSequenceEqual(Merge.merge([8, 16, 16, 8]), [8, 32, 8, 0])

    def test_merge_case6(self):
        self.assertSequenceEqual(Merge.merge([4, 4, 8]), [8, 8, 0])

    def test_merge_case7(self):
        self.assertSequenceEqual(Merge.merge([2, 0, 2, 2]), [4, 2, 0, 0])

    def test_merge_case8(self):
        self.assertSequenceEqual(Merge.merge([0, 2]), [2, 0])

    # --------------------------------------------------------------------------

    def test_can_shift(self):
        self.assertTrue(Merge.can_shift([2, 0, 2, 4]))
        self.assertTrue(Merge.can_shift([0, 0, 2, 2]))
        self.assertFalse(Merge.can_shift([2, 2, 0, 0]))
        self.assertFalse(Merge.can_shift([2, 2, 2, 2, 2]))
        self.assertFalse(Merge.can_shift([8, 16, 16, 8]))
        self.assertFalse(Merge.can_shift([4, 4, 8]))
        self.assertTrue(Merge.can_shift([2, 0, 2, 2]))
        self.assertTrue(Merge.can_shift([0, 2]))


if __name__ == '__main__':
    unittest.main()
