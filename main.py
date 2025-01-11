# Tic Tac Toe Game

board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "
three_in_a_row = False
next_player = 'X'
win_sets = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
X_replaced = []
O_replaced = []
count = 0


# Determines if a player won the game
def is_winner(sets, replaced_list):
    for a_set in sets:
        if set(replaced_list).issuperset(a_set):
            return True
    return False


print('Welcome to Tic Tac Toe!\nPlayer 1 goes first and plays with X, Player 2 plays with O')
print(board)

while not three_in_a_row:
    if count == 9:
        break
    player_input = input('Which square will you select(1 - 9): ')
    if int(player_input) in X_replaced or int(player_input) in O_replaced:
        print("This space has already been marked. Please choose an unmarked space.")
        continue
    count += 1
    if next_player == 'X':
        X_replaced.append(int(player_input))
        board = board.replace(player_input, next_player)
        print(board)
        three_in_a_row = is_winner(win_sets, X_replaced)
    else:
        O_replaced.append(int(player_input))
        board = board.replace(player_input, next_player)
        print(board)
        three_in_a_row = is_winner(win_sets, O_replaced)
    if next_player == 'X' and not three_in_a_row and count < 9:
        next_player = 'O'
        print(f'Next player is Player 2 (O)')
    elif next_player == 'O' and not three_in_a_row and count < 9:
        next_player = 'X'
        print(f'Next player is Player 1 (X)')
if count < 9:
    print(f'The Winner is {next_player}!')
else:
    print("It's a Draw!")
