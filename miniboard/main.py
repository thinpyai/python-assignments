import numpy as np

GRIP_SIZE = 6

def main():
    """
    main method for mini board game
    :return: nothing
    """
    select_player()
    player1_mark = 'O'
    player2_mark = 'X'
    player1_arr = [['','','','','',''], ['','','','','',''],['','','','','',''],['','','','','',''],[player1_mark,player1_mark,player1_mark,'','',''],[player1_mark,player1_mark,player1_mark,'','','']]
    player2_arr = [['', '', '', player2_mark, player2_mark, player2_mark], ['', '', '', player2_mark, player2_mark, player2_mark], ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]
    board= [['', '', '', player2_mark, player2_mark, player2_mark], ['', '', '', player2_mark, player2_mark, player2_mark],['','','','','',''],['','','','','',''],[player1_mark,player1_mark,player1_mark,'','',''],[player1_mark,player1_mark,player1_mark,'','','']]

    player1_win_arr = [['', '', '', player1_mark, player1_mark, player1_mark], ['', '', '', player1_mark, player1_mark, player1_mark], ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]
    player2_win_arr = [['','','','','',''], ['','','','','',''],['','','','','',''],['','','','','',''],[player2_mark,player2_mark,player2_mark,'','',''],[player2_mark,player2_mark,player2_mark,'','','']]
    draw_board(player1_arr, player2_arr, player1_mark, player2_mark, GRIP_SIZE)
    is_continue = True
    turn = 1
    while is_continue:
        print(f'Player\'s {turn}')
        try:
            current_x = int(input('Input current position of x'))
        except Exception:
            print('Invalid input')
            return
        try:
            current_y = int(input('Input current position of y'))
        except Exception:
            print('Invalid input')
            return

        try:
            next_x = int(input('Input next position of x'))
        except Exception:
            print('Invalid input')
            return
        try:
            next_y = int(input('Input next position of y'))
        except Exception:
            print('Invalid input')
            return
        if turn == 1:
            board, player1_arr = move(current_x, current_y, next_x, next_y, player1_mark, board, player1_arr)
            if is_win(player1_arr, player1_win_arr):
                print(f'Player{turn} is win')
                is_continue = False
            turn = 2
        elif turn == 2:
            board, player2_arr = move(current_x, current_y, next_x, next_y, player2_mark, board, player2_arr)
            if is_win(player2_arr, player2_win_arr):
                print(f'Player{turn} is win')
                is_continue = False
            turn = 1
        draw_board(player1_arr, player2_arr, player1_mark, player2_mark, GRIP_SIZE)

def select_player():
    """
    select player number
    :return: nothing
    """
    print("Type 1 to choose player1. If not player 2")
    data = input()
    if data == '1':
        print('You are player1')
    else:
        print('You are player2')

def draw_board(player1_arr, player2_arr, player1_mark, player2_mark, grip_size):
    print('   ', end='')
    for grip_y in range(grip_size):
        print(grip_y, end='  ')

    print()
    for grip_x in range(grip_size):
        print(f'{grip_x} |', end='')
        for grip_y in range(grip_size):
            if player1_arr[grip_x][grip_y]:
                print(player1_mark, end=' |')
            elif player2_arr[grip_x][grip_y]:
                print(player2_mark, end=' |')
            else:
                print(' ', end=' |')
        print()

def move(current_x, current_y, next_x, next_y, player_mark, board, player_arr):
    if not board[current_x][current_y] == player_mark:
        # not current player's mark
        print('Invalid move')
        return
    if '' != board[next_x][next_y]:
        # next moveis not blank
        print('Invalid move')
        return
    #move to just next
    move_OK = False
    if current_x == next_x and (current_y == next_y-1 or current_y == next_y+1) :
        move_OK = True
    elif current_y == next_y and (current_x == next_x-1 or current_x == next_x+1) :
        move_OK = True
    elif (current_y == next_y+1 and current_x == next_x+1) or (current_y == next_y-1 and current_x == next_x-1):
        move_OK = True
    #jump
    if not move_OK:
        if current_x == next_x and (current_y == next_y-2 or current_y == next_y+2) :
            jump = next_y-current_y
            if(jump>0):
                if '' == board[next_x][next_y-1]:
                    print('Invalid move')
                    return
            else:
                if '' == board[next_x][next_y+1]:
                    print('Invalid move')
                    return
        elif current_y == next_y and (current_x == next_x-2 or current_x == next_x+2) :
            jump = next_x - current_x
            if (jump > 0):
                if '' == board[next_x-1][next_y]:
                    print('Invalid move')
                    return
            else:
                if '' == board[next_x+1][next_y]:
                    print('Invalid move')
                    return
        elif (current_y == next_y+2 and current_x == next_x+2) or (current_y == next_y-2 and current_x == next_x-2):
            jump_x = next_x - current_x
            jump_y = next_y - current_y
            if (jump_x >= 0 and jump_y >= 0):
                if '' == board[next_x - 1][next_y -1 ]:
                    print('Invalid move')
                    return
            elif (jump_x <= 0 and jump_y <= 0):
                if '' == board[next_x + 1][next_y + 1]:
                    print('Invalid move')
                    return
            elif (jump_x <= 0 and jump_y >= 0):
                if '' == board[next_x + 1][next_y - 1]:
                    print('Invalid move')
                    return
            elif (jump_x >= 0 and jump_y <= 0):
                if '' == board[next_x - 1][next_y + 1]:
                    print('Invalid move')
                    return

    board[next_x][next_y] = player_mark
    board[current_x][current_y] = ''
    player_arr[current_x][current_y] = ''
    player_arr[next_x][next_y] = player_mark
    return board, player_arr

def is_win(player_arr, player_win_arr):
    if np.array_equal(player_arr, player_win_arr):
        return True
    else:
        return False
if __name__ == '__main__':
    main()

class Player:
    """
    Player class
    """

    def __init__(self):
        pass

