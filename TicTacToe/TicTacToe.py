import Player

player1 = Player()
player2 = Player()
table = [[" "," "," "],[" "," "," "],[" "," "," "]]
name : ""
pattern : ""
turn : int
win_flag = False
max_room_no =0

# def set_turn(turn):
    # self.turn = turn

def get_player_info():
    player1.set_name(input('Type name of Player1 : '))
    player1.set_pattern(input('Type patter of Player1 : '))

    player2.set_name(input('Type name of Player2 : '))
    player2.set_pattern(input('Type patter of Player2 : '))

def decide_order():
    player1.set_order(1)
    player2.set_order(2)
    if (player1.get_order() < player2.get_order()):
        print(player1.get_name + "'s turn will be first.")
        return 1
    else:
        print(player2.get_name + "'s turn will be first.")
        return 2


def change_turn(turn):
    if(turn ==1):
        return 2
    elif(turn == 2):
        return 1

def check_win(table,input_array, pattern):
    x = input_array[0]
    y = input_array[1]
    match_count = 0

    # check vertically to top
    index = -1
    match_count = check_vertical(table,x,y,index,match_count)

    # 2 match patterns are at upper
    if match_count == 2:
        return True

    # check vertically to lower
    index = 1
    match_count = check_vertical(table, x, y, index, match_count)

    # 2 match patterns are at lower
    if match_count == 2:
        return True

    # check horizontally to left
    index = -1
    match_count = check_horizontal(table, x, y, index, match_count)

    # 2 match patterns are at left
    if match_count == 2:
        return True

    # check horizontally to right
    index = 1
    match_count = check_horizontal(table, x, y, index, match_count)

    # 2 match patterns are at lower
    if match_count == 2:
        return True

    # check left and top in slope
    index = -1
    match_count = check_slope(table, x, y, index, match_count)

    # 2 match patterns are at left
    if match_count == 2:
        return True

    # check right and down to right
    index = 1
    match_count = check_slope(table, x, y, index, match_count)

    # 2 match patterns are at lower
    if match_count == 2:
        return True

    return False


def check_horizontal(table,x,y,index,match_count):
    while True:
        if (x + index == 3 or x + index == -1):
            break
        if (table[x + index][y] == pattern):
            ++match_count
        if index < 0:
            --index
        else:
            ++index
    return match_count

def check_vertical(table, x, y, index, match_count):
    while True:
        if (y + index == 3 or y + index == -1):
            break
        if (table[x][y + index] == pattern):
            ++match_count
        if index < 0:
            --index
        else:
            ++index
    return match_count

def check_slope(table, x, y, index, match_count):
    while True:
        if (y + index == 3 or y + index == -1 or x + index == 3 or x + index == -1):
            break
        if (table[x + index][y + index] == pattern):
            ++match_count
        if index < 0:
            --index
        else:
            ++index
    return match_count

def check_slope_rev(table, x, y, index_x, index_y, match_count):
    while True:
        if (y + index_y == 3 or y + index_y == -1 or x + index_x == 3 or x + index_x == -1):
            break
        if (table[x + index_x][y + index_y] == pattern):
            ++match_count
        if index_x < 0:
            --index_x
        else:
            ++index_x
        if index_y < 0:
            --index_y
        else:
            ++index_y
    return match_count



def play_game(turn):
    if(turn == 1):
        name = player1.get_name()
        pattern = player1.get_pattern()
    elif(turn == 2):
        name = player1.get_name()
        pattern = player1.get_pattern()

    print("Player "+ name +"'s turn")

    # todo To reduce nested if
    while True:
        input = input("Type row and column position (e.g. 1,2")
        input_array = input.split(",")

        if(len(input_array) == 2):
            if(table[input_array[0]][input_array[1]].strip() == ""):
                table[input_array[0]][input_array[1]] = pattern
                show_table()
                if (check_win(table,input_array, pattern)):
                    print("Player "+ name + " win the game.")
                    break
                play_game(change_turn(turn))
                break
            print("The position is already filled. Please choose another.")
        else:
            print("Input format is wrong. Type again.")


def show_table():
    for row in range(2):
        for column in range(2):
            print(table[row][column], end=" ")
        print("\n")



def main():
    get_player_info()
    turn = decide_order()
    play_game(turn)

if __name__ == '__main__':
    main()