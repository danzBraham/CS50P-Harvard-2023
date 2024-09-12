def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = get_number("Insert Coin: ")
        if coin in [25, 10, 5]:
            amount_due -= coin

    print(f"Change Owed: {abs(amount_due)}")


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
