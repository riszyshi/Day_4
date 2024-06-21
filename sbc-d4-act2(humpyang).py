from random import randint  # Imports randint function from the random module for random number generation

print("THIS IS HUMPYANG GAME!")  # Game title

player1 = ""  # Initializing the player's choice as an empty string

# Prompts the player to choose between "FOLD" and "UNFOLD" until a valid input is provided
while player1 not in ["FOLD", "UNFOLD"]:
    player1 = input("Choose [FOLD or UNFOLD]: ").upper()  # Take inputs and converts it to uppercase
    if player1 not in ["FOLD", "UNFOLD"]:  # Checks if the input is valid
        print("Invalid input. Please choose either FOLD or UNFOLD.")  # Prompts the user to input a valid choice if the input is invalid

# Randomly choosing "FOLD" or "UNFOLD" for Computer 1
computer1 = "FOLD" if randint(0, 1) == 0 else "UNFOLD"
print(f"Computer 1: {computer1}")  # Display Computer 1's choice

# Randomly choosing "FOLD" or "UNFOLD" for Computer 2
computer2 = "FOLD" if randint(0, 1) == 0 else "UNFOLD"
print(f"Computer 2: {computer2}")  # Display Computer 2's choice

# Determining the result based on the player's and computers' choices
if player1 == computer1 == computer2:  # If all choices are the same
    print("Result: Draw!")  # It's a draw
elif player1 != computer1 and player1 != computer2:  # If the player's choice is different from both computers' choices
    print("Result: You Won")  # Dispays if player 1 wins
else:  # If none of the above conditions are met
    winner = "Computer 1" if player1 == computer2 else "Computer 2"  # Determine the winner among the computers
    print(f"Result: {winner} Won")  # Prints the result with the winner's name