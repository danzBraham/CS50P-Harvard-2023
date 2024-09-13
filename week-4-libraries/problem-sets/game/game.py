import random


def main():
    level = get_int("Level: ")
    guess(level)


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


def guess(level):
    random_number = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if guess < random_number:
            print("Too small!")
            continue
        if guess > random_number:
            print("Too large!")
            continue
        if guess == random_number:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
