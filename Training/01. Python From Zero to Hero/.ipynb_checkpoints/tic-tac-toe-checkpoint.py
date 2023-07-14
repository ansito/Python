# GAME TIC TAC TOE
# code by as

# 1A
def display_board(board):
    pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    pos = board

    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[6]) + '|' + ' {} '.format(pos[7]) + '|' + ' {} '.format(pos[8]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print('-'*11)
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[3]) + '|' + ' {} '.format(pos[4]) + '|' + ' {} '.format(pos[5]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print('-'*11)
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[0]) + '|' + ' {} '.format(pos[1]) + '|' + ' {} '.format(pos[2]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')

# 1B
def display_board_preview():
    pos = [1,2,3,4,5,6,7,8,9]

    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[6]) + '|' + ' {} '.format(pos[7]) + '|' + ' {} '.format(pos[8]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print('-'*11)
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[3]) + '|' + ' {} '.format(pos[4]) + '|' + ' {} '.format(pos[5]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print('-'*11)
    print(                 '   '+ '|' + '   '                 + '|' + '   ')
    print(' {} '.format(pos[0]) + '|' + ' {} '.format(pos[1]) + '|' + ' {} '.format(pos[2]))
    print(                 '   '+ '|' + '   '                 + '|' + '   ')

# 2
def player_input(num_player):
    
    choice = 'Wrong'
    ready_or_not = 'Wrong'
    num_player = int(num_player)
    
    while choice not in ('X','O'):
        choice = input('Player {} : Do you want to be X or O? :'.format(num_player))
        if choice not in ('X','O'):
            print('Wrong Input! Please input X or O.')
        else:
            pass
    
    return choice

# 3
def place_marker(board, marker, position):
    
    board[position-1] = marker
    return board

# 4
def win_check(board, mark):
    
    check_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    check_board = board
    
    if check_board[6] == mark and check_board[7] == mark and check_board[8] == mark:
        return True
    elif check_board[6] == mark and check_board[4] == mark and check_board[2] == mark:
        return True
    elif check_board[6] == mark and check_board[3] == mark and check_board[0] == mark:
        return True
    elif check_board[3] == mark and check_board[4] == mark and check_board[5] == mark:
        return True
    elif check_board[0] == mark and check_board[3] == mark and check_board[6] == mark:
        return True
    elif check_board[0] == mark and check_board[4] == mark and check_board[8] == mark:
        return True
    elif check_board[0] == mark and check_board[1] == mark and check_board[2] == mark:
        return True
    elif check_board[2] == mark and check_board[5] == mark and check_board[8] == mark:
        return True
    elif check_board[1] == mark and check_board[4] == mark and check_board[7] == mark:
        return True
    else:
        return False

# 5
import random

def choose_first():
    
    player = ''
    choosen = random.randint(1,2)
    if choosen == 1:
        player = 'Player 1'
        print('{} will go first.'.format(player))
    else:
        player = 'Player 2'
        print('{} will go first.'.format(player))
    
    return choosen

# 6
def space_check(board, position):
    
    position = int(position)
    if board[position-1] == ' ':
        return True # space on the board is available
    else:
        return False # space on the board is not available

# 7
def full_board_check(board):
    
    check = False
    for item in board:
        if item == ' ':
            check = False # Not Full
            break
        else:
            check = True # Full
            pass
    return check

# 8
def player_choice(board,num_player):
    
    choice = 'WRONG'
    input_range = range(1,10)
    
    # while with condition with parameter isdigit, not in input_range, or space availability
    while choice.isdigit() == False or choice not in input_range or space_check(board,choice) == False:
        choice = input('Player {}, Choose your next position (1-9): '.format(num_player))
        if choice.isdigit() == False or int(choice) not in input_range or space_check(board,choice) == False:
            print('Wrong Input. Please input the correct number (1-9)')
        else:
            choice = int(choice)   # convert str choice to be int, IMPORTANT!!
            return choice

# 9
def replay():
    
    choice = 'WRONG'
    
    while choice not in ('Yes','No'):
        choice = input('Do you want to play again? Yes or No: ')
        if choice == 'Yes':
            return True
        elif choice == 'No':
            return False
        else:
            print("Wrong Input. Please type 'Yes' or 'No'. ")

# 10
def print_credit(letter):
    patterns = {1:'  *   *****',2:' * *  *',3:'***** *****',4:'*   *     *',5:'*   * *****'}
    alphabet = {'AS':[1,2,3,4,5]}
    for item in alphabet[letter.upper()]:
        print(patterns[item])

# MAIN PROGRAM #
# code by AS

from IPython.display import clear_output

def tic_tac_toe():
    myboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_one = False
    player_two = False
        
    print('Welcome to Tic Tac Toe!')
    display_board_preview()
    
    choosen = choose_first()
    # function choose player 1 or 2 to start the game
    if choosen == 1:
        player_one = True
        num_player = 1
        mark_player_one = player_input(num_player)
        if mark_player_one == 'X':
            mark_player_two = 'O'
        else:
            mark_player_two = 'X'
        
    else:
        player_two = True
        num_player = 2
        mark_player_two = player_input(num_player)
        if mark_player_two == 'X':
            mark_player_one = 'O'
        else:
            mark_player_one = 'X'
    
    # looping start the game
    while full_board_check(myboard) == False or win_check(myboard,mark_player_one) == False or win_check(myboard, mark_player_two) == False: # OK
        if full_board_check(myboard) == True and win_check(myboard,mark_player_one) == False and win_check(myboard,mark_player_two) == False:
            print('GAME OVER !')
            break
        elif player_one == True and win_check(myboard,mark_player_two) == False:
            num_player = 1
            choice = player_choice(myboard, num_player)
            place_marker(myboard,mark_player_one,choice)
            player_one = False
            player_two = True
        elif player_two == True and win_check(myboard,mark_player_one) == False:
            num_player = 2
            choice = player_choice(myboard, num_player)
            place_marker(myboard,mark_player_two,choice)
            player_one = True
            player_two = False
        elif win_check(myboard,mark_player_one) == True or win_check(myboard,mark_player_two) == True:
            # Announce the winner
            print('Congratulations. Player {} is the WINNER!'.format(num_player))
            break

        clear_output()     # Function for clear the output, make the board still in the same board. It should be before display_board(myboard)
        display_board(myboard)
        
    
    # If want to replay the game
    wanna_replay = replay()
    if wanna_replay == True:
        clear_output()
        tic_tac_toe()
    else:
        clear_output()
        print('Thank you for playing the game. Good bye!')
        print('Credit to:')
        print_credit('AS')

# END OF MAIN PROGRAM #