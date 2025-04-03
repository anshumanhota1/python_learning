
word_list = ["aardvark", "baboon", "camel"]

# step 1

# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
# #  is, "Wrong" if it's not.

# import random

# word =random.choice(word_list)
# print(word)
# guess = input("Guess a letter ").lower()

# for item in word:
#     if item == guess:
#         print("Right")
#     else:
#         print("Wrong")


# step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# guess = input("Guess a letter: ").lower()

# blanks = ["_"] * len(chosen_word)
# # print(" ".join(blanks))  # Display the blanks with spaces between them

# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

# # for letter in chosen_word:
# #     if letter == guess:
# #         print("Right")
# #     else:
# #         print("Wrong")
# for i in range(len(chosen_word)):
#     if chosen_word[i] == guess:
#         blanks[i] = guess

# print(" ".join(blanks))  # Show the updated blanks

# step 3
# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win.")

# Step 4

# import random
# stages = [r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# word_list = ["aardvark", "baboon", "camel"]

# lives = 6

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You lose.")

#     if "_" not in display:
#         game_over = True
#         print("You win.")

#     print(stages[lives])

# step 6

import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
