def main():
    # Initialize the amount owed
    owed = 50

    # Continue loop while the owed amount is greater than 0
    while owed > 0:
        # Print the amount due
        print(f"Amount Due: {owed}")

        # Ask the user to insert coins
        pay = int(input("Insert Coin: "))

        # Check if the inserted coin is valid
        if pay in [25, 10, 5]:
            owed -= pay

    # Print the change owed
    print(f"Change Owed: {abs(owed)}")


if __name__ == "__main__":
    main()
