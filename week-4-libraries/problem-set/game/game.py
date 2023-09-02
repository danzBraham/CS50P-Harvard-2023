import random


def main():
    # Get the desired level from the user
    level = get_level()
    # Start the guessing game
    guess(level)


def get_level():
    while True:
        try:
            # Prompt the user to enter the level
            level = int(input("Level: "))
            # Validate the level
            if level > 0:
                return level
        except ValueError:
            pass


def guess(level):
    # Generate a random number within the given level
    target_number = random.randint(1, level)

    while True:
        try:
            # Prompt the user to make a guess
            user_guess = int(input("Guess: "))
            if user_guess < 1:
                continue
        except ValueError:
            pass
        else:
            # Matching users guess with target number
            if user_guess < target_number:
                print("Too small!")
            elif user_guess > target_number:
                print("Too large!")
            else:
                print("Just right!")
                return


if __name__ == "__main__":
    main()
