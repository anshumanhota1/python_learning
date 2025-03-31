# Positive or Negative number:

# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# Even or Odd number:

# number = int(input("Enter a number: "))

# if number % 2 ==0:
#     print("This number is even number .")

# else:
#     print("Number is ODD. ")

# Sum of First N Natural numbers
# number = int(input("Enter a number: "))

# sum = 0
# for i in range(number+1):
#     sum = sum + i
# print(sum)

# Sum of N Natural numbers

# number = int(input("Enter a number: "))
# sum = 0
# for i in range(number+1):
#     sum = sum + i
# print(sum)

# Greatest of two numbers: 

# number1 = int(input("Enter a number 1: "))
# number2 = int(input("Enter a number 2: "))

# if number1 > number2 :
#     print(f" The greatest number is {number1}")

# else:
#     print(f" The greatest number is {number2}")

# Greatest of the Three numbers: 

# number1 = int(input("Enter a number 1: "))
# number2 = int(input("Enter a number 2: "))
# number3 = int(input("Enter a number 3: "))

# if number1 > number2 and number1 > number3:
#     print(f"greatest number is {number1}")

# elif number2 > number1 and number2 > number3:
#     print(f"greatest number is {number2}")

# else:
#     print(f"greatest number is {number3}")

# Leap year or not:

# year = int(input("Enter a Year: "))

# if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0):
#     print(f"The {year} year is leap year. ")

# else:
#     print(f"{year}not a leap year. ")

# import calendar

# year = int(input("Enter a year: "))

# if calendar.isleap(year):
#     print(year, " is a leap year")
# else:
#     print(year, "is not a leap year.")

# Check Prime numbers

# num = int(input("Enter a number: "))
# flag = 0
# for i in range(2,num):
#   if num%i==0:
#     flag = 1
#     break
# if flag == 1:
#   print('Not Prime')
# else:
#   print("Prime")


# Check list of Prime numbers from 1 to 100
# for num in range(2, 101):  # We start from 2 because 1 is not a prime number
#     flag = 0  # Reset flag for each number
#     for i in range(2, num):
#         if num % i == 0:  # If num is divisible by any number other than 1 and itself
#             flag = 1  # It's not a prime number
#             break  # No need to check further
#     if flag == 0:  # If the flag is still 0, it means it's a prime number
#         print(num)

# Sum of digits of a number:

# num = input("Enter Number: ")
# sum = 0

# for i in num:
#     sum = sum + int(i)

# print(sum)

















