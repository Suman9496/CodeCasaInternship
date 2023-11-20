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


def hangman_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Incorrect! Attempts remaining: {attempts}")

        if set(secret_word) <= set(guessed_letters):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The correct word was: {secret_word}")


if __name__ == "__main__":
    hangman_game()
