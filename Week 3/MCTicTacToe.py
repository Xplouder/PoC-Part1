"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 1  # Number of trials to run
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
    while board.check_win() is None:
        rand_empty_cell = random.choice(board.get_empty_squares())
        board.move(rand_empty_cell[0], rand_empty_cell[1], player)
        provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    Score the completed board and update the scores grid. As the function
    updates the scores grid directly, it does not return anything.
    :param player: Machine Player
    :param board: board from a completed game
    :param scores: grid of scores (a list of lists) with the same dimensions
    as the Tic-Tac-Toe board
    """
    if scores is None:
        dim = board.get_dim()
        scores = [[0 for _ in dim] for _ in dim]

    result = board.check_win()
    if result != provided.DRAW:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                cell_value = board.square(row, col)
                if cell_value == result:
                    scores[row][col] += 1
                elif cell_value == provided.EMPTY:
                    continue
                else:
                    scores[row][col] -= 1


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple. It is an error to call this
    function with a board that has no empty squares (there is no possible next
    move), so your function may do whatever it wants in that case. The case
    where the board is full will not be tested.
    :param scores:
    :param board:
    """
    max_coords = []
    max_value = 0

    if len(board.get_empty_squares()) > 0:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                temp = scores[row][col]
                if temp != provided.EMPTY:
                    if temp > max_value:
                        max_coords = []
                        max_value = temp
                        max_coords.append((row, col))
                    elif temp == max_value:
                        max_coords.append((row, col))

    return random.choice(max_coords)


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. Return a move for the machine player in the
    form of a (row, column) tuple.
    :param trials:
    :param player:
    :param board:
    """
    return random.choice(board.get_empty_squares())

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
