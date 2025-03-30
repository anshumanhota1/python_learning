# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

maths_score = int(input("How much you have score in maths out of 100 ? "))
english_score = int(input("How much you have score in english out of 100 ? "))

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
elif english_score >= 90:
    print("You're good at english")
# In this case only when a student has over 90 on maths and english, do they get "You are good at everything".
