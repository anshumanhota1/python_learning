def life_in_weeks(age):
    Weeks_Lived = age * 52
    Total_Weeks_in_90_Years = 90 * 52
    Weeks_Left = Total_Weeks_in_90_Years - Weeks_Lived
    print(f"You have {Weeks_Left} weeks left.")

# Example with a predefined age (instead of input)
# age = 56  # You can change this value to any age

age = int(input("How old are you ? "))


life_in_weeks(age)

