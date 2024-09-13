import random


def main():
    # choice
    coin = random.choice(["heads", "tails"])
    print(coin)

    # randint
    for _ in range(3):
        print(random.randint(1, 10))

    # shuffle
    cards = ["jack", "queen", "king"]
    for _ in range(3):
        random.shuffle(cards)
        print(cards)


if __name__ == "__main__":
    main()
