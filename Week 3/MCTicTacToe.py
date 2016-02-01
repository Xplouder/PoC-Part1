"""
Monte Carlo Tic-Tac-Toe Player
"""

import random

from aux import poc_ttt_gui
from aux import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 200  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function play a game starting with the given player by making
    random moves, alternating between players until the game is in progress.
    :param player:
    :param board:
    """
    # while board.check_win() is None and len(board.get_empty_squares()) > 0:
    #     rand_empty_cell = random.choice(board.get_empty_squares())
    #     board.move(rand_empty_cell[0], rand_empty_cell[1], player)
    #     provided.switch_player(player)

    if board.check_win() is not None:
        return
    empty_squares = board.get_empty_squares()
    rand_empty_square = empty_squares[random.randrange(len(empty_squares))]
    board.move(rand_empty_square[0], rand_empty_square[1], player)
    mc_trial(board, provided.switch_player(player))

    # while board.check_win() is None:
    #     empty_squares = board.get_empty_squares()
    #     rand_empty_square = empty_squares[random.randrange(len(empty_squares))]
    #     board.move(rand_empty_square[0], rand_empty_square[1], player)
    #     provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    Score the completed board and update the scores grid. As the function
    updates the scores grid directly, it does not return anything.
    :param player: Machine Player
    :param board: board from a completed game
    :param scores: grid of scores (a list of lists) with the same dimensions
    as the Tic-Tac-Toe board
    """
    winner = board.check_win()
    if winner == provided.DRAW:
        return

    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            cell_value = board.square(row, col)
            if cell_value == provided.EMPTY:
                continue

            if cell_value == winner:
                scores[row][col] += SCORE_CURRENT
            else:
                scores[row][col] -= SCORE_OTHER

    # game_result = board.check_win()
    # if game_result == provided.DRAW:
    #     return
    #
    # for row in range(board.get_dim()):
    #     for col in range(board.get_dim()):
    #         square_value = board.square(row, col)
    #         if square_value == provided.EMPTY:
    #             continue
    #
    #         if game_result == player and square_value == player:
    #             scores[row][col] += SCORE_CURRENT
    #         elif game_result == player and not square_value == player:
    #             scores[row][col] -= SCORE_OTHER
    #         elif not game_result == player and square_value == player:
    #             scores[row][col] -= SCORE_CURRENT
    #         else:
    #             scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple.
    :param scores:
    :param board:
    """
    max_squares_list = []
    # simulate min integer possible in python without sys lib
    max_value = -99999
    empty_squares_list = board.get_empty_squares()

    # only happen when the board is full, however its not fully protected
    if len(empty_squares_list) == 0:
        # only happen when the board is full, however its not fully protected
        return None

    for empty_square in empty_squares_list:
        temp = scores[empty_square[0]][empty_square[1]]
        if temp > max_value:
            max_squares_list = []
            max_value = temp
            max_squares_list.append(empty_square)
        elif temp == max_value:
            max_squares_list.append(empty_square)
    return random.choice(max_squares_list)


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. Return a move for the machine player in the
    form of a (row, column) tuple.
    :param trials:
    :param player:
    :param board:
    """
    dim = board.get_dim()
    scores = [[0 for _ in range(dim)] for _ in range(dim)]

    for _ in range(trials):
        clone = board.clone()
        mc_trial(clone, player)
        mc_update_scores(scores, clone, player)

    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
