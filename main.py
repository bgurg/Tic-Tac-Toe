#Author: bgurg
#Date: 2018-12-26
#Reference:
#   - Udemy class
#   - Complete-Python-3-Bootcamp-master
#   - 04-Milestone Project

#---------------------------------------------------------------------------

def screen_clear():
    '''
    Just scrolls existing text off the screen so that user only sees
    current text.
    '''
    print('\n'*50)
    return

#---------------------------------------------------------------------------

def player_setup():
    '''
    Randomly select which player name will go first and have user
    select which mark ("X" or "O") to associate with players.  
    INTPUTS: none
    OUTPUTS: list of player names and marks where. Note that order of 
             player names in list determines who plays first
             (e.g. in ["Player 2","X","Player 1","O"], "Player 2" would
             play first and use the "X" mark)
        
    '''
    
    players = ['Player 1', 'Player 2']
    mark1s = ['X', 'O']

    name1 = random.choice(players)
    name2 = ''.join(set(players) - set([name1]))
       
    print(f'{name1} was randomly selected to go first.')
    
    mark1 = input(f'Choose mark for {name1} (X/O): ').upper()
    
    while mark1 not in mark1s:
        mark1 = input (f'Please enter either "X" or "O": ').upper()
    
    mark2 = ''.join(set(mark1s) - set(mark1))   

    return [name1, mark1, name2, mark2]

#---------------------------------------------------------------------------

def display_board(board):
    '''
    Prints board values to screen in a 3 x 3 matrix
    INPUTS: board = list of values on board (e.g. ['X','O',' ','X',...])
    OUTPUTS: none
    '''
    
    screen_clear()
    indent = ' '*20

    print('{} {} | {} | {}'.format(indent, board[7], board[8], board[9]))
    print('{}---+---+---'  .format(indent))
    print('{} {} | {} | {}'.format(indent, board[4], board[5], board[6]))
    print('{}---+---+---'  .format(indent))
    print('{} {} | {} | {}'.format(indent, board[1], board[2], board[3]))
    print('\n')
    
    return

#---------------------------------------------------------------------------

def win_check(board, mark):
    '''
    Determine whether mark has won the game
    INPUTS:
        - board = list of values on board (e.g. ['X','O',' ','X',...])
        - mark = character ('X' or 'O')
    OUTPUTS:
        - whether mark has won the game (boolean)
    '''
    
    win_positions = [board[7]+board[8]+board[9],
                     board[4]+board[5]+board[6],
                     board[1]+board[2]+board[3],
                     board[7]+board[4]+board[1],
                     board[8]+board[5]+board[2],
                     board[9]+board[6]+board[3],
                     board[7]+board[5]+board[3],
                     board[1]+board[5]+board[9]
                     ]
    
    win_item = mark*3
    
    # check to see if mark has won game
    for item in win_positions:
        if item == win_item:
            return True

    # mark has not won game
    return False

#---------------------------------------------------------------------------

def get_move(board, name, mark):
    '''
    1. Get valid cell selection from user (i.e. 1-9)
    2. Verify that cell is available (i.e. contains ' ')
    3. Update selected cell if available
    '''
    
    cell = input(f"[{name}] place an '{mark}' in cell (1-9): ")
    
    while True:
        # if cell value is not valid, ask to re-enter
        if cell not in ['1','2','3','4','5','6','7','8','9']:
            cell = input('Invalid entry.  Please try again: ')

        # if selected cell is not available, ask to re-enter
        elif board[int(cell)] != ' ':
            cell = input('Cell not empty.  Please try again: ')

        # add mark to selected cell
        else:                
            board[int(cell)] = mark
            break

    return

#---------------------------------------------------------------------------

def is_final_move(board, name, mark):
    '''
    Checks to see if game is over due to win or tie.
    INPUTS:
        - board = list of values on board (e.g. ['X','O',' ','X',...])
        - name = player name string (e.g. 'Player 1')
        - mark = character ('X' or 'O')
    OUTPUT: 
        - whether the game continues (boolean)
    '''

    # check to see if this move won the game
    if win_check(board, mark):
        print(f'{name} wins!')
        return True
        
    # check to see if board is full (i.e. game ends in a tie)
    elif ' ' not in board:
        print("It's a tie")
        return True
 
    # otherwise, game continues
    return False

#---------------------------------------------------------------------------

def get_replay_response():
    '''
    Have user indicate whether they want to play again
    INPUTS: 
        - none 
    OUTPUTS: 
        - char entered by the user ('Y' or 'N')
    '''
    
    replay = input('Another game (Y/N)? ').upper()
    
    while replay not in ['y','Y','n','N']:
        replay = input('Invalid entry.  Please enter "Y" or "N": ').upper()

    return replay

#---------------------------------------------------------------------------

import random

screen_clear()
print('Welcome to Tic Tac Toe!\n')

replay = 'Y'

while replay == 'Y':
    # Initialize board to all spaces.  Note that [0] contains #.
    # This is to improve code readability by allowing indexing from 1-9
    # rather than 0-8.  The value in [0] could be anything non-' '.
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    name1, mark1, name2, mark2 = player_setup()
    display_board(board)

    while True:
        # First player's turn
        get_move(board, name1, mark1)
        display_board(board)
        if is_final_move(board, name1, mark1):
            break #-----game over-----
    
        # Second player's turn
        get_move(board, name2, mark2)
        display_board(board)
        if is_final_move(board, name2, mark2):
            break #-----game over-----

    replay = get_replay_response()
        
print('\nProgram Complete')
