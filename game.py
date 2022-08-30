#!/usr/bin/env python3

from IPython.display import clear_output
import random


def display(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    player1_marker = ''

    while player1_marker != 'X' and player1_marker != 'O':
        clear_output()
        player1_marker = input('Player 1, choose X or O: ').upper()

    if player1_marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):
    if position in range(1, 10):
        board[position] = marker
    else:
        print("Position out of range")


def win_check(board, mark):

    if board[1] == mark and board[2] == mark and board[3] == mark:  # Bottom
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:  # noqa: E501  Diag bottom left to top right
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:  # Left
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:  # noqa: E501 middle left to right
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:  # top
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:  # noqa: E501 diag top left to bottom right
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:  # noqa: E501 middle bottom to top
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:  # right
        return True


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) and space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))

    return position


def replay():
    restart = str(input("Game ended, do you wanna play again: (Yes or No) ").lower)

    if restart == "yes":
        return True
    else:
        return False


print('Welcome to Tic-Tac-Toe')

while True:
    theBoard = [' ']*10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + 'goes first')

    play_game = input('Are you ready to play? Enter yes or No. ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display(theBoard)
                print('Congratulations, you won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'

        if turn == 'Player 2':
            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)

            if win_check(theBoard, player2):
                display(theBoard)
                print('Congratulations, you won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
