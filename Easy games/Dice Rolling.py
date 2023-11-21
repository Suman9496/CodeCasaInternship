import random

def roll_dice():
    input("Press Enter to roll the dice...")
    number = random.randint(1, 6)
    print(f"You rolled a {number}!")

if __name__ == "__main__":
    while True:
        roll_dice()
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break
