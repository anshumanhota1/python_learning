rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
# Create a list of options  
options = [rock, paper, scissors]
# Get user input    
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Check if the user input is valid
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(options[user_choice])
    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(options[computer_choice])
    # Determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
# The code above implements a simple Rock, Paper, Scissors game where the user can choose one of the three options and the computer randomly selects one as well. The winner is determined based on the rules of the game.  

