import random

def guess_number_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        # Prompt the user to enter their guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    guess_number_game()