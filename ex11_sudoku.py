################################################################
# FILE : ex11_sudoku.py
# WRITER : Aviad Dudkewitz
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION:  This program solve a Sudoku boards
# using the principle of backtracking.
################################################################
from ex11_backtrack import general_backtracking

def print_board(board, board_size=9):
    """ prints a sudoku board to the screen

    ---  board should be implemented as a dictinary 
         that points from a location to a number {(row,col):num}
    """ 
    for row in range(board_size):
        if(row%3 == 0):
            print('-------------')
        toPrint = ''
        for col in range(board_size):
            if(col%3 == 0):
                toPrint += '|'
            toPrint += str(board[(row,col)])
        toPrint += '|'
        print(toPrint)
    print('-------------')


def load_game(sudoku_file):
    """
    This function load a file to a sudoku board.
    :param sudoku_file: path
    :return: Dictionary that represents a Sudoku board
    """
    return_dict = {}
    with open(sudoku_file, "r") as load_board:
        for row, line in enumerate(load_board):
            col = 0
            for letter in line:
                if letter is not "," and letter is not "\n":
                    return_dict[(row, col)] = int(letter)
                    col += 1
    return return_dict


def check_board(board, x, *args):
    """
    The function determines if the assignment in coordinate X is valid.
    :return: True or False
    """
    current_number = board[x]
    num_of_square = (x[0]//3, x[1]//3)
    if board[x] in range(1, 10):
        # check row
        for row in range(9):
            current_key = (row, x[1])
            if x != current_key and board[current_key] == current_number:
                return False
        # check column
        for col in range(9):
            current_key = (x[0], col)
            if current_key != x and board[current_key] == current_number:
                return False
        # check relative square 3X3
        for relative_row in range(3):
            for relative_col in range(3):
                current_key = (num_of_square[0]*3 + relative_row,
                               num_of_square[1]*3 + relative_col)
                if current_key != x and board[current_key] == current_number:
                    return False
        return True
    else:
        return False


def run_game(sudoku_file, print_mode = False):
    """
    This function checks if the given Sudoku board has solution.
    if it is and print_mode=True - prints the solution.
    :param sudoku_file: path
    :param print_mode: boolean variable. default to False.
    :return: True or False
    """
    game_borad = load_game(sudoku_file)
    list_of_items = []
    # create a list of the empty squares:
    for key in game_borad.keys():
        if game_borad[key] == 0:
            list_of_items.append(key)
    if general_backtracking(sorted(list_of_items), game_borad, 0, range(1,10),
                            check_board):
        if print_mode is True:
            print_board(game_borad)
        return True
    else:
        return False

