import random


def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Set the maximum number of guesses to 10
    max_guesses = 10

    # Initialize the number of guesses to 0
    guesses = 0

    # Start the game loop
    while guesses < max_guesses:
        # Prompt the user to enter a guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the secret number in", guesses, "guesses.")
            break
        elif guess < secret_number:
            print("Too low.")
            guesses += 1
        else:
            print("Too high.")
            guesses += 1

    # If the user ran out of guesses, print the secret number
    if guesses == max_guesses:
        print("Sorry, you ran out of guesses. The secret number was", secret_number)


# Play the game
play_game()
