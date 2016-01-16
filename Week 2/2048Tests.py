"""
Merge function Unit Tests for 2048 game.
"""

import unittest

import twentyfortyeight


class MyTestCase(unittest.TestCase):
    def test_reset(self):
        obj = twentyfortyeight.TwentyFortyEight(2, 2)
        obj.reset()
        self.assertEqual("[[0, 0][0, 0]]", obj)


if __name__ == '__main__':
    unittest.main()
