def main():
    # Define the menu items and their corresponding prices
    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    # Initialize the total cost to 0
    total = 0

    # Loop until the user inputs ctrl + d
    while True:
        try:
            # Prompt the user for an item
            item = input("Item: ").title()
            # Check if the item is present in the menu items
            if item in items:
                # Add the item's price to the total cost
                total += items[item]
                # Print the updated total cost with 2 decimal places
                print(f"Total: ${total:.2f}")
        except EOFError:
            # Handle the EOFError exception
            print()
            break


if __name__ == "__main__":
    main()
