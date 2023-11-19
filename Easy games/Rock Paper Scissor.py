import random

options = ["Rock", "Paper", "Scissors"]

def play_game():
    # Get the user's choice
    user_choice = input("Choose Rock, Paper, or Scissors: ")

    # Check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        play_game()
        return

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Check who won
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("Rock smashes scissors! You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("Paper covers rock! You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()
