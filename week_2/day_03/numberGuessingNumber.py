
# # Task 04: Number Guessing Game

# ## Objective

# Create a simple number guessing game where the program generates a random number, and the user has to guess it.
    
# ## Requirements

# 1. Generate a random number between a specified range.
# 2. Ask the user to guess the number.
# 3. Provide feedback on whether the guess is too high, too low, or correct.
# 4. Allow the user to continue guessing until they guess the correct number.
# 5. Display the number of attempts it took to guess correctly.

# ## Additional Challenges

# 1. Implement error handling to ensure the user inputs a valid number.
# 2. Allow the user to choose the range of numbers for the guessing game.
# 3. Enhance the program to provide hints or clues based on the user's previous guesses.

import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Get the range of numbers from the user
    while True:
        try:
            min_num = int(input("Enter the minimum number of the range: "))
            max_num = int(input("Enter the maximum number of the range: "))
            break
        except ValueError:
            print("Please enter valid integers for the range.")

    # Generate a random number within the specified range
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
            attempts += 1

            if guess < min_num or guess > max_num:
                print(f"Your guess is out of the range. Please guess between {min_num} and {max_num}.")
                continue

            if secret_number < guess :
                print("Too low!")
            elif secret_number > guess :
                print("Too high!")
            else:
                print("Congratulations! You guessed the number {} correctly in {} attempts!".format(secret_number,
                                                                                                    attempts))
                break
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        number_guessing_game()
    else:
        print("Thank you for playing!")


# Start the game
number_guessing_game()
    
    
    