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
    player1_arr = [['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''], [player1_mark, player1_mark, player1_mark, '', '', ''],
                   [player1_mark, player1_mark, player1_mark, '', '', '']]
    player2_arr = [['', '', '', player2_mark, player2_mark, player2_mark],
                   ['', '', '', player2_mark, player2_mark, player2_mark], ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]

    player1_win_arr = [['', '', '', player1_mark, player1_mark, player1_mark],
                       ['', '', '', player1_mark, player1_mark, player1_mark], ['', '', '', '', '', ''],
                       ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]
    player2_win_arr = [['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''],
                       ['', '', '', '', '', ''], [player2_mark, player2_mark, player2_mark, '', '', ''],
                       [player2_mark, player2_mark, player2_mark, '', '', '']]
    draw_board(player1_arr, player2_arr, player1_mark, player2_mark)
    is_continue = True
    turn = 1
    while is_continue:
        print(f'Player\'s {turn}')

        current_x, current_y = receive_coordinate_values('current')
        next_x, next_y = receive_coordinate_values('next')

        if turn == 1:
            while is_continue:
                player1_arr, is_jump = move(current_x, current_y, next_x, next_y, player1_mark, player1_arr,
                                            player2_arr)
                if not player1_arr:
                    return

                if is_win(player1_arr, player1_win_arr):
                    print(f'Player{turn} is win')
                    is_continue = False

                if is_jump:
                    next_input = input('Will you input again. Type Y to jump next')
                    if next_input != 'Y':
                        break
                    current_x, current_y, next_x, next_y = ask_next_move(next_x, next_y, player1_arr, player2_arr,
                                                                         player1_mark, player2_mark)

                else:
                    break
            turn = 2
        elif turn == 2:
            while is_continue:
                player2_arr, is_jump = move(current_x, current_y, next_x, next_y, player2_mark, player2_arr,
                                            player1_arr)
                if not player2_arr:
                    return

                if is_win(player2_arr, player2_win_arr):
                    print(f'Player{turn} is win')
                    is_continue = False
                if is_jump:
                    next_input = input('Will you input again. Type Y to jump next')
                    if next_input != 'Y':
                        break
                    current_x, current_y, next_x, next_y = ask_next_move(next_x, next_y, player1_arr, player2_arr,
                                                                         player1_mark, player2_mark)
                else:
                    break
            turn = 1
        draw_board(player1_arr, player2_arr, player1_mark, player2_mark)


def ask_next_move(next_x, next_y, player1_arr, player2_arr, player1_mark, player2_mark):
    """
    Ask for next move
    :param next_x: next position of item on x coordinate
    :param next_y: next position of item on y coordinate
    :param player1_arr: player1's playing result array
    :param player2_arr: player2's playing result array
    :param player1_mark: player1's mark
    :param player2_mark: player2's mark
    :return:
        next_x: next position of item on x coordinate
        next_y: next position of item on y coordinate
        next_x: next position of item on x coordinate
        next_y: next position of item on y coordinate
    """
    draw_board(player1_arr, player2_arr, player1_mark, player2_mark)
    current_x = next_x
    current_y = next_y
    next_x, next_y = receive_coordinate_values('next')
    return current_x, current_y, next_x, next_y


def receive_coordinate_values(status):
    """
    Receive input for the current location
    :return:
        x for current x location
        current_y for current y location
    """
    while True:
        try:
            x = int(input('Input ' + status + ' position of x'))
            if GRIP_SIZE > x > -1:
                break
            else:
                print('Invalid input')
        except Exception:
            print('Invalid input')

    while True:
        try:
            y = int(input('Input ' + status + ' position of y'))
            if GRIP_SIZE > y > -1:
                break
            else:
                print('Invalid input')
        except Exception:
            print('Invalid input')

    return x, y


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


def draw_board(player1_arr, player2_arr, player1_mark, player2_mark):
    """
    Draw board of plyaers
    :param player1_arr: player1's playing result array
    :param player2_arr: player2's playing result array
    :param player1_mark: player1's mark on board
    :param player2_mark: player2's mark on board
    :return:
    """
    print('   ', end='')
    for grip_y in range(GRIP_SIZE):
        print(grip_y, end='  ')

    print()
    for grip_x in range(GRIP_SIZE):
        print(f'{grip_x} |', end='')
        for grip_y in range(GRIP_SIZE):
            if player1_arr[grip_x][grip_y]:
                print(player1_mark, end=' |')
            elif player2_arr[grip_x][grip_y]:
                print(player2_mark, end=' |')
            else:
                print(' ', end=' |')
        print()


def move(current_x, current_y, next_x, next_y, player_mark, player_arr, other_player_arr):
    """
    Move the mark to the next position from current
    :param current_x: current position of item on x coordinate
    :param current_y: current position of item on y coordinate
    :param next_x: current position of item on y coordinate
    :param next_y: next position of item on y coordinate
    :param player_mark: mark on board of target player
    :param player_arr: player's playing result array
    :param other_player_arr: other player's playing result array
    :return:
        player_arr : player's playing result array
        jump :
            If jumped, return True
            Else, False
    """
    jump = False
    # is current location valid
    if not player_arr[current_x][current_y]:
        print('Invalid move')
        return None, jump

    # is current location valid
    if player_arr[current_x][current_y] != player_mark:
        print('Invalid move')
        return None, jump

    # is next location valid
    if '' != player_arr[next_x][next_y] or '' != other_player_arr[next_x][next_y]:
        # next move is not blank
        print('Invalid move')
        return None, jump

    if not is_valid_move(current_x, current_y, next_x, next_y):
        print('Invalid move')
        return None, jump

    if is_one_step_move(current_x, current_y, next_x, next_y):
        pass
    elif is_valid_jump(current_x, current_y, next_x, next_y, player_arr, other_player_arr):
        jump = True
    else:
        print('Invalid move')
        return None, jump

    player_arr[current_x][current_y] = ''
    player_arr[next_x][next_y] = player_mark
    return player_arr, jump


def is_valid_move(current_x, current_y, next_x, next_y):
    if next_x not in (current_x, current_x - 1, current_x - 2, current_x + 1, current_x + 2):
        return False
    if next_y not in (current_y, current_y - 1, current_y - 2, current_y + 1, current_y + 2):
        return False
    return True


def is_valid_jump(current_x, current_y, next_x, next_y, player_arr, other_player_arr):
    if next_x not in (current_x, current_x - 2, current_x + 2):
        return False
    if next_y not in (current_y, current_y - 2, current_y + 2):
        return False

    x_diff = next_x - current_x
    y_diff = next_y - current_y

    x = get_jumped_coordinate(current_x, x_diff)
    y = get_jumped_coordinate(current_y, y_diff)

    if not player_arr[x][y]:
        if not other_player_arr[x][y]:
            # no item to jump. Gap is empty
            return False

    return True


def get_jumped_coordinate(current, diff):
    if diff > 0:
        return current + 1
    elif diff < 0:
        return current - 1
    return current


def is_one_step_move(current_x, current_y, next_x, next_y):
    if next_x not in (current_x, current_x - 1, current_x + 1):
        return False
    if next_y not in (current_y, current_y - 1, current_y + 1):
        return False
    return True


def is_win(player_arr, player_win_arr):
    """
    Check whether the player is win or not.
    :param player_arr: player's playing result array
    :param player_win_arr: Expected wining position on board for player
    :return:
        If win, True
        Else, False
    """
    if np.array_equal(player_arr, player_win_arr):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
