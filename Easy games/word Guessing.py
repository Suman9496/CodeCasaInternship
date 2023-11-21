import random


def choose_word():
    words = ["python", "java", "programming", "coding", "developer", "hangman"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def word_guessing_game():
    secret_word = choose_word()
    guessed_letters = []

    print("Welcome to Word Guessing Game!")

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")

        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                print("Incorrect! Try again.")
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print(f"Congratulations! You guessed the word: {secret_word}")
                break
            else:
                print("Incorrect! Try again.")
        else:
            print("Invalid input. Try again.")

        if set(secret_word) <= set(guessed_letters):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    word_guessing_game()
