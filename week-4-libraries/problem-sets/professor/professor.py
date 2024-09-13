import random


def main():
    lvl = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                correct_answer = x + y

                if answer == correct_answer:
                    score += 1
                    break
                print("EEE")

                if i == 2:
                    print(f"{x} + {y} = {correct_answer}")
            except ValueError:
                print("EEE")
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
