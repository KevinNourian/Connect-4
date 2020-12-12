'''
Connect Four is a two-player connection board game, in which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. In this program I used numpy to create the board and used 1 and 2 to show the two different color pieces. 
'''

import numpy as np

ROWS = 6
COLUMNS = 7

def start_board():
    '''
    Creates a matrix of zeros with the specified dimensions.
    '''
    board = np.zeros((ROWS,COLUMNS))
    return board


def flip_board(board):
    '''
    Flips the matrix on its x axis. The matrix will fill up from the bottom of the matrix.
    '''
    board = np.flip(board, 0)
    return board


def current_board(board, col, row):
    '''
    Returns the board status at each stage of the game.
    '''
    return board


def print_board(board):
    '''
    Displays the board status at each stage of the game.
    '''
    print(board)


def matrix_full(board):
    '''
    Displays a message and ends the program if the matrix is full.
    '''
    num_of_non_zeros = np.count_nonzero(board)

    if num_of_non_zeros >= 42:
        print ()
        print ('************************************************')
        print ('*    THE BOARD IS FULL. EXITING THE PROGRAM    *')
        print ('************************************************')
        game_over()


def player_turn(board, player):
    '''
    Returns the column that the player has chosen. Checks that the column is not full by checking the last row of the column.
    '''
    if player == 1:
        try:
            col = int(input('\nPlayer 1, choose column (1-7). Enter 0 to end: ')) - 1
            assert col + 1 >= 0 # Tests if number entered is positive.
        except ValueError:
            print("Enter an integer only.\n")
        except AssertionError:
            print("Enter a positive integer only.\n")
        else:
            return col

    if player == 2:
        try:
            col = int(input('\nPlayer 2, choose column (1-7). Enter 0 to end: ')) - 1
            assert col + 1 >= 0 # Tests if number entered is positive.
        except ValueError:
            print("Enter an integer only.\n")
        except AssertionError:
            print("Enter a positive integer only.\n")
        else:
            return col


def row_determination(board, col, player):
    '''
    Returns the row that the next piece will occcupy.
    '''
    if col == -1: # If zero(0) is entered.
        game_over()

    if player == 1:
        try:
            for row in range (ROWS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    break
        except IndexError:
            print("Enter an integer (1-7) or 0 only.\n")
        finally:
            return row

    if player == 2:
        try:
            for row in range (ROWS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    break
        except IndexError:
            print("Enter an integer (1-7) or 0 only.\n")
        finally:
            return row

def horizontal_check(board, player):
    '''
    Checks if a connect 4 horizontal has occured.
    '''
    count = 0
    for row in range(ROWS):
        for col in range (COLUMNS):
            if player == 1:
                if board[row][col] == 1:
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print ()
                    print ('************************************************')
                    print ('*    CONNECT 4 HORIZONTAL -- PLAYER 1 WINS     *')
                    print ('************************************************')
                    game_over()

            if player == 2:
                if board[row][col] == 2:
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print ()
                    print ('************************************************')
                    print ('*    CONNECT 4 HORIZONTAL -- PLAYER 2 WINS     *')
                    print ('************************************************')
                    game_over()


def vertical_check(board, player):
    '''
    Checks if a connect 4 vertical has occured.
    '''
    count = 0
    for col in range(COLUMNS):
        for row in range (ROWS):
            if player == 1:
                if board[row][col] == 1:
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print ()
                    print ('************************************************')
                    print ('*     CONNECT 4 VERTICAL -- PLAYER 1 WINS      *')
                    print ('************************************************')
                    game_over()

            if player == 2:
                if board[row][col] == 2:
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print ()
                    print ('************************************************')
                    print ('*     CONNECT 4 VERTICAL -- PLAYER 2 WINS      *')
                    print ('************************************************')
                    game_over()


def positive_diagonal_check(board, player):
    '''
    Checks if a connect 4 diagonal in the positive direction has occured.
    '''
    for row in range(ROWS):
        for col in range (COLUMNS):
            if player == 1:
                if col + 3 <= COLUMNS - 1 and row + 3 <= ROWS - 1:
                    if board[row][col] == 1 and\
                    board[row + 1][col + 1] == 1 and\
                    board[row + 2][col + 2] == 1 and\
                    board[row + 3][col + 3] == 1:
                        print ()
                        print ('************************************************')
                        print ('* CONNECT 4 POSITIVE DIAGONAL -- PLAYER 1 WINS *')
                        print ('************************************************')
                        game_over()

            if player == 2:
                if col + 3 <= COLUMNS - 1 and row + 3 <= ROWS - 1:
                    if board[row][col] == 2 and\
                    board[row + 1][col + 1] == 2 and\
                    board[row + 2][col + 2] == 2 and\
                    board[row + 3][col + 3] == 2:
                        print ()
                        print ('************************************************')
                        print ('* CONNECT 4 POSITIVE DIAGONAL -- PLAYER 2 WINS *')
                        print ('************************************************')
                        game_over()


def negative_diagonal_check(board, player):
    '''
    Checks if a connect 4 diagonal in the negative direction has occured.
    '''
    for row in range(ROWS):
        for col in range (COLUMNS):
            if player == 1:
                if col - 3 >= 0 and row + 3 <= ROWS - 1:
                    if board[row][col] == 1 and\
                    board[row + 1][col - 1] == 1 and\
                    board[row + 2][col - 2] == 1 and\
                    board[row + 3][col - 3] == 1:
                        print ()
                        print ('************************************************')
                        print ('* CONNECT 4 NEGATIVE DIAGONAL -- PLAYER 1 WINS *')
                        print ('************************************************')
                        game_over()

            if player == 2:
                if col - 3 >= 0 and row + 3 <= ROWS - 1:
                    if board[row][col] == 2 and\
                    board[row + 1][col - 1] == 2 and\
                    board[row + 2][col - 2] == 2 and\
                    board[row + 3][col - 3] == 2:
                        print ()
                        print ('************************************************')
                        print ('* CONNECT 4 NEGATIVE DIAGONAL -- PLAYER 2 WINS *')
                        print ('************************************************')
                        game_over()


def game_over():
    '''
    Prints game over message and ends the program.
    '''
    print ()
    print ('************************************************')
    print ('*                  GAME OVER                   *')
    print ('************************************************')
    print ()
    exit()


board = start_board()
print()
print (board)
player = 1

while True:
    if player == 1:
        matrix_full(board)
        col = player_turn(board, player)
        row = row_determination(board, col, player)
        board = flip_board(board)
        print_board(board)
        board = flip_board(board)
        current_board(board, col, row)
        horizontal_check(board, player)
        vertical_check(board, player)
        positive_diagonal_check(board, player)
        negative_diagonal_check(board, player)
        player = 2

    if player == 2:
        matrix_full(board)
        col = player_turn(board, player)
        row = row_determination(board, col, player)
        board = flip_board(board)
        print_board(board)
        board = flip_board(board)
        current_board(board, col, row)
        horizontal_check(board, player)
        vertical_check(board, player)
        positive_diagonal_check(board, player)
        negative_diagonal_check(board, player)
        player = 1
