import functions as f

f.screen_clear()
#screen_clear()
print('Welcome to Tic Tac Toe!\n')

replay = 'Y'

while replay == 'Y':
    # Initialize board to all spaces.  Note that [0] contains #.
    # This is to improve code readability by allowing indexing from 1-9
    # rather than 0-8.  The value in [0] could be anything non-' '.
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    name1, mark1, name2, mark2 = f.player_setup()
    f.display_board(board)

    while True:
        # First player's turn
        f.get_move(board, name1, mark1)
        f.display_board(board)
        if f.is_final_move(board, name1, mark1):
            break #-----game over-----
    
        # Second player's turn
        f.get_move(board, name2, mark2)
        f.display_board(board)
        if f.is_final_move(board, name2, mark2):
            break #-----game over-----

    replay = f.get_replay_response()
        
print('\nProgram Complete')
