"""
Unit Tests for Monte Carlo Tic-Tac-Toe
"""

import unittest

from aux import poc_ttt_provided as provided

import MCTicTacToe


class TestsMCTicTacToe(unittest.TestCase):
    def test_trial(self):
        counter = 0
        runs = 10000

        initial_board = [[provided.EMPTY, provided.EMPTY, provided.EMPTY],
                         [provided.EMPTY, provided.EMPTY, provided.EMPTY],
                         [provided.EMPTY, provided.EMPTY, provided.EMPTY]]

        for _ in range(runs):
            board1 = provided.TTTBoard(3, False, initial_board)
            board2 = board1.clone()
            MCTicTacToe.mc_trial(board1, provided.PLAYERX)
            MCTicTacToe.mc_trial(board2, provided.PLAYERX)
            if board1._board == board2._board:
                counter += 1

        # assert that generated boards are different 99% of the times
        self.assertTrue((counter / (runs * 1.0)) < 0.01)

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

    def test_get_best_move4(self):
        initial_board = [[provided.EMPTY, provided.PLAYERX, provided.EMPTY],
                         [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                         [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]
        board = provided.TTTBoard(3, False, initial_board)
        scores = [[-3, 6, -2],
                  [8, 0, -3],
                  [3, -2, -4]]

        result = MCTicTacToe.get_best_move(board, scores)
        self.assertTrue(result in [(0, 2), (2, 1)])

    def test_update_scores1(self):
        init_board = [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                      [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                      [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]

        scores = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        board = provided.TTTBoard(3, False, init_board)

        MCTicTacToe.mc_update_scores(scores, board, provided.PLAYERX)

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

        MCTicTacToe.mc_update_scores(scores, board, provided.PLAYERX)

        self.assertSequenceEqual([[0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0]], scores)

    def test_update_scores3(self):
        init_board = [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                      [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                      [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]

        scores = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        board = provided.TTTBoard(3, False, init_board)

        MCTicTacToe.mc_update_scores(scores, board, provided.PLAYERO)

        self.assertSequenceEqual([[1.0, 1.0, -1.0],
                                  [-1.0, 1.0, 0],
                                  [0, 1.0, -1.0]], scores)

    def test_move1(self):
        init_board = [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
                      [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                      [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]

        board = provided.TTTBoard(3, False, init_board)
        move = MCTicTacToe.mc_move(board, provided.PLAYERX, MCTicTacToe.NTRIALS)
        self.assertEqual(move, (1, 2))

    def test_move2(self):
        init_board = [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                      [provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
                      [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]

        board = provided.TTTBoard(3, False, init_board)
        move = MCTicTacToe.mc_move(board, provided.PLAYERX, MCTicTacToe.NTRIALS)
        self.assertEqual(move, (2, 1))


if __name__ == '__main__':
    unittest.main()
