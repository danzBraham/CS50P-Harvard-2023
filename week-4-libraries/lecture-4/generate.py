import random


def main():
    # choice
    # coin = random.choice(["heads", "tails"])
    # print(coin)

    # randint
    # number = random.randint(1, 10)
    # print(number)

    # shuffle
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    print(cards)


if __name__ == "__main__":
    main()
