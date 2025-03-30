#
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
#
# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1
#
# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.
#
# _________________________________________________________________________________________________________

print("Welcome to Python Pizza Deliveries!")

# Getting user input and converting to uppercase
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# Price Calculation Based on Size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size selection!")

# Adding Pepperoni Cost
if pepperoni == "Y":
    if size == "S":
        bill += 2  # $2 for small pizza
    else:
        bill += 3  # $3 for medium/large pizzas

# Adding Extra Cheese Cost
if extra_cheese == "Y":
    bill += 1  # Extra cheese costs $1

# Final Output
print(f"Your total bill is: ${bill}")


