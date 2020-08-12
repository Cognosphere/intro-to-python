'''
Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''
def display_board(board):
    pass

#Test display_board function
test_board = ['_','X','O','X','O','X','O','X','O','X']
display_board(test_board)



'''
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
Hint: Use while loops to continually ask until you get a correct answer.
'''
def player_input():
    pass

#Test player_input function
print(player_input())

'''
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a chosen position (number 1-9). Then, it is assigned to the board.
'''
def place_marker(board, marker, position):
    pass

#test place_marker function
place_marker(test_board,'$',8)
display_board(test_board)

'''
Step 4: Write a function that takes in a board and a marker (X or O) and then checks to see if that marker has won.
'''
def win_check(board, mark):
    pass

#test win_check function
print(win_check(test_board,'X')) #SHOULD RETURN TRUE!

'''
Step 5: Write a function that uses the random module to randomly decide which player goes first. 
Hint: Remember random.randint()?
Return a string of which player went first. 
'''
import random

def choose_first():
    pass


'''
Step 6: Write a function that returns a boolean indicating whether a space on the board is available.
'''
def space_check(board, position):
    pass


'''
Step 7: Write a function that checks if the board is full and returns a boolean value. If the board is full, return True. Otherwise, return False.
'''
def full_board_check(board):
    pass


'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
'''
def player_choice(board):
    pass


'''
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():
    pass


'''
Step 10: Now the hardest part! Use while loops and the functions you've made to run the game! (it's hard!)
'''
print('Welcome to Tic Tac Toe!')

#while True:
    #Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break