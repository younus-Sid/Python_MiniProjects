"""
In this game the player chooses between Rock, Paper, Scissors against the computer.
"""

import random
def play():
    user_input = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer_guess = random.choice(['r','p','s'])
    if user_input == computer_guess:
    	print("It's a tie !!")
    	return play()
    if is_win(user_input,computer_guess):
    	return "Woohoo!! You Won."
    return "Sorry!! You lost"
    
def is_win(player1, player2):
	if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
		return True
print(play())	
