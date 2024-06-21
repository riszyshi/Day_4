from random import randint  # Import randint for generating random numbers

print("WELCOME TO SWERTRES!\n")  # Game title

user_input = input("Place your 3-digit bet: ")  # Prompt user for a 3-digit bet

print(f"Your 3-digit bet: {user_input}")  # Display user's bet

# Generate a 3-digit winning number as a string
winning_number = ([(randint(0, 9)) for _ in range(3)])

print(f"The winning number is: {winning_number}")  # Display the winning number

# Determine and print the result
if user_input == winning_number:  # Exact match
    print("You Won!")
elif sorted(user_input) == sorted(winning_number):  # Digits are match but in different order
    print("You have Partially Win!")
else:  # No match
    print("Better luck next time!")