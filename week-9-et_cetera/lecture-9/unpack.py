def main():
    # * means unpacking list
    # coins = [100, 50, 25]
    # print(total(*coins), "Knuts")

    # ** means unpacking dict
    # coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    # print(total(**coins), "Knuts")

    # Positional
    f(100, 50, 25)
    f(100, 50, 25, 5)
    f(100)

    print("=============================")

    # Named
    f(galleons=100, sickles=50, knuts=25)
    f(galleons=100, sickles=50)
    f(galleons=100)


def f(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Named: {kwargs}")


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


if __name__ == "__main__":
    main()
