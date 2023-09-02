def main():
    # Ask user's fruit
    fruit = input("Item: ").lower()
    # Retrieve the calories for the fruit
    cal = calories(fruit)
    # Print the calories if available
    if cal:
        print(f"Calories: {cal}")


def calories(item):
    # Define a dictionary of fruits
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    # Check if the item is present in the fruits dictionary
    if item in fruits:
        return fruits[item]


if __name__ == "__main__":
    main()
