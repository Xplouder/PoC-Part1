"""
Thomco's unit tests for 2048(Full)
"""

import random
import unittest
import TwentyFortyEight as twenty_forty_eight

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

directions = {UP: 'up', DOWN: 'down', LEFT: 'left', RIGHT: 'right'}


# Add test case for out of bounds index exception in set_tile, get_tile

class TestsTwentyFortyEight(unittest.TestCase):
    def test_init_single(self):

        height = random.randrange(4, 12)
        width = random.randrange(4, 12)
        game = twenty_forty_eight.TwentyFortyEight(height, width)
        self.assertEqual(game.get_grid_height(), height)
        self.assertEqual(game.get_grid_width(), width)

        zeros = sum([row.count(0) for row in game._grid])
        empties = len(game._empty_tiles)
        self.assertEqual(empties, height * width - 2)
        self.assertEqual(empties, zeros)
        print game
        print "Empty tiles: %d" % len(game._empty_tiles)

    def test_init_multi(self):
        TEST_CASES = [(0, 0), (1, 0), (0, 1), (1, 1), (4, 4), (8, 8), (50, 100)]

        for test in TEST_CASES:
            game = twenty_forty_eight.TwentyFortyEight(*test)
            self.assertEqual(game.get_grid_height(), test[0])
            self.assertEqual(game.get_grid_width(), test[1])
            zeros = sum([row.count(0) for row in game._grid])
            empties = len(game._empty_tiles)
            self.assertEqual(empties, max(test[0] * test[1] - 2, 0))
            self.assertEqual(empties, zeros)

    def test_init_initial(self):
        test_cases = [(0, 0), (1, 0), (0, 1), (1, 1), (4, 4), (8, 8),
                      (500, 1000)]

        for test in test_cases:
            game = twenty_forty_eight.TwentyFortyEight(*test)
            print
            print game._initial

    def test_new_tile(self):
        height = 6
        width = 12
        game = twenty_forty_eight.TwentyFortyEight(height, width)
        print game
        print "Empty tiles: %d" % len(game._empty_tiles)

        tile_counter = 2

        while tile_counter < (height * width):
            print game.new_tile()
            tile_counter += 1
            zeros = sum([row.count(0) for row in game._grid])
            empties = len(game._empty_tiles)
            self.assertEqual(empties, height * width - tile_counter)
            self.assertEqual(empties, zeros)

        print game
        print "Empty tiles: %d" % len(game._empty_tiles)
        game.new_tile()
        self.assertFalse(sum([row.count(0) for row in game._grid]))
        self.assertFalse(game._empty_tiles)
        game.new_tile()
        self.assertFalse(sum([row.count(0) for row in game._grid]))
        self.assertFalse(game._empty_tiles)

    def test_new_tile_bigtest(self):
        HEIGHT = 100
        WIDTH = 200
        game = twenty_forty_eight.TwentyFortyEight(HEIGHT, WIDTH)

        num_times = HEIGHT * WIDTH
        for _ in range(num_times):
            game.new_tile()
        twos = sum([row.count(2) for row in game._grid])
        fours = sum([row.count(4) for row in game._grid])

        print "two: %d / %d - %4.1f percent" % (
            twos, num_times, (twos * 100.0) / num_times)
        print "fours: %d / %d - %4.1f percent" % (
            fours, num_times, (fours * 100.0) / num_times)

    def test_get_set_tile(self):

        for test in range(10):
            height = random.randrange(4, 12)
            width = random.randrange(4, 12)
            game = twenty_forty_eight.TwentyFortyEight(height, width)
            print "Test %d: height: %d, %d\n" % (test, height, width)
            row = random.randrange(height - 1)
            col = random.randrange(width - 1)
            value = 2 ** random.randrange(11)

            game.set_tile(row, col, value)
            self.assertEqual(game._grid[row][col], value)
            self.assertEqual(game.get_tile(row, col), value)

    def test_merge(self):
        tests = [
            [[], []],
            [[0], [0]],
            [[0, 0, 0, 0], [0, 0, 0, 0]],
            [[2, 0, 2, 4], [4, 4, 0, 0]]

        ]
        for test in tests:
            self.assertEqual(twenty_forty_eight.merge(test[0]), test[1])

    def test_move(self):
        game = twenty_forty_eight.TwentyFortyEight(4, 4)
        for _ in range(4): game.new_tile()
        print game
        for direction, text in directions.iteritems():
            print
            print 'MERGE %s:' % text
            game.move(direction)
            print '%s\n\n' % str(game)

    def test_OWL_test_cases(self):
        OWL_TESTCASE_BOARD = ((0, 0, 4), (0, 1, 4), (0, 2, 4), (0, 3, 4),
                              (1, 0, 4), (1, 1, 0), (1, 2, 0), (1, 3, 4),
                              (2, 0, 4), (2, 1, 0), (2, 2, 0), (2, 3, 4),
                              (3, 0, 4), (3, 1, 4), (3, 2, 4), (3, 3, 4))
        OWL_TESTCASE_MOVE = (UP, LEFT, LEFT)
        return

    def test_OWL1(self):
        game = twenty_forty_eight.TwentyFortyEight(4, 4)
        game.set_tile(0, 0, 4)
        game.set_tile(0, 0, 4)
        game.set_tile(0, 1, 4)
        game.set_tile(0, 2, 4)
        game.set_tile(0, 3, 4)
        game.set_tile(1, 0, 4)
        game.set_tile(1, 1, 0)
        game.set_tile(1, 2, 0)
        game.set_tile(1, 3, 4)
        game.set_tile(2, 0, 4)
        game.set_tile(2, 1, 0)
        game.set_tile(2, 2, 0)
        game.set_tile(2, 3, 4)
        game.set_tile(3, 0, 4)
        game.set_tile(3, 1, 4)
        game.set_tile(3, 2, 4)
        game.set_tile(3, 3, 4)
        game.move(UP)
        print game

    def test_OWL2(self):
        game = twenty_forty_eight.TwentyFortyEight(5, 6)
        game.set_tile(0, 0, 0)
        game.set_tile(0, 1, 2)
        game.set_tile(0, 2, 4)
        game.set_tile(0, 3, 8)
        game.set_tile(0, 4, 8)
        game.set_tile(0, 5, 32)
        game.set_tile(1, 0, 16)
        game.set_tile(1, 1, 2)
        game.set_tile(1, 2, 4)
        game.set_tile(1, 3, 16)
        game.set_tile(1, 4, 64)
        game.set_tile(1, 5, 32)
        game.set_tile(2, 0, 0)
        game.set_tile(2, 1, 2)
        game.set_tile(2, 2, 4)
        game.set_tile(2, 3, 8)
        game.set_tile(2, 4, 0)
        game.set_tile(2, 5, 32)
        game.set_tile(3, 0, 16)
        game.set_tile(3, 1, 16)
        game.set_tile(3, 2, 16)
        game.set_tile(3, 3, 16)
        game.set_tile(3, 4, 16)
        game.set_tile(3, 5, 16)
        game.set_tile(4, 0, 16)
        game.set_tile(4, 1, 8)
        game.set_tile(4, 2, 4)
        game.set_tile(4, 3, 4)
        game.set_tile(4, 4, 16)
        game.set_tile(4, 5, 2)
        print game
        print 'MOVE LEFT'
        game.move(LEFT)
        print game

    def test_OWL3(self):
        game = twenty_forty_eight.TwentyFortyEight(4, 4)
        game.set_tile(0, 0, 2)
        game.set_tile(0, 1, 0)
        game.set_tile(0, 2, 0)
        game.set_tile(0, 3, 0)
        game.set_tile(1, 0, 0)
        game.set_tile(1, 1, 2)
        game.set_tile(1, 2, 0)
        game.set_tile(1, 3, 0)
        game.set_tile(2, 0, 0)
        game.set_tile(2, 1, 0)
        game.set_tile(2, 2, 2)
        game.set_tile(2, 3, 0)
        game.set_tile(3, 0, 0)
        game.set_tile(3, 1, 0)
        game.set_tile(3, 2, 0)
        game.set_tile(3, 3, 2)
        print game
        print 'MOVE LEFT'
        game.move(LEFT)
        print game

    def test_OWL_new_tile(self):
        twos, fours = 0, 0
        height, width = 2, 2
        LOOP_COUNT = 1000
        GRID_SIZE = height * width
        game = twenty_forty_eight.TwentyFortyEight(height, width)
        for count in range(LOOP_COUNT):
            game.set_tile(0, 0, 0)
            game.set_tile(0, 1, 0)
            game.set_tile(1, 0, 0)
            game.set_tile(1, 1, 0)
            for _ in range(GRID_SIZE): game.new_tile()
            twos += sum([row.count(2) for row in game._grid])
            fours += sum([row.count(4) for row in game._grid])

        new_tiles = LOOP_COUNT * GRID_SIZE
        twos_ratio = float(twos) / new_tiles
        fours_ratio = float(fours) / new_tiles

        self.assertAlmostEqual(twos_ratio, 0.9, places=1)
        self.assertAlmostEqual(fours_ratio, 0.1, places=1)

        print "twos:  %5d / %d = %8.6f (%4.2f%%)" % (
            twos, new_tiles, twos_ratio, 100.0 * twos_ratio)
        print "fours: %5d / %d = %8.6f (%4.2f%%)" % (
            fours, new_tiles, fours_ratio, 100.0 * fours_ratio)


if __name__ == '__main__':
    unittest.main()
