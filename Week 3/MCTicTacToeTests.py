"""
Unit Tests for Monte Carlo Tic-Tac-Toe
"""

import unittest
import MCTicTacToe
import poc_ttt_provided as provided


class MyTestCase(unittest.TestCase):
    def test_get_best_move1(self):
        initial_board = [[provided.EMPTY, provided.EMPTY],
                         [provided.EMPTY, provided.EMPTY]]
        board = provided.TTTBoard(2, False, initial_board)
        scores = [[0, 0],
                  [3, 0]]

        result = MCTicTacToe.get_best_move(board, scores)
        self.assertTrue(result in [(1, 0)])

    def test_get_best_move2(self):
        initial_board = [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                         [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                         [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]
        board = provided.TTTBoard(3, False, initial_board)
        scores = [[0, 2, 0],
                  [0, 2, 0],
                  [0, 2, 0]]

        result = MCTicTacToe.get_best_move(board, scores)
        self.assertTrue(result in [(2, 1)])

    def test_get_best_move3(self):
        initial_board = [[provided.EMPTY, provided.PLAYERX],
                         [provided.EMPTY, provided.PLAYERO]]
        board = provided.TTTBoard(2, False, initial_board)
        scores = [[3, 3],
                  [0, 0]]

        result = MCTicTacToe.get_best_move(board, scores)
        self.assertTrue(result in [(0, 0)])

    def test_update_scores1(self):
        init_board = [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                      [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                      [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]

        scores = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        board = provided.TTTBoard(3, False, init_board)

        MCTicTacToe.mc_update_scores(scores, board, 2)

        self.assertSequenceEqual([[1.0, 1.0, -1.0],
                                  [-1.0, 1.0, 0],
                                  [0, 1.0, -1.0]], scores)

    def test_update_scores2(self):
        init_board = [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO],
                      [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                      [provided.PLAYERX, provided.PLAYERX, provided.PLAYERO]]

        scores = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        board = provided.TTTBoard(3, False, init_board)

        MCTicTacToe.mc_update_scores(scores, board, 2)

        self.assertSequenceEqual([[0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0]], scores)


if __name__ == '__main__':
    unittest.main()
