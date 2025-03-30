print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure. ")

# First Choice: Left or Right
print("\You're at a crossroad. Where do you want to go?")
choice = input("Type 'Left' or 'Right': ").strip().lower()

if choice == "left":
    print("You've reached a lake. There's an island in the middle of the lake.")
    print('Do you want to "wait" for a boat or "swim" across?')

    # Second Choice: Wait or Swim
    choice = input("Type 'Wait' or 'Swim': ").strip().lower()
    
    if choice == "wait":
        print("\nYou safely reach the island. There is a house with 3 doors:")
        print("Red , Yellow , Blue")
        
        # Third Choice: Choose a Door
        choice = input("Which door do you choose? Type 'Red', 'Yellow', or 'Blue': ").strip().lower()
        
        if choice == "red":
            print("\n The room is filled with fire! You are burned alive. \n Game Over.")
        elif choice == "yellow":
            print("\n Congratulations! You found the treasure!  \n You Win!")
        elif choice == "blue":
            print("\n The room is full of wild beasts! You are eaten. \n Game Over.")
        else:
            print("\n Invalid choice. You get lost in the darkness. \n Game Over.")
    else:
        print("\n You try to swim but are attacked by a giant trout! \n Game Over.")

else:
    print("\nYou took the wrong path and fell into a deep hole! \n Game Over.")

# Final Message
print("\n Thanks for playing Treasure Island! Try again for a different ending! ")
