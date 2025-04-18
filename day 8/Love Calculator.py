# ?? This is a difficult challenge! ?? 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times   # L occurs 1 time 
# R occurs 1 times   # O occurs 0 times 
# U occurs 2 times   # V occurs 0 times 
# E occurs 2 times   # E occurs 2 times 
# Total = 5          # Total = 3 

# Love Score = 53

def calculate_love_score(name1, name2):
    # Step 1: Combine and lowercase the names
    combined_names = (name1 + name2).lower()

    # Step 2: Count letters in 'TRUE'
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Step 3: Count letters in 'LOVE'
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Step 4: Combine counts to form the score
    love_score = int(f"{true_count}{love_count}")
    
    # Step 5: Print the result
    print(f"Your love score is: {love_score}")


calculate_love_score("Angela Yu", "Jack Bauer")
