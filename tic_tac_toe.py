# Create a function that asks users to choose X or O
def u1_choice():
    var1 = input("Player_1 please choose 'X' or 'O'. Player_2 will default to the other symbol: ").upper()

    while var1 not in ('X', 'O'):
        var1 = input("Player_1 please choose 'X' or 'O'. Player_2 will default to the other symbol: ").upper()

    if var1 == 'X':
        var2 = 'O'
    else:
        var2 = 'X'

    #print(f'Player 1: {var1}.')
    #print(f'Player 2: {var2}.')
    return [var1, var2]



# Create A Function that displays the board according to user inputs up to now
def board(users, var1, var2):
    # Clear prior output
    from IPython.display import clear_output
    clear_output()

    print(f'Player 1: {var1}.')
    print(f'Player 2: {var2}.')

    #First display the board positions:
    print('Here are the board positions')
    print('1', '2', '3')
    print('4', '5', '6')
    print('7', '8', '9')

    #Display the current board
    print('Here is the current board:')
    print(users[0:3])
    print(users[3:6])
    print(users[6:9])



# Create a function that asks user for input and turns it into a move on the board
def pos_choice(users, move_ct, var1, var2):
    pos = input("Please enter a position on the board using numbers 1 - 9: ")


    while pos.isdigit() == False or int(pos) < 1 or int(pos) > 9 or users[int(pos)-1] != ' ':
        pos = input("This position is occupied or out of range. Please enter another position on the board using numbers 1 - 9: ")


    posint = int(pos)

    if move_ct%2 != 0:
        users[posint-1] = var1
    else:
        users[posint-1] = var2

    board(users, var1, var2)



# Create a function that checks the board for winning combo
def winning(users, move_ct, var1, var2):
    win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    user1 = []
    user2 = []
    pos_ct = 1

    # First convert the board to positions for each player
    for num in range(1, 10):

        #print(users[num-1])
        #print(pos_ct)
        if users[num-1] == var1:
            user1.append(pos_ct)
        elif users[num-1] == var2:
            user2.append(pos_ct)
        else:
            pass

        pos_ct += 1

    #print(pos_ct)
    #print(move_ct)
    #print(user1)
    #print(user2)

    # Check if either user has a winning combo
    for combo in win_comb:
        comb = set(combo)
        exit_game = 0

        if comb.issubset(set(user1)):
            print('User 1 has won!')
            exit_game = 1
            return exit_game
        elif comb.issubset(set(user2)):
            print('User 2 has won!')
            exit_game = 1
            return exit_game
        elif move_ct == 9:
            print('This is a draw.')
            exit_game = 1
            return exit_game
        else:
            pass
    else:
        print('No winner yet. Continue to next user.')
        return exit_game



# Create a function that asks users if they would like to continue playing
def gameon():
    goon = input('Would you like to Play Again? Enter Y or N: ')

    while goon not in ('Y', 'N', 'y', 'n'):
        print(goon.upper())
        goon = input('Would you like to keep playing? Please enter Y or N. No other character allowed.: ')

    if goon.upper() == 'Y':
        restart = 1
        return restart
    else:
        restart = 0
        return restart



def tic_tac_toe():
    #Define board and counters/flags:
    exit_game_tag = 0
    move_ct = 1
    restart = 1
    users = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    [var1, var2] = u1_choice()
    board(users, var1, var2)

    while exit_game_tag != 1 or restart == 1:
        #print(f'exit_game_tag is {exit_game_tag}.')

        # Check if game should exit
        if exit_game_tag != 0:
            # Check if players want to play again
            restart = gameon()

            # If players want to restart, reset the board and all counters/flags
            if restart == 1:
                move_ct = 1
                exit_game_tag = 0
                users = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            # If player does not want to restart, exit game.
            else:
                print('Exit Game.')
                break

        # If game should continue, run the next move
        elif exit_game_tag == 0:
            #Asks User to choose where to place next move
            print(f'This is move #{move_ct}: ')
            pos_choice(users, move_ct, var1, var2)

            #Check if anyone has won yet
            exit_game_tag = winning(users, move_ct, var1, var2)

            move_ct += 1

        # Otherwise break the game
        else:
            break



#Run tic_tac_toe:
tic_tac_toe()
    