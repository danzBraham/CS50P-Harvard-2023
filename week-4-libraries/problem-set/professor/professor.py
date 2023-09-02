import random


def main():
    # Get the desired level from the user
    level = get_level()
    # Initialize the score
    score = 0

    # Run the game for 10 rounds
    for _ in range(10):
        # Generate two random integers based on the level
        first = generate_integer(level)
        second = generate_integer(level)

        # Calculate the correct answer
        answer = first + second

        # Check the user's answer
        if check_answer(first, second, answer):
            score += 1

    # Print the final score
    print(f"Score: {score}")


def get_level():
    # Prompt the user to enter the level until a valid input is provided
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Generate a random integer based on the level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    return random.randint(100, 999)


def check_answer(first, second, answer):
    # Allow the user three attempts to provide the correct answer
    for _ in range(3):
        try:
            # Prompt the user to enter their answer
            user_answer = int(input(f"{first} + {second} = "))

            # Check if the user's answer is correct
            if user_answer == answer:
                return True
            else:
                # Incorrect answer message
                print("EEE")
        except ValueError:
            # Invalid input message
            print("EEE")

    # If the user exhausts all attempts, display the correct answer
    print(f"{first} + {second} = {answer}")
    return False


if __name__ == "__main__":
    main()
