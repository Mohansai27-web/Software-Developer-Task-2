import random


def number_guessing_game():
    # Set the upper and lower limits for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number between 1 and 100
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            # Prompt the user for input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Compare the user's guess with the target number
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(
                    f"\nCongratulations! You guessed the correct number ({target_number}) in {attempts} attempts!"
                )
                break
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


if __name__ == "__main__":
    number_guessing_game()
