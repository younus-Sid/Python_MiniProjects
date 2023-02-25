"""
In this game the player chooses between Rock, Paper, Scissors against the computer.
"""

# Code For Rock Paper Scissors

# Sign Of 'Rock', 'Paper', 'Scissors'
rock = '''
    _______
---'   ____)
      (_____)
      (_____)         ROCK {}
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)    PAPER {}
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)    SCISSORS {}
      (____)
---.__(___)
'''


import random

print("Welcome! To Rock Paper Scissors Game")
player_choice = int(input("What do you choose? [ 0 For 'Rock', 1 For 'Paper', 2 For 'Scissors' ]\n"))
computer_choice = random.randint(0, 2)
if player_choice in range(0, 3):
    x = "[ YOU ]"
    sign_list = [rock.format(x), paper.format(x), scissors.format(x)]
    print(sign_list[player_choice])

    x = "[ COMPUTER ]"
    sign_list = [rock.format(x), paper.format(x), scissors.format(x)]
    print(sign_list[computer_choice] + "\n")

    if player_choice == 0: # 'Rock'
        if computer_choice == 0:   # 'Rock'
            print("IT'S A DRAW.")
        elif computer_choice == 1: # 'Paper'
            print("YOU LOSE!")
        elif computer_choice == 2: # 'Scissors'
            print("YOU WIN!")
    elif player_choice == 1: # 'Paper'
        if computer_choice == 1:   # 'Paper'
            print("IT'S A DRAW.")
        elif computer_choice == 2: # 'Scissors'
            print("YOU LOSE!")
        elif computer_choice == 0: # 'Rock'
            print("YOU WIN!")
    elif player_choice == 2: # 'Scissors'
        if computer_choice == 2:   # 'Scissors'
            print("IT'S A DRAW.")
        elif computer_choice == 0: # 'Rock'
            print("YOU LOSE!")
        elif computer_choice == 1: # 'Paper'
            print("YOU WIN!")
else:
    print("Invalid choice! You Lose.")

print("")
